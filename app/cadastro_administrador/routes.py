from flask import Blueprint 
from app.cadastro_administrador.controllers import (AdministradorCurrent, AdministradorCreate, AdministradorDetails, AdministradorConfirm, EmailPassword, ResetPassword) 

administrador_api = Blueprint('administrador_api', __name__)

administrador_api.add_url_rule(
    '/administrador/current', view_func=AdministradorCurrent.as_view('administrador_current'), methods=['GET']
)

administrador_api.add_url_rule(
    '/administrador', view_func=AdministradorCreate.as_view('administrador_create'), methods=['GET', 'POST']
)

administrador_api.add_url_rule(
    '/administrador/<int:id>', view_func=AdministradorDetails.as_view('administrador_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

administrador_api.add_url_rule(
    '/administrador-confirm', view_func=AdministradorConfirm.as_view('administrador_change'), methods=['POST']
)

administrador_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_change'), methods=['POST']
)

administrador_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('password_change'), methods=['POST']
)