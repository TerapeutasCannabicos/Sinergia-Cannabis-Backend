from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_administrador.model import Administrador
from app.cadastro_advogado.model import Advogado
from app.cadastro_gestor.model import Gestor
from app.cadastro_medico.model import Medico
from app.cadastro_outros.model import Outros
from app.cadastro_paciente.model import Paciente
from app.cadastro_responsavel.model import Responsavel
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from app.cadastro_administrador.schemas import AdministradorSchema
from app.cadastro_advogado.schemas import AdvogadoSchema
from app.cadastro_gestor.schemas import GestorSchema
from app.cadastro_medico.schemas import MedicoSchema
from app.cadastro_outros.schemas import OutrosSchema
from app.cadastro_paciente.schemas import PacienteSchema
from app.cadastro_responsavel.schemas import ResponsavelSchema
from app.utils.filters import filters
from app.functions import cpf_check, email_check
import json
from app.permissions_with_id import administrador_jwt_required
from app.permissions import administrador_required

class AdministradorLista(MethodView): #/administrador/lista
    decorators = [administrador_required]
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=AdministradorSchema, many=True) 
        return jsonify(schema.dump(Administrador.query.all())), 200


class AdministradorCreate(MethodView): #/administrador
    def post(self):
        schema = AdministradorSchema()
        administrador = schema.load(request.json)
        
        if not email_check(administrador.email) or not cpf_check(administrador.cpf):
            return {'error': 'Usuário já cadastrado'}

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

class RegisterConfirm(MethodView): #register-confirm/<int:id>
    decorators = [administrador_jwt_required]
    def get(self): 

        advogado = Advogado.query.filter_by(confirmacao_cadastro=False)
        schema = filters.getSchema(qs=request.args, schema_cls=AdvogadoSchema, many=True)
        json_advogado = jsonify(schema.dump(advogado))
        json_advogado = json_advogado.json
        dicionario = {"advogado": json_advogado}


        gestor = Gestor.query.filter_by(confirmacao_cadastro=False)
        schema = filters.getSchema(qs=request.args, schema_cls=GestorSchema, many=True)
        json_gestor = jsonify(schema.dump(gestor))
        json_gestor = json_gestor.json
        dicionario["gestor"] = json_gestor

        outros = Outros.query.filter_by(confirmacao_cadastro=False)
        schema = filters.getSchema(qs=request.args, schema_cls=OutrosSchema, many=True)
        json_outros = jsonify(schema.dump(outros))
        json_outros = json_outros.json
        dicionario["outros"] = json_outros

        medico = Medico.query.filter_by(confirmacao_cadastro=False)
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema, many=True)
        json_medico = jsonify(schema.dump(medico))
        json_medico = json_medico.json
        dicionario["medico"] = json_medico

        responsavel = Responsavel.query.filter_by(confirmacao_cadastro=False)
        schema = filters.getSchema(qs=request.args, schema_cls=ResponsavelSchema, many=True)
        json_responsavel = jsonify(schema.dump(responsavel))
        json_responsavel = json_responsavel.json
        dicionario["responsavel"] = json_responsavel

        return json.dumps(dicionario), 200
        

class RegisterAcceptAdvogado(MethodView): #register-accept-advogado/<int:administrador_id>/<int:id>
    decorators = [administrador_jwt_required]
    def patch(self, administrador_id, id):
        advogado = Advogado.query.get_or_404(id)
        schema = AdvogadoSchema()
        data = {'confirmacao_cadastro':True}
        advogado = schema.load(data, instance = advogado, partial=True)

        advogado.save()

        return schema.dump(advogado)

class RegisterAcceptGestor(MethodView): #register-accept-gestor/<int:administrador_id>/<int:id>
    decorators = [administrador_jwt_required]
    def patch(self, administrador_id, id):
        gestor = Gestor.query.get_or_404(id)
        schema = GestorSchema()
        data = {'confirmacao_cadastro':True}
        gestor = schema.load(data, instance = gestor, partial=True)

        gestor.save()

        return schema.dump(gestor)

class RegisterAcceptOutros(MethodView): #register-accept-outros/<int:administrador_id>/<int:id>
    decorators = [administrador_jwt_required]
    def patch(self, administrador_id, id):
        outros = Outros.query.get_or_404(id)
        schema = OutrosSchema()
        data = {'confirmacao_cadastro':True}
        outros = schema.load(data, instance = outros, partial=True)

        outros.save()

        return schema.dump(outros)

class RegisterAcceptMedico(MethodView): #register-accept-medico/<int:administrador_id>/<int:id>
    decorators = [administrador_jwt_required]
    def patch(self, administrador_id, id):
        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        data = {'confirmacao_cadastro':True}
        medico = schema.load(data, instance = medico, partial=True)

        medico.save()

        return schema.dump(medico)

class RegisterAcceptResponsavel(MethodView): #register-accept-responsavel/<int:administrador_id>/<int:id>
    decorators = [administrador_jwt_required]
    def patch(self, administrador_id, id):
        responsavel = Responsavel.query.get_or_404(id)
        schema = ResponsavelSchema()
        data = {'confirmacao_cadastro':True}
        responsavel = schema.load(data, instance = responsavel, partial=True)

        responsavel.save()

        return schema.dump(responsavel)

class ShowMedico(MethodView): #/show/medico
    decorators = [administrador_required] 
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema, many=True, only=['nome', 'cpf']) 
        return jsonify(schema.dump(Medico.query.all())), 200

class ShowMedicoPaciente(MethodView): #/show/medico/paciente/<int:medico_id>
    decorators = [administrador_required] 
    def get(self, medico_id):
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema, only=['nome', 'cpf', 'especialidade', 'paciente'])
        medico = Medico.query.get_or_404(medico_id)
        return schema.dump(medico), 200
