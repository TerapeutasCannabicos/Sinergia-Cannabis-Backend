from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_patient.model import Patient
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import decode_token
from .schemas import PatientSchema
from app.utils.filters import filters 
from app.permissions import responsavel_patient_required, responsavel_required
from app.permissions_with_id import responsavel_patient_jwt_required
from app.model import BaseModel
#Rever -> Só pode ver os pacientes dele
class PatientLista(MethodView): #/patient/lista
    decorators = [responsavel_patient_required]
    def get(self):

        schema = filters.getSchema(qs=request.args, schema_cls=PatientSchema, many=True) 
        return jsonify(schema.dump(Patient.query.all())), 200


class PatientCreate(MethodView): #/patient
    decorators = [responsavel_required]
    def post(self):
        schema = PatientSchema()
        patient = schema.load(request.json)

        patient.save()

        return schema.dump(patient), 201

class PatientDetails(MethodView): #/patient/<int:patient_id>/<int:responsavel_id>
    decorators = [responsavel_patient_jwt_required]
    def get(self,patient_id, responsavel_id):
        schema = filters.getSchema(qs=request.args, schema_cls=PatientSchema)
        patient = Patient.query.get_or_404(patient_id)
        return schema.dump(patient), 200

    def put(self, patient_id, responsavel_id):
        patient = Patient.query.get_or_404(patient_id)
        schema = PatientSchema()
        patient = schema.load(request.json, instance = patient)

        patient.save()

        return schema.dump(patient)

    def patch(self, patient_id, responsavel_id):
        patient = Patient.query.get_or_404(patient_id)
        schema = PatientSchema()
        patient = schema.load(request.json, instance = patient, partial=True)

        patient.save()

        return schema.dump(patient)

    def delete(self,patient_id, responsavel_id): 
        patient = Patient.query.get_or_404(patient_id)
        patient.delete(patient)

        return {}, 204