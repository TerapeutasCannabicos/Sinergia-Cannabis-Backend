from flask.views import MethodView
from app.utils.filters import filters
from flask import request, jsonify
from app.cadastro_medico.schemas import MedicoSchema
from app.agendamento_atendimento.model import Agendamento
from app.agendamento_atendimento.schemas import AgendamentoSchema
from app.cadastro_patient.schemas import PatientSchema
from app.cadastro_patient.model import Patient
from app.cadastro_medico.model import Medico
from app.horario_disponivel.model import Horario
from app.horario_disponivel.schemas import HorarioSchema
import json
from app.permissions_with_id import responsavel_patient_adm_jwt_required, responsavel_patient_jwt_required
from app.permissions import administrador_required, responsavel_patient_required, responsavel_patient_adm_required
from datetime import datetime, timedelta
from app.utils.filters import Filter
from flask_jwt_extended import  get_jwt, verify_jwt_in_request
from app.model import BaseModel
'''
- Mudar login outros 
- Rota excluir permissão calendário e aceitar cadastro
- Adiconar disponível= False em agendar consulta 
- Rever consultalist
- Rever as rotas que tem que colocar permissão_calendário=True 
- Rever permissão adm
- Fazer rota aparecendo os horários dos médicos para as pessoas
- Rever rota details paciente e RegisterConfirm adm
-Rever get pacientes'''
class ListaMedico(MethodView): #/lista/medico/<medico_especialidade>
    decorators = [responsavel_patient_adm_required]

    def get(self, medico_especialidade):
        medico = Medico.query.filter_by(especialidade=medico_especialidade)
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema, many=True, only = ['nome', 'sobrenome', 'especialidade'])
        json_medico = jsonify(schema.dump(medico))
        json_medico = json_medico.json
        dicionario = {"medico": json_medico}

        return json.dumps(dicionario), 200
        
class EscolhaMedico(MethodView): #/escolha/medico/<int:medico_id>
    decorators = [responsavel_patient_adm_required]

    def get(self, medico_id):
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema, only = ['nome', 'sobrenome'])
        medico = Medico.query.get_or_404(medico_id)
        return schema.dump(medico), 200

class AcessoCalendario(MethodView):   #/acesso/calendario
    decorators = [administrador_required]
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=PatientSchema, many=True, only=['nome', 'sobrenome', 'cpf']) 
        return jsonify(schema.dump(Patient.query.all())), 200

class PermissaoCalendario(MethodView): #/permissao/calendario/<int:patient_id>
    decorators = [administrador_required]
    def patch(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        schema = PatientSchema()
        data = {'permissao_calendario':True}
        patient = schema.load(data, instance = patient, partial=True)

        patient.save()

        return schema.dump(patient)  

class AgendarConsulta(MethodView):    #/patient/agendar/<int:patient_id>/<int:medico_id>
    decorators = [responsavel_patient_adm_required]
    def post(self, patient_id, medico_id):
        patient = Patient.query.get_or_404(patient_id)
        if patient.permissao_calendario == True:
            return {'error':'permission denied'}
        else:
            ini_time_for_now = datetime.now()
            limit_date = ini_time_for_now + \
                timedelta(days = 60)
            schema = AgendamentoSchema()
            data = request.json
            data["patient_id"] = patient_id
            data["medico_id"] = medico_id
            datahora = data['date']
            hora = datetime.strptime(datahora, "%d/%m/%y-%H:%M:%S")
            horario = Horario.query.filter(Horario.date==hora, Horario.disponivel==False).first()
            if not horario: #if not hora==agenda or not horario.disponivel==True or agendamento.date > limit_date
                return {'error':'agendamento não disponivel'}, 400
            horario.disponivel=True
            id=horario.id
            data["horario_id"] = id
            horario.save()
            agendamento = schema.load(data)
            agendamento.save()
            return schema.dump(agendamento), 201

class ConsultaList(MethodView): #/consulta/lista/<int:responsavel_id>/<int:agendamento_id>
    decorators = [responsavel_patient_jwt_required]
    def get(self, agendamento_id, responsavel_id):
        schema = filters.getSchema(qs=request.args, schema_cls=AgendamentoSchema)
        agendamento = Agendamento.query.get_or_404(agendamento_id)
        return jsonify(schema.dump(agendamento)), 200

'''#Verificar horario 
class ConsultaDelete(MethodView):     #/consulta/delete/<int:patient_id>/<int:responsavel_id>/<int:agendamento_id>/<int:horario_id>
    decorators = [responsavel_patient_jwt_required]
    def delete(self, patient_id, agendamento_id, responsavel_id, horario_id):
        patient = Patient.query.get_or_404(patient_id)
        if patient.permissao_calendario == True:
            return {'permission denied'}
        else:
            agendamento = Agendamento.query.get_or_404(agendamento_id)
            agendamento.delete(agendamento)
            horario = Horario.query.filter_by(disponivel=True)

            return horario.disponivel==False, 204'''

#Para os casos em que não tem acesso ao calendário 
class ScheduleAdm(MethodView): #/schedule/Adm/create/<int:patient_id>/<int:medico_id>
    decorators = [administrador_required]
    def post(self, patient_id, medico_id):
        patient = Patient.query.get_or_404(patient_id)
        if patient.permissao_calendario == False:
            return {'error':'permission denied'}, 400
        else:
            ini_time_for_now = datetime.now()
            limit_date = ini_time_for_now + \
                timedelta(days = 60)
            schema = AgendamentoSchema()
            data = request.json
            data["patient_id"] = patient_id
            data["medico_id"] = medico_id
            datahora = data['date']
            hora = datetime.strptime(datahora, "%d/%m/%y-%H:%M:%S")
            horario = Horario.query.filter(Horario.date==hora, Horario.disponivel==False).first()
            if not horario: #if not hora==agenda or not horario.disponivel==True or agendamento.date > limit_date
                return {'error':'agendamento não disponivel'}, 400
            horario.disponivel=True
            id=horario.id
            data["horario_id"] = id
            horario.save()
            agendamento = schema.load(data)
            agendamento.save()
            agenda = agendamento #agenda = Agendamento.query.filter_by(active=False, patient_id=patient_id).first()
            agenda.active=True
            agenda.save()
            return schema.dump(agendamento), 201

class PatienteRequestSchedule(MethodView): #/request/schedule/<int:responsavel_id>/<int:patient_id>/<int:agendamento_id>
    decorators = [responsavel_patient_jwt_required]
    def patch(self, patient_id, agendamento_id, responsavel_id):
        patient = Patient.query.get_or_404(patient_id)
        #patient = Patient.query.filter(Patient.permissao_calendario==False).first()
        if patient.permissao_calendario==True:
            return {'error': 'Função não permitida'}, 400
        else:
            agendamento = Agendamento.query.get_or_404(agendamento_id)
            schema = AgendamentoSchema()
            data = {'active':True}
            agendamento = schema.load(data, instance = agendamento, partial=True)

            agendamento.save()

            return schema.dump(agendamento) 

class ScheduleRequestsList(MethodView): #/schedule/requests/list
    decorators = [administrador_required]
    def get(self):
        agendamento = Agendamento.query.filter_by(active=True)
        if agendamento: 
            schema = filters.getSchema(qs=request.args, schema_cls=AgendamentoSchema, many=True) 
            return jsonify(schema.dump(agendamento)), 200

class AdmChooseRequests(MethodView): #/adm/choose/requests/<int:agendamento_id>
    decorators = [administrador_required]
    def get(self, agendamento_id):
        agendamento = Agendamento.query.filter_by(active=True)
        if agendamento: 
            schema = filters.getSchema(qs=request.args, schema_cls=AgendamentoSchema)
            agendamento = Agendamento.query.get_or_404(agendamento_id)
            return schema.dump(agendamento), 200
        