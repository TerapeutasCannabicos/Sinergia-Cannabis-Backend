from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_lawyer.model import Lawyer
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from .schemas import LawyerSchema
from app.utils.filters import filters
from app.functions import cpf_check, email_check
from app.permissions import lawyer_required
from app.model import BaseModel

class LawyerLista(MethodView): #/lawyer/lista
    decorators = [lawyer_required]
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=LawyerSchema, many=True) 
        return jsonify(schema.dump(Lawyer.query.all())), 200


class LawyerCreate(MethodView): #/lawyer
    def post(self):
        schema = LawyerSchema()
        lawyer = schema.load(request.json)

        if not email_check(lawyer.email) or not cpf_check(lawyer.cpf):
            return {'error': 'Usuário já cadastrado'}

        lawyer.save()

        '''msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[lawyer.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=lawyer.nome))

        mail.send(msg)'''

        return schema.dump(lawyer), 201

class LawyerDetails(MethodView): #/lawyer/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=LawyerSchema)
        lawyer = Lawyer.query.get_or_404(id)
        return schema.dump(lawyer), 200

    def put(self, id):
        lawyer = Lawyer.query.get_or_404(id)
        schema = LawyerSchema()
        lawyer = schema.load(request.json, instance = lawyer)

        lawyer.save()

        return schema.dump(lawyer)

    def patch(self, id):
        lawyer = Lawyer.query.get_or_404(id)
        schema = LawyerSchema()
        lawyer = schema.load(request.json, instance = lawyer, partial=True)

        lawyer.save()

        return schema.dump(lawyer)

    def delete(self,id): 
        lawyer = Lawyer.query.get_or_404(id)
        lawyer.delete(lawyer)

        return {}, 204

class LawyerConfirm(MethodView): #lawyer-confirm
    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        lawyer = Lawyer.query.get_or_404(data['identity'])

        if not lawyer.active:
            lawyer.active = True 
            lawyer.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        lawyer  = Lawyer.query.filter_by(email=dados['email']).first_or_404()

        if not lawyer: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[lawyer.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=lawyer.nome))
        
        mail.send(msg)

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset
    def patch(self, token):
        try: 
            lawyer = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        lawyer = Lawyer.query.get_or_404(lawyer['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        lawyer.password = data['password']
        lawyer.save()

        return {'msg': 'senha atualizada'}, 200