from flask import Blueprint 
from app.agendamento_atendimento.controllers import (ListaMedico, EscolhaMedico, AcessoCalendario, PermissaoCalendario, AgendarConsulta,ConsultaList, ConsultaDetails) 

agendamento_api = Blueprint('agendamento_api', __name__)

agendamento_api.add_url_rule(
    '/lista/medico/<medico_especialidade>', view_func=ListaMedico.as_view('agendamento_medico'), methods=['GET']
)

agendamento_api.add_url_rule(
    '/escolha/medico/<int:medico_id>', view_func=EscolhaMedico.as_view('escolha_medico'), methods=['GET']
)

agendamento_api.add_url_rule(
    '/acesso/calendario', view_func=AcessoCalendario.as_view('acesso_calendario'), methods=['GET']
)

agendamento_api.add_url_rule(
    '/permissao/calendario/<int:paciente_id>', view_func=PermissaoCalendario.as_view('permissao_calendario'), methods=['PATCH']
)

agendamento_api.add_url_rule(
    '/paciente/agendar/<int:paciente_id>', view_func=AgendarConsulta.as_view('agendar_consulta'), methods=['POST']
)

agendamento_api.add_url_rule(
    '/consulta/lista/<int:paciente_id>', view_func=ConsultaList.as_view('consulta_lista'), methods=['GET']
)

agendamento_api.add_url_rule(
    '/consulta/details/<int:paciente_id>/<int:agendamento_id>', view_func=ConsultaDetails.as_view('consulta_details'), methods=['GET','PATCH', 'DELETE']
)