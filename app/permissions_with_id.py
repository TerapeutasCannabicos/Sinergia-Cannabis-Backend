from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt
from app.cadastro_gestor.model import Gestor
from app.cadastro_administrador.model import Administrador
from app.cadastro_medico.model import Medico
from app.cadastro_patient.model import Patient
from app.cadastro_lawyer.model import Lawyer
#from app.cadastro_outros.model import Outros
from app.cadastro_responsavel.model import Responsavel

from functools import wraps

def gestor_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('gestor_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Gestor.query.get_or_404(get_jwt_identity())
            claims = get_jwt()
            if check and claims["is_gestor"]:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def medico_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('medico_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Medico.query.get_or_404(get_jwt_identity())
            claims = get_jwt()
            if check and claims["is_medico"]:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def administrador_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('administrador_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Administrador.query.get_or_404(get_jwt_identity())
            claims = get_jwt()
            if check and claims["is_admnistrador"]:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def patient_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('patient_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Patient.query.get_or_404(get_jwt_identity())
            claims = get_jwt()
            if check and claims["is_patient"]:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def lawyer_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('lawyer_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Lawyer.query.get_or_404(get_jwt_identity())
            claims = get_jwt()
            if check and claims["is_lawyer"]:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def responsavel_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('responsavel_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Responsavel.query.get_or_404(get_jwt_identity())
            claims = get_jwt()
            if check and claims["is_responsavel"]:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def responsavel_patient_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('responsavel_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Responsavel.query.get_or_404(get_jwt_identity())
            patient = Patient.query.get_or_404(get_jwt_identity())
            if patient.responsavel_id == check.id:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def responsavel_patient_adm_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('responsavel_id') == get_jwt_identity() or kwargs.get('administrador_id') == get_jwt_identity():
            check = Responsavel.query.get_or_404(get_jwt_identity())
            check2 = Administrador.query.get_or_404(get_jwt_identity())
            if check or check2:
                return func(*args, **kwargs)
        else:
            return {'error': 'Unauthorized user'}, 401    
        return func(*args, **kwargs)
    return wrapper
