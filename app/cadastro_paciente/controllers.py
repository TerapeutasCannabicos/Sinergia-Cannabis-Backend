from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_paciente.model import Paciente
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from .schemas import PacienteSchema
from app.model import BaseModel
from app.utils.filters import filters 
from app.functions import cpf_check, email_check

class PacienteCurrent(MethodView): #/paciente/current

    def get(self):

        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema, many=True) 
        return jsonify(schema.dump(Paciente.query.all())), 200


class PacienteCreate(MethodView): #/paciente

    def post(self):
        schema = PacienteSchema()
        paciente = schema.load(request.json)

        paciente.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[paciente.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=paciente.nome))

        mail.send(msg)

        return schema.dump(paciente), 201

class PacienteDetails(MethodView): #/paciente/<int:id>

    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema)
        paciente = Paciente.query.get_or_404(id)
        return schema.dump(paciente), 200

    def put(self, id):
        paciente = Paciente.query.get_or_404(id)
        schema = PacienteSchema()
        paciente = schema.load(request.json, instance = paciente)

        paciente.save()

        return schema.dump(paciente)

    def patch(self, id):
        paciente = Paciente.query.get_or_404(id)
        schema = PacienteSchema()
        paciente = schema.load(request.json, instance = paciente, partial=True)

        paciente.save()

        return schema.dump(paciente)

    def delete(self,id): 
        paciente = Paciente.query.get_or_404(id)
        paciente.delete(paciente)

        return {}, 204

class PacienteConfirm(MethodView): #paciente-confirm

    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        paciente = Paciente.query.get_or_404(data['identity'])

        if not paciente.active:
            paciente.active = True 
            paciente.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email

    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        paciente  = Paciente.query.filter_by(email=dados['email']).first_or_404()

        if not paciente: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[paciente.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=paciente.nome))
        
        mail.send(msg)

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset

    def patch(self, token):
        try: 
            paciente = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        paciente = Paciente.query.get_or_404(paciente['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        paciente.password = data['password']
        paciente.save()

        return {'msg': 'senha atualizada'}, 200