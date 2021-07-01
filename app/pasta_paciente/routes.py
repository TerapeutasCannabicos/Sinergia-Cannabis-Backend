from flask import Blueprint 
from app.pasta_paciente.controllers import (PastaPacienteList, AcessoAdvogado, AnotacoesMedicasCurrent, AnotacoesMedicasCreate, AnotacoesMedicasDetails) 

pasta_paciente_api = Blueprint('pasta_paciente_api', __name__)

pasta_paciente_api.add_url_rule(
    '/pastapaciente/medico/<int:medico_id>', view_func=PastaPacienteList.as_view('pastapaciente_medico'), methods=['GET']
)

pasta_paciente_api.add_url_rule(
    '/pastapaciente/advogado/<int:advogado_id>', view_func=AcessoAdvogado.as_view('pastapaciente_advogado'), methods=['GET']
)

pasta_paciente_api.add_url_rule(
    '/anotacoesmedicas/current', view_func=AnotacoesMedicasCurrent.as_view('anotacoesmedicas_current'), methods=['GET']
)

pasta_paciente_api.add_url_rule(
    '/anotacoesmedicas/create', view_func=AnotacoesMedicasCreate.as_view('anotacoesmedicas_create'), methods=['POST']
)

pasta_paciente_api.add_url_rule(
    '/anotacoesmedicas/details', view_func=AnotacoesMedicasDetails.as_view('anotacoesmedicas_details'), methods=['GET', 'PUT', 'PATCH', 'DELETE']
)


