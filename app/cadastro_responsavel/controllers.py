from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_responsavel.model import Responsavel
from app.cadastro_paciente.model import Paciente
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from .schemas import ResponsavelSchema
from app.cadastro_paciente.schemas import PacienteSchema
from app.utils.filters import filters 
from app.functions import cpf_check, email_check
from app.permissions_with_id import responsavel_paciente_jwt_required
from app.permissions import responsavel_required

class ResponsavelLista(MethodView): #/responsavel/lista
    decorators = [responsavel_required]
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=ResponsavelSchema, many=True) 
        return jsonify(schema.dump(Responsavel.query.all())), 200

class ResponsavelCreate(MethodView): #/responsavel
    def post(self):
        schema = ResponsavelSchema()
        responsavel = schema.load(request.json)

        if not email_check(responsavel.email) or not cpf_check(responsavel.cpf):
            return {'error': 'Usuário já cadastrado'} 

        responsavel.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[responsavel.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=responsavel.nome))

        mail.send(msg)

        return schema.dump(responsavel), 201

class ResponsavelDetails(MethodView): #/responsavel/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=ResponsavelSchema)
        responsavel = Responsavel.query.get_or_404(id)
        return schema.dump(responsavel), 200

    def put(self, id):
        responsavel = Responsavel.query.get_or_404(id)
        schema = ResponsavelSchema()
        responsavel = schema.load(request.json, instance = responsavel)

        responsavel.save()

        return schema.dump(responsavel)

    def patch(self, id):
        responsavel = Responsavel.query.get_or_404(id)
        schema = ResponsavelSchema()
        responsavel = schema.load(request.json, instance = responsavel, partial=True)

        responsavel.save()

        return schema.dump(responsavel)

    def delete(self,id): 
        responsavel = Responsavel.query.get_or_404(id)
        responsavel.delete(responsavel)

        return {}, 204

class ResponsavelConfirm(MethodView): #responsavel-confirm
    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        responsavel = Responsavel.query.get_or_404(data['identity'])

        if not responsavel.active:
            responsavel.active = True 
            responsavel.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        responsavel  = Responsavel.query.filter_by(email=dados['email']).first_or_404()

        if not responsavel: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[responsavel.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=responsavel.nome))
        
        mail.send(msg)

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset
    def patch(self, token):
        try: 
            responsavel = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        responsavel = Responsavel.query.get_or_404(responsavel['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        responsavel.password = data['password']
        responsavel.save()

        return {'msg': 'senha atualizada'}, 200


class ShowPacientes(MethodView): #/show/pacientes/<int:responsavel_id>
    decorators = [responsavel_paciente_jwt_required]
    def get(self,responsavel_id):
        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema)
        paciente = Paciente.query.get_or_404(responsavel_id)
        return schema.dump(paciente), 200