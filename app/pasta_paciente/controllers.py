from flask.views import MethodView
from flask import request, jsonify
from app.cadastro_paciente.model import Paciente
from app.pasta_paciente.model import AnotacoesMedico
from app.cadastro_paciente.schemas import PacienteSchema
from app.pasta_paciente.schemas import AnotacoesMedicoSchema
from app.cadastro_medico.model import Medico
from app.cadastro_medico.schemas import MedicoSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.permissions import medico_jwt_required, advogado_jwt_required 

class PastaPacienteList(MethodView): #/pastapaciente/medico/<int:medico_id>
    decorators = [medico_jwt_required]

    def get(self, medico_id):
        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema, many=True)
        return jsonify(schema.dump(Paciente.query.all())), 200

class AcessoAdvogado(MethodView): #/pastapaciente/advogado/<int:advogado_id>
    decorators = [advogado_jwt_required]

    def get(self, advogado_id):
        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema, many=True, rel=['receita_medica', 'laudo_medico']) 
        return jsonify(schema.dump(Paciente.query.all())), 200
        #exclude=[]

class AnotacoesMedicasCurrent(MethodView): #/anotacoesmedicas/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=AnotacoesMedicoSchema, many=True) 
        return jsonify(schema.dump(AnotacoesMedico.query.all())), 200


class AnotacoesMedicasCreate(MethodView): #/anotacoesmedicas/create
    def post(self):
        schema = AnotacoesMedicoSchema()
        anotacoesmedico = schema.load(request.json)

        anotacoesmedico.save()

        return schema.dump(anotacoesmedico), 201

class AnotacoesMedicasDetails(MethodView): #/anotacoesmedicas/details
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=AnotacoesMedicoSchema)
        anotacoesmedico = AnotacoesMedico.query.get_or_404(id)
        return schema.dump(anotacoesmedico), 200

    def put(self, id):
        anotacoesmedico = AnotacoesMedico.query.get_or_404(id)
        schema = AnotacoesMedicoSchema()
        anotacoesmedico = schema.load(request.json, instance = anotacoesmedico)

        anotacoesmedico.save()

        return schema.dump(anotacoesmedico)

    def patch(self, id):
        anotacoesmedico = AnotacoesMedico.query.get_or_404(id)
        schema = AnotacoesMedicoSchema()
        anotacoesmedico = schema.load(request.json, instance = anotacoesmedico, partial=True)

        anotacoesmedico.save()

        return schema.dump(anotacoesmedico)

    def delete(self,id): 
        anotacoesmedico = AnotacoesMedico.query.get_or_404(id)
        anotacoesmedico.delete(anotacoesmedico)

        return {}, 204