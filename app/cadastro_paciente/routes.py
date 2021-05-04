from flask import Blueprint 
from app.cadastro_paciente.controllers import (PacienteCurrent, PacienteCreate, PacienteDetails, PacienteConfirm, EmailPassword, ResetPassword)

paciente_api = Blueprint('paciente_api', __name__)

paciente_api.add_url_rule(
    '/paciente/current', view_func=PacienteCurrent.as_view('paciente_current'), methods=['GET']
)

paciente_api.add_url_rule(
    '/paciente', view_func=PacienteCreate.as_view('paciente_create'), methods=['GET', 'POST']
)

paciente_api.add_url_rule(
    '/paciente/<int:id>', view_func=PacienteDetails.as_view('paciente_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

paciente_api.add_url_rule(
    '/paciente-confirm', view_func=PacienteConfirm.as_view('paciente_change'), methods=['POST']
)

paciente_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_change'), methods=['POST']
)

paciente_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('password_change'), methods=['POST']
)
