from app.cadastro_administrador.model import Administrador
from app.cadastro_lawyer.model import Lawyer
from app.cadastro_gestor.model import Gestor
from app.cadastro_medico.model import Medico
from app.cadastro_outros.model import Outros
from app.cadastro_patient.model import Patient
from app.cadastro_responsavel.model import Responsavel
from functools import wraps
from flask import jsonify
from flask_jwt_extended import  get_jwt, verify_jwt_in_request, get_jwt_identity

def administrador_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        administrador = Administrador.query.get_or_404(get_jwt_identity())
        if not claim.get('is_administrador'):
            return {'msg': 'Unauthorized user'}, 401
        else:
            return func(*args, **kwargs)
    return wrapper


def lawyer_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        lawyer = Lawyer.query.get_or_404(get_jwt_identity())
        if not claim.get('is_lawyer'):
            return {'msg': 'Unauthorized user'}, 401
        else:
            return func(*args, **kwargs)
    return wrapper

def gestor_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        gestor = Gestor.query.get_or_404(get_jwt_identity())
        if not claim.get('is_gestor'):
            return {'msg': 'Unauthorized user'}, 401
        else:
            return func(*args, **kwargs)
    return wrapper

def medico_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        medico = Medico.query.get_or_404(get_jwt_identity())
        if not claim.get('is_medico'):
            return {'msg': 'Unauthorized user'}, 401
        else:
            return func(*args, **kwargs)
    return wrapper

def outros_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        outros = Outros.query.get_or_404(get_jwt_identity())
        if not claim.get('is_outros'):
            return {'msg': 'Unauthorized user'}, 401
        else:
            return func(*args, **kwargs)
    return wrapper

def patient_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        patient = Patient.query.get_or_404(get_jwt_identity())
        if not claim.get('is_patient'):
            return {'msg': 'Unauthorized user'}, 401
        else:
            return func(*args, **kwargs)
    return wrapper

def responsavel_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        responsavel = Responsavel.query.get_or_404(get_jwt_identity())
        if not claim.get('is_responsavel'):
            return {'msg': 'Unauthorized user'}, 401
        else:
            return func(*args, **kwargs)
    return wrapper


def responsavel_patient_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        responsavel = Responsavel.query.get_or_404(get_jwt_identity())
        patient = Patient.query.get_or_404(get_jwt_identity())
        if not claim.get('is_responsavel') and patient.responsavel_id == None:
            return {'msg': 'Unauthorized user'}, 401
        else:
            return func(*args, **kwargs)
    return wrapper

def responsavel_patient_adm_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim = get_jwt()
        if claim.get('is_responsavel') or claim.get('is_administrador'):
            return func(*args, **kwargs)
        else:
            return {'msg': 'Unauthorized user'}, 401
            
    return wrapper