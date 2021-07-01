from flask import Blueprint 
from app.cadastro_administrador.controllers import (AdministradorCurrent, AdministradorCreate, AdministradorDetails, AdministradorConfirm, EmailPassword, ResetPassword, RegisterConfirm, RegisterAcceptAdvogado, RegisterAcceptGestor, RegisterAcceptOutros, RegisterAcceptMedico, RegisterAcceptPaciente, RegisterAcceptResponsavel) 

administrador_api = Blueprint('administrador_api', __name__)

administrador_api.add_url_rule(
    '/administrador/current', view_func=AdministradorCurrent.as_view('administrador_current'), methods=['GET']
)

administrador_api.add_url_rule(
    '/administrador', view_func=AdministradorCreate.as_view('administrador_create'), methods=['POST']
)

administrador_api.add_url_rule(
    '/administrador/<int:id>', view_func=AdministradorDetails.as_view('administrador_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

administrador_api.add_url_rule(
    '/administrador-confirm', view_func=AdministradorConfirm.as_view('administrador_confirm'), methods=['GET']
)

administrador_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_password'), methods=['POST']
)

administrador_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('reset_password'), methods=['PATCH']
)

administrador_api.add_url_rule(
    '/register-confirm', view_func=RegisterConfirm.as_view('register_confirm'), methods=['GET']
)

administrador_api.add_url_rule(
    '/register-accept-advogado/<int:administrador_id>/<int:id>', view_func=RegisterAcceptAdvogado.as_view('register_accept_advogado'), methods=['PATCH']
)

administrador_api.add_url_rule(
    '/register-accept-gestor/<int:administrador_id>/<int:id>', view_func=RegisterAcceptGestor.as_view('register_accept_gestor'), methods=['PATCH']
)

administrador_api.add_url_rule(
    '/register-accept-outros/<int:administrador_id>/<int:id>', view_func=RegisterAcceptOutros.as_view('register_accept_outros'), methods=['PATCH']
)

administrador_api.add_url_rule(
    '/register-accept-medico/<int:administrador_id>/<int:id>', view_func=RegisterAcceptMedico.as_view('register_accept_medico'), methods=['PATCH']
)

administrador_api.add_url_rule(
    '/register-accept-paciente/<int:administrador_id>/<int:id>', view_func=RegisterAcceptPaciente.as_view('register_accept_paciente'), methods=['PATCH']
)

administrador_api.add_url_rule(
    '/register-accept-responsavel/<int:administrador_id>/<int:id>', view_func=RegisterAcceptResponsavel.as_view('register_accept_responsavel'), methods=['PATCH']
)