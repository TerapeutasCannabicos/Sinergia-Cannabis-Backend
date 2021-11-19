from flask import Blueprint 
from app.agendamento_atendimento.controllers import (ListaMedico, EscolhaMedico, AcessoCalendario, PermissaoCalendario, AgendarConsulta,ConsultaList, ScheduleAdm, ScheduleRequestsList, PatienteRequestSchedule, AdmChooseRequests) 

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
    '/permissao/calendario/<int:patient_id>', view_func=PermissaoCalendario.as_view('permissao_calendario'), methods=['PATCH']
)

agendamento_api.add_url_rule(
    '/patient/agendar/<int:patient_id>/<int:medico_id>', view_func=AgendarConsulta.as_view('agendar_consulta'), methods=['POST']
)

agendamento_api.add_url_rule(
    '/consulta/lista/<int:responsavel_id>/<int:agendamento_id>', view_func=ConsultaList.as_view('consulta_lista'), methods=['GET']
)

'''agendamento_api.add_url_rule(
    '/consulta/delete/<int:patient_id>/<int:responsavel_id>/<int:agendamento_id>/<int:horario_id>', view_func=ConsultaDelete.as_view('consulta_delete'), methods=['DELETE']
)'''

agendamento_api.add_url_rule(
    '/schedule/Adm/create/<int:patient_id>/<int:medico_id>', view_func=ScheduleAdm.as_view('schedule_adm'), methods=['POST']
)

agendamento_api.add_url_rule(
    '/schedule/requests/list', view_func=ScheduleRequestsList.as_view('schedule_requests_list'), methods=['GET']
)

agendamento_api.add_url_rule(
    '/request/schedule/<int:responsavel_id>/<int:patient_id>/<int:agendamento_id>', view_func=PatienteRequestSchedule.as_view('patient_request_schedule'), methods=['PATCH']
)

agendamento_api.add_url_rule(
    '/adm/choose/requests/<int:agendamento_id>', view_func=AdmChooseRequests.as_view('adm_choose_requests'), methods=['GET']
)