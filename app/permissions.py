from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.cadastro_gestor.model import Gestor
from app.cadastro_administrador.model import Administrador
from app.cadastro_medico.model import Medico
from app.cadastro_paciente.model import Paciente
from app.cadastro_advogado.model import Advogado
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
            if check:
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
            if check:
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
            if check:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def paciente_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('paciente_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Paciente.query.get_or_404(get_jwt_identity())
            if check:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

def advogado_jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('advogado_id') != get_jwt_identity():
            return {'error': 'Unauthorized user'}, 401
        else:
            check = Advogado.query.get_or_404(get_jwt_identity())
            if check:
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
            if check:
                return func(*args, **kwargs)

            return func(*args, **kwargs)
    return wrapper

#cirar decorator para tipo de usuários, dentro da tabela outros -> permissão outros ver se o usuário acessa 
#create_access_token(identity=[user.id, user.email])