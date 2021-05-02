from flask import Blueprint 
from app.cadastro_medico.controllers import (MedicoCurrent, MedicoCreate, MedicoDetails, ChangePassword) 
#Change Password

medico_api = Blueprint('medico_api', __name__)

medico_api.add_url_rule(
    '/medico/current', view_func=MedicoCurrent.as_view('medico_current'), methods=['GET']
)

medico_api.add_url_rule(
    '/medico', view_func=MedicoCreate.as_view('medico_create'), methods=['GET', 'POST']
)

medico_api.add_url_rule(
    '/medico/<int:id>', view_func=MedicoDetails.as_view('medico_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

medico_api.add_url_rule(
    '/pw-change', view_func=ChangePassword.as_view('password_change'), methods=['POST']
)
