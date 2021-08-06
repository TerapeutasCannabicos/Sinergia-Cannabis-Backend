from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_medico.model import Medico
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from .schemas import MedicoSchema
from app.utils.filters import filters
from app.functions import cpf_check, email_check
from app.permissions import medico_required

class MedicoLista(MethodView): #/medico/lista
    decorators = [medico_required]
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema, many=True) 
        return jsonify(schema.dump(Medico.query.all())), 200


class MedicoCreate(MethodView): #/medico
    def post(self):
        schema = MedicoSchema()
        medico = schema.load(request.json)

        if not email_check(medico.email) or not cpf_check(medico.cpf):
            return {'error': 'Usuário já cadastrado'} 

        medico.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[medico.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=medico.nome))

        mail.send(msg)

        return schema.dump(medico), 201

class MedicoDetails(MethodView): #/medico/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema)
        medico = Medico.query.get_or_404(id)
        return schema.dump(medico), 200

    def put(self, id):
        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        medico = schema.load(request.json, instance = medico)

        medico.save()

        return schema.dump(medico)

    def patch(self, id):
        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        medico = schema.load(request.json, instance = medico, partial=True)

        medico.save()

        return schema.dump(medico)

    def delete(self,id): 
        medico = Medico.query.get_or_404(id)
        medico.delete(medico)

        return {}, 204

class MedicoConfirm(MethodView): #medico-confirm
    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        medico = Medico.query.get_or_404(data['identity'])

        if not medico.active:
            medico.active = True 
            medico.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        medico  = Medico.query.filter_by(email=dados['email']).first_or_404()

        if not medico: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[medico.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=medico.nome))
        
        mail.send(msg)

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset
    def patch(self, token):
        try: 
            medico = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        medico = Medico.query.get_or_404(medico['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        medico.password = data['password']
        medico.save()

        return {'msg': 'senha atualizada'}, 200