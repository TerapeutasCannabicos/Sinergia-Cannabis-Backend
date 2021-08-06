from flask import Blueprint 
from app.cadastro_advogado.controllers import (AdvogadoLista, AdvogadoCreate, AdvogadoDetails, AdvogadoConfirm, EmailPassword, ResetPassword) 

advogado_api = Blueprint('advogado_api', __name__)

advogado_api.add_url_rule(
    '/advogado/lista', view_func=AdvogadoLista.as_view('advogado_lista'), methods=['GET']
)

advogado_api.add_url_rule(
    '/advogado', view_func=AdvogadoCreate.as_view('advogado_create'), methods=['POST']
)

advogado_api.add_url_rule(
    '/advogado/<int:id>', view_func=AdvogadoDetails.as_view('advogado_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

advogado_api.add_url_rule(
    '/advogado-confirm', view_func=AdvogadoConfirm.as_view('advogado_confirm'), methods=['GET']
)

advogado_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_password'), methods=['POST']
)

advogado_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('reset_password'), methods=['PATCH']
)