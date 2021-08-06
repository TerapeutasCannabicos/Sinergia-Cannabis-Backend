from flask import Blueprint 
from app.cadastro_medico.controllers import (MedicoLista, MedicoCreate, MedicoDetails, MedicoConfirm, EmailPassword, ResetPassword) 

medico_api = Blueprint('medico_api', __name__)

medico_api.add_url_rule(
    '/medico/lista', view_func=MedicoLista.as_view('medico_lista'), methods=['GET']
)

medico_api.add_url_rule(
    '/medico', view_func=MedicoCreate.as_view('medico_create'), methods=['POST']
)

medico_api.add_url_rule(
    '/medico/<int:id>', view_func=MedicoDetails.as_view('medico_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

medico_api.add_url_rule(
    '/medico-confirm', view_func=MedicoConfirm.as_view('medico_confirm'), methods=['GET']
)

medico_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_password'), methods=['POST']
)

medico_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('reset_password'), methods=['PATCH']
)
