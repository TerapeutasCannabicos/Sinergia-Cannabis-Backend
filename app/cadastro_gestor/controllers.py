from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_gestor.model import Gestor
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from .schemas import GestorSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.functions import cpf_check, email_check

class GestorCurrent(MethodView): #/gestor/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=GestorSchema, many=True) 
        return jsonify(schema.dump(Gestor.query.all())), 200


class GestorCreate(MethodView): #/gestor
    def post(self):
        schema = GestorSchema()
        gestor = schema.load(request.json)

        if not email_check(gestor.email) or not cpf_check(gestor.cpf):
            return {'error': 'Usuário já cadastrado'}        

        gestor.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[gestor.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=gestor.nome))

        mail.send(msg)

        return schema.dump(gestor), 201

class GestorDetails(MethodView): #/gestor/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=GestorSchema)
        gestor = Gestor.query.get_or_404(id)
        return schema.dump(gestor), 200

    def put(self, id):
        gestor = Gestor.query.get_or_404(id)
        schema = GestorSchema()
        gestor = schema.load(request.json, instance = gestor)

        gestor.save()

        return schema.dump(gestor)

    def patch(self, id):
        gestor = Gestor.query.get_or_404(id)
        schema = GestorSchema()
        gestor = schema.load(request.json, instance = gestor, partial=True)

        gestor.save()

        return schema.dump(gestor)

    def delete(self,id): 
        gestor = Gestor.query.get_or_404(id)
        gestor.delete(gestor)

        return {}, 204

class GestorConfirm(MethodView): #gestor-confirm
    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        gestor = Gestor.query.get_or_404(data['identity'])

        if not gestor.active:
            gestor.active = True 
            gestor.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        gestor  = Gestor.query.filter_by(email=dados['email']).first_or_404()

        if not gestor: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[gestor.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=gestor.nome))
        
        mail.send(msg)

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset
    def patch(self, token):
        try: 
            gestor = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        gestor = Gestor.query.get_or_404(gestor['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        gestor.password = data['password']
        gestor.save()

        return {'msg': 'senha atualizada'}, 200