from flask import Blueprint 
from app.cadastro_paciente.controllers import (PacienteLista, PacienteCreate, PacienteDetails)

paciente_api = Blueprint('paciente_api', __name__)

paciente_api.add_url_rule(
    '/paciente/lista', view_func=PacienteLista.as_view('paciente_lista'), methods=['GET']
)

paciente_api.add_url_rule(
    '/paciente', view_func=PacienteCreate.as_view('paciente_create'), methods=['POST']
)

paciente_api.add_url_rule(
    '/paciente/<int:id>', view_func=PacienteDetails.as_view('paciente_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

