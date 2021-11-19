  
from flask.views import MethodView
from datetime import timedelta
from app.login.schemas import LoginSchema
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from app.cadastro_administrador.model import Administrador
from app.cadastro_lawyer.model import Lawyer
from app.cadastro_gestor.model import Gestor
from app.cadastro_medico.model import Medico
from app.cadastro_outros.model import Outros
from app.cadastro_responsavel.model import Responsavel
from app.login.schemas import LoginSchema
from app.extensions import db 
from app.cadastro_outros.controllers import PermissaoAdm

'''
Não esquecer!
 and lawyer.confirmacao_cadastro==True
 and gestor.confirmacao_cadastro==True
 and medico.confirmacao_cadastro==True
 and outros.confirmacao_cadastro==True
 and patient.confirmacao_cadastro==True
 and responsavel.confirmacao_cadastro==True
'''

class UserLogin(MethodView):  #/login

    def post(self): 
        schema = LoginSchema()
        dados = schema.load(request.json)

        administrador = Administrador.query.filter_by(email=dados['email']).first()
        if administrador and administrador.verify_password(dados['password']): 
            token = create_access_token(identity=administrador.id, expires_delta=timedelta(minutes=900), fresh=True, additional_claims={"is_administrador": True})
            refresh_token = create_refresh_token(identity=administrador.id, expires_delta=timedelta(minutes=1500))
            return {'user': 'administrador',
                    'id': administrador.id,
                    'token': token,
                    'refresh_token': refresh_token}, 200
        else: 
            lawyer = Lawyer.query.filter_by(email=dados['email']).first()
            if lawyer and lawyer.verify_password(dados['password']):
                token = create_access_token(identity=lawyer.id, expires_delta=timedelta(minutes=900), fresh=True, additional_claims={"is_lawyer": True})
                refresh_token = create_refresh_token(identity=lawyer.id, expires_delta=timedelta(minutes=1500))
                return {'user': 'lawyer',
                        'id': lawyer.id,
                        'token': token,
                        'refresh_token': refresh_token}, 200
            else:
                gestor = Gestor.query.filter_by(email=dados['email']).first()
                if gestor and gestor.verify_password(dados['password']): 
                    token = create_access_token(identity=gestor.id, expires_delta=timedelta(minutes=900), fresh=True, additional_claims={"is_gestor": True})
                    refresh_token = create_refresh_token(identity=gestor.id, expires_delta=timedelta(minutes=1500))
                    return {'user': 'gestor',
                            'id': gestor.id,
                            'token': token,
                            'refresh_token': refresh_token}, 200
                else:
                    medico = Medico.query.filter_by(email=dados['email']).first()
                    if medico and medico.verify_password(dados['password']):
                        token = create_access_token(identity=medico.id, expires_delta=timedelta(minutes=900), fresh=True, additional_claims={"is_medico": True})
                        refresh_token = create_refresh_token(identity=medico.id, expires_delta=timedelta(minutes=1500))
                        return {'user': 'medico',
                                'id': medico.id,
                                'token': token,
                                'refresh_token': refresh_token}, 200
                    else:
                        outros = Outros.query.filter_by(email=dados['email']).first()
                        if outros and outros.verify_password(dados['password']):
                            token = create_access_token(identity=outros.id, expires_delta=timedelta(minutes=900), fresh=True)
                            refresh_token = create_refresh_token(identity=outros.id, expires_delta=timedelta(minutes=1500))
                            return {'user': 'outros',
                                    'id': outros.id,
                                    'token': token,
                                    'refresh_token': refresh_token}, 200
                        else:
                            responsavel = Responsavel.query.filter_by(email=dados['email']).first()
                            if responsavel and responsavel.verify_password(dados['password']):
                                token = create_access_token(identity=responsavel.id, expires_delta=timedelta(minutes=900), fresh=True, additional_claims={"is_responsavel": True})
                                refresh_token = create_refresh_token(identity=responsavel.id, expires_delta=timedelta(minutes=1500)) 
                                return  {'user': 'responsavel',
                                         'id': responsavel.id,
                                        'token': token,
                                        'refresh_token': refresh_token}, 200                                 
                            else: 
                                return {'error': 'email ou senha inválidos'}, 401
                                
            