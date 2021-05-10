  
from flask.views import MethodView
from datetime import timedelta
from app.login.schemas import LoginSchema
from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from app.cadastro_administrador.model import Administrador
from app.cadastro_advogado.model import Advogado
from app.cadastro_gestor.model import Gestor
from app.cadastro_medico.model import Medico
from app.cadastro_outros.model import Outros
from app.cadastro_paciente.model import Paciente
from app.cadastro_responsavel.model import Responsavel
from app.login.schemas import LoginSchema
from app.extensions import db 


class UserLogin(MethodView):  #/login

    def post(self): 

        dados = LoginSchema().load(request.json)
        administrador = Administrador.query.filter_by(email=dados['email']).first()
        advogado = Advogado.query.filter_by(email=dados['email']).first()
        gestor = Gestor.query.filter_by(email=dados['email']).first()
        medico = Medico.query.filter_by(email=dados['email']).first()
        outros = Outros.query.filter_by(email=dados['email']).first()
        paciente = Paciente.query.filter_by(email=dados['email']).first()
        responsavel = Responsavel.query.filter_by(email=dados['email']).first()

        if not administrador or not administrador.verify_password(dados['password']): 
            return {'error': 'email ou password incorretos'}, 401
        if not advogado or not advogado.verify_password(dados['password']): 
            return {'error': 'email ou password incorretos'}, 401
        if not medico or not medico.verify_password(dados['password']): 
            return {'error': 'email ou password incorretos'}, 401
        if not outros or not outros.verify_password(dados['password']): 
            return {'error': 'email ou password incorretos'}, 401
        if not paciente or not paciente.verify_password(dados['password']): 
            return {'error': 'email ou password incorretos'}, 401
        if not responsavel or not responsavel.verify_password(dados['password']): 
            return {'error': 'email ou password incorretos'}, 401

        token = create_access_token(identity=administrador.id, expires_delta=timedelta(minutes=900), fresh=True) 
        token = create_access_token(identity=advogado.id, expires_delta=timedelta(minutes=900), fresh=True)
        token = create_access_token(identity=gestor.id, expires_delta=timedelta(minutes=900), fresh=True)
        token = create_access_token(identity=medico.id, expires_delta=timedelta(minutes=900), fresh=True)
        token = create_access_token(identity=outros.id, expires_delta=timedelta(minutes=900), fresh=True)
        token = create_access_token(identity=paciente.id, expires_delta=timedelta(minutes=900), fresh=True)
        token = create_access_token(identity=responsavel.id, expires_delta=timedelta(minutes=900), fresh=True)

        refresh_token = create_refresh_token(identity=administrador.id, expires_delta=timedelta(minutes=1500))
        refresh_token = create_refresh_token(identity=advogado.id, expires_delta=timedelta(minutes=1500))
        refresh_token = create_refresh_token(identity=gestor.id, expires_delta=timedelta(minutes=1500))
        refresh_token = create_refresh_token(identity=medico.id, expires_delta=timedelta(minutes=1500))
        refresh_token = create_refresh_token(identity=outros.id, expires_delta=timedelta(minutes=1500))
        refresh_token = create_refresh_token(identity=paciente.id, expires_delta=timedelta(minutes=1500))
        refresh_token = create_refresh_token(identity=responsavel.id, expires_delta=timedelta(minutes=1500))

        return {'token': token}, 200 