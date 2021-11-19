from flask.views import MethodView
from flask import request, jsonify
from app.cadastro_patient.model import Patient
from app.patient_folder.model import AnotacoesMedico
from app.cadastro_patient.schemas import PatientSchema
from app.patient_folder.schemas import AnotacoesMedicoSchema
from app.cadastro_medico.model import Medico
from app.cadastro_medico.schemas import MedicoSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.permissions_with_id import medico_jwt_required, lawyer_jwt_required 
from app.permissions import medico_required
import json
from app.model import BaseModel

class PatientFolderList(MethodView): #/patientfolder/medico/<int:medico_id>
    decorators = [medico_jwt_required]

    def get(self, medico_id):
        schema = filters.getSchema(qs=request.args, schema_cls=PatientSchema, many=True)
        return jsonify(schema.dump(Patient.query.all())), 200

class AcessoLawyer(MethodView): #/patientfolder/lawyer/<int:lawyer_id>
    decorators = [lawyer_jwt_required]

    def get(self, lawyer_id):
        schema = filters.getSchema(qs=request.args, schema_cls=PatientSchema, many=True, rel=['receita_medica', 'laudo_medico']) 
        return jsonify(schema.dump(Patient.query.all())), 200

class AnotacoesMedicasLista(MethodView): #/anotacoesmedicas/lista
    decorators = [medico_required]
    def get(self, medico_id):
        schema = filters.getSchema(qs=request.args, schema_cls=AnotacoesMedicoSchema, many=True) 
        return jsonify(schema.dump(AnotacoesMedicoSchema.query.all())), 200

class AnotacoesMedicasCreate(MethodView): #/anotacoesmedicas/create/<int:medico_id>
    decorators = [medico_jwt_required]
    def post(self, medico_id):
        schema = AnotacoesMedicoSchema()
        data = request.json
        data["medico_id"] = medico_id
        anotacoesmedico = schema.load(data)
        anotacoesmedico.save()

        return schema.dump(anotacoesmedico), 201

class AnotacoesMedicasDetails(MethodView): #/anotacoesmedicas/details/<int:anotacoesmedico_id>/<int:medico_id>
    decorators = [medico_jwt_required]
    def get(self, medico_id, anotacoesmedico_id):
        schema = filters.getSchema(qs=request.args, schema_cls=AnotacoesMedicoSchema)
        anotacoesmedico = AnotacoesMedico.query.get_or_404(anotacoesmedico_id)
        return schema.dump(anotacoesmedico), 200

    def put(self, medico_id, anotacoesmedico_id):
        anotacoesmedico = AnotacoesMedico.query.get_or_404(anotacoesmedico_id)
        schema = AnotacoesMedicoSchema()
        anotacoesmedico = schema.load(request.json, instance = anotacoesmedico)

        anotacoesmedico.save()

        return schema.dump(anotacoesmedico)

    def patch(self, medico_id, anotacoesmedico_id):
        anotacoesmedico = AnotacoesMedico.query.get_or_404(anotacoesmedico_id)
        schema = AnotacoesMedicoSchema()
        anotacoesmedico = schema.load(request.json, instance = anotacoesmedico, partial=True)

        anotacoesmedico.save()

        return schema.dump(anotacoesmedico)

    def delete(self, medico_id, anotacoesmedico_id): 
        anotacoesmedico = AnotacoesMedico.query.get_or_404(anotacoesmedico_id)
        anotacoesmedico.delete(anotacoesmedico)

        return {}, 204