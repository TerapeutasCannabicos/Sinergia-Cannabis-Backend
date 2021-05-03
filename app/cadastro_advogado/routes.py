from flask import Blueprint 
from app.cadastro_advogado.controllers import (AdvogadoCurrent, AdvogadoCreate, AdvogadoDetails, ChangePassword) 

advogado_api = Blueprint('advogado_api', __name__)

advogado_api.add_url_rule(
    '/advogado/current', view_func=AdvogadoCurrent.as_view('advogado_current'), methods=['GET']
)

advogado_api.add_url_rule(
    '/advogado', view_func=AdvogadoCreate.as_view('advogado_create'), methods=['GET', 'POST']
)

advogado_api.add_url_rule(
    '/advogado/<int:id>', view_func=AdvogadoDetails.as_view('advogado_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

advogado_api.add_url_rule(
    '/pw-change', view_func=ChangePassword.as_view('password_change'), methods=['POST']
)