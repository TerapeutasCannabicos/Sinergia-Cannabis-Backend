  
from flask.views import MethodView
from datetime import timedelta
from app.login.schemas import LoginSchema
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from app.cadastro_administrador.model import Administrador
from app.cadastro_advogado.model import Advogado
from app.cadastro_gestor.model import Gestor
from app.cadastro_medico.model import Medico
from app.cadastro_outros.model import Outros
from app.cadastro_paciente.model import Paciente
from app.cadastro_responsavel.model import Responsavel
from app.cadastro_administrador.schemas import AdministradorSchema
from app.cadastro_advogado.schemas import AdvogadoSchema
from app.cadastro_gestor.schemas import GestorSchema
from app.cadastro_medico.schemas import MedicoSchema
from app.cadastro_outros.schemas import OutrosSchema
from app.cadastro_paciente.schemas import PacienteSchema
from app.cadastro_responsavel.schemas import ResponsavelSchema
from app.login.schemas import LoginSchema
from app.extensions import db 

'''
Não esquecer!
 and advogado.confirmacao_cadastro==True
 and gestor.confirmacao_cadastro==True
 and medico.confirmacao_cadastro==True
 and outros.confirmacao_cadastro==True
 and paciente.confirmacao_cadastro==True
 and responsavel.confirmacao_cadastro==True
'''

class UserLogin(MethodView):  #/login

    def post(self): 
        schema = LoginSchema()
        dados = schema.load(request.json)

        administrador = Administrador.query.filter_by(email=dados['email']).first()
        if administrador and administrador.verify_password(dados['password']): 
            token = create_access_token(identity=administrador.id, expires_delta=timedelta(minutes=900), fresh=True)
            refresh_token = create_refresh_token(identity=administrador.id, expires_delta=timedelta(minutes=1500))
            return {'user': 'administrador',
                    'token': token,
                    'refresh_token': refresh_token}, 200
        else: 
            advogado = Advogado.query.filter_by(email=dados['email']).first()
            if advogado and advogado.verify_password(dados['password']):
                token = create_access_token(identity=advogado.id, expires_delta=timedelta(minutes=900), fresh=True)
                refresh_token = create_refresh_token(identity=advogado.id, expires_delta=timedelta(minutes=1500))
                return {'user': 'advogado',
                        'token': token,
                        'refresh_token': refresh_token}, 200
            else:
                gestor = Gestor.query.filter_by(email=dados['email']).first()
                if gestor and gestor.verify_password(dados['password']): 
                    token = create_access_token(identity=gestor.id, expires_delta=timedelta(minutes=900), fresh=True)
                    refresh_token = create_refresh_token(identity=gestor.id, expires_delta=timedelta(minutes=1500))
                    return {'user': 'gestor',
                            'token': token,
                            'refresh_token': refresh_token}, 200
                else:
                    medico = Medico.query.filter_by(email=dados['email']).first()
                    if medico and medico.verify_password(dados['password']):
                        token = create_access_token(identity=medico.id, expires_delta=timedelta(minutes=900), fresh=True)
                        refresh_token = create_refresh_token(identity=medico.id, expires_delta=timedelta(minutes=1500))
                        return {'user': 'medico',
                                'token': token,
                                'refresh_token': refresh_token}, 200
                    else:
                        outros = Outros.query.filter_by(email=dados['email']).first()
                        if outros and outros.verify_password(dados['password']):
                            token = create_access_token(identity=outros.id, expires_delta=timedelta(minutes=900), fresh=True)
                            refresh_token = create_refresh_token(identity=outros.id, expires_delta=timedelta(minutes=1500))
                            return {'user': 'outros',
                                    'token': token,
                                    'refresh_token': refresh_token}, 200
                        else:
                            paciente = Paciente.query.filter_by(email=dados['email']).first()
                            if paciente and paciente.verify_password(dados['password']):
                                token = create_access_token(identity=paciente.id, expires_delta=timedelta(minutes=900), fresh=True)
                                refresh_token = create_refresh_token(identity=paciente.id, expires_delta=timedelta(minutes=1500))
                                return {'user': 'paciente',
                                        'token': token,
                                        'refresh_token': refresh_token}, 200
                            else:
                                responsavel = Responsavel.query.filter_by(email=dados['email']).first()
                                if responsavel and responsavel.verify_password(dados['password']):
                                    token = create_access_token(identity=responsavel.id, expires_delta=timedelta(minutes=900), fresh=True)
                                    refresh_token = create_refresh_token(identity=responsavel.id, expires_delta=timedelta(minutes=1500)) 
                                    return  {'user': 'responsavel',
                                             'token': token,
                                             'refresh_token': refresh_token}, 200                                 
                                else: 
                                    return {'error': 'email ou senha inválidos'}, 401
            