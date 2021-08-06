from flask.views import MethodView
from app.utils.filters import filters
from flask import request, jsonify
from app.cadastro_medico.schemas import MedicoSchema
from app.agendamento_atendimento.model import Agendamento
from app.agendamento_atendimento.schemas import AgendamentoSchema
from app.cadastro_paciente.schemas import PacienteSchema
from app.cadastro_paciente.model import Paciente
from app.cadastro_medico.model import Medico
import json
from app.permissions import administrador_required, responsavel_paciente_required
from datetime import datetime
from app.utils.filters import Filter
from flask_jwt_extended import  get_jwt, verify_jwt_in_request

class ListaMedico(MethodView): #/lista/medico/<medico_especialidade>
    decorators = [responsavel_paciente_required]

    def get(self, medico_especialidade):
        medico = Medico.query.filter_by(especialidade=medico_especialidade)
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema, many=True, only = ['nome', 'sobrenome', 'especialidade'])
        json_medico = jsonify(schema.dump(medico))
        json_medico = json_medico.json
        dicionario = {"medico": json_medico}

        return json.dumps(dicionario), 200
        
class EscolhaMedico(MethodView): #/escolha/medico/<int:medico_id>
    decorators = [responsavel_paciente_required]

    def get(self, medico_id):
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema, only = ['nome', 'sobrenome'])
        medico = Medico.query.get_or_404(medico_id)
        return schema.dump(medico), 200

class AcessoCalendario(MethodView):   #/acesso/calendario
    #decorators = [administrador_required]

    def get(self):

        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema, many=True, only=['nome', 'sobrenome', 'cpf']) 
        return jsonify(schema.dump(Paciente.query.all())), 200

class PermissaoCalendario(MethodView): #/permissao/calendario/<int:paciente_id>
    #decorators = [administrador_required]
        def patch(self, paciente_id):
            paciente = Paciente.query.get_or_404(paciente_id)
            schema = PacienteSchema()
            data = {'permissao_calendario':True}
            paciente = schema.load(data, instance = paciente, partial=True)

            paciente.save()

            return schema.dump(paciente)   

class AgendarConsulta(MethodView):    #/paciente/agendar/<int:paciente_id>
    decorators = [responsavel_paciente_required]
    def post(self, paciente_id):
        schema = AgendamentoSchema()
        data = request.json
        data["paciente_id"] = paciente_id
        agendamento = schema.load(data)
        agendamento.save()

        return schema.dump(agendamento), 201

class ConsultaList(MethodView): #/consulta/lista/<int:paciente_id>
    def get(self, paciente_id):
        agendamento = Agendamento.query.filter_by(paciente_id)
        schema = filters.getSchema(qs=request.args, schema_cls=AgendamentoSchema, many=True)
        json_agendamento = jsonify(schema.dump(agendamento))
        json_agendamento = json_agendamento.json
        dicionario = {"agendamento": json_agendamento}

        return json.dumps(dicionario), 200
        #retornar False

class ConsultaDetails(MethodView):          #/consulta/details/<int:paciente_id>/<int:agendamento_id>
    if Paciente.permissao_calendario == True:
        decorators = [responsavel_paciente_required]
        def get(self, paciente_id, agendamento_id):
            schema = filters.getSchema(qs=request.args, schema_cls=AgendamentoSchema)
            agendamento = Agendamento.query.get_or_404(agendamento_id)
            return schema.dump(agendamento), 200

        def patch(self, agendamento_id):
            agendamento = Agendamento.query.get_or_404(agendamento_id)
            schema = AgendamentoSchema()
            agendamento = schema.load(request.json, instance = agendamento, partial=True)

            agendamento.save()

            return schema.dump(agendamento)

        def delete(self, agendamento_id): 
            agendamento = Agendamento.query.get_or_404(agendamento_id)
            agendamento.delete(agendamento)

            return agendamento.disponivel==True, 204


    



