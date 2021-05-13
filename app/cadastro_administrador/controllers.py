from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_administrador.model import Administrador
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from app.cadastro_administrador.schemas import AdministradorSchema
from app.model import BaseModel
from app.utils.filters import filters

class AdministradorCurrent(MethodView): #/administrador/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=AdministradorSchema) 
        return jsonify(schema.dump(Administrador.query.all())), 200


class AdministradorCreate(MethodView): #/administrador
    def post(self):
        schema = AdministradorSchema()
        administrador = schema.load(request.json)

        administrador.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
        recipients=[administrador.email],
        subject= 'Bem-vindo!', 
        html=render_template('email.html', name=administrador.nome))

        mail.send(msg)

        return schema.dump(administrador), 201


class AdministradorDetails(MethodView): #/administrador/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=AdministradorSchema)
        administrador = Administrador.query.get_or_404(id)
        return schema.dump(administrador), 200

    def put(self, id):
        administrador = Administrador.query.get_or_404(id)
        schema = AdministradorSchema()
        administrador = schema.load(request.json, instance = administrador)

        administrador.save()

        return schema.dump(administrador)

    def patch(self, id):
        administrador = Administrador.query.get_or_404(id)
        schema = AdministradorSchema()
        administrador = schema.load(request.json, instance = administrador, partial=True)

        administrador.save()

        return schema.dump(administrador)

    def delete(self,id): 
        administrador = Administrador.query.get_or_404(id)
        administrador.delete(administrador)

        return {}, 204

class AdministradorConfirm(MethodView): #administrador-confirm
    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        administrador = Administrador.query.get_or_404(data['identity'])

        if not administrador.active:
            administrador.active = True 
            administrador.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        administrador  = Administrador.query.filter_by(email=dados['email']).first_or_404()

        if not administrador: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[administrador.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=administrador.nome))
        
        mail.send(msg)

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset
    def patch(self, token):
        try: 
            administrador = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        administrador = Administrador.query.get_or_404(administrador['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        administrador.password = data['password']
        administrador.save()

        return {'msg': 'senha atualizada'}, 200