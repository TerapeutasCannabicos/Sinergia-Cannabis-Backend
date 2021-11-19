from flask import Blueprint 
from app.cadastro_patient.controllers import (PatientLista, PatientCreate, PatientDetails)

patient_api = Blueprint('patient_api', __name__)

patient_api.add_url_rule(
    '/patient/lista', view_func=PatientLista.as_view('patient_lista'), methods=['GET']
)

patient_api.add_url_rule(
    '/patient', view_func=PatientCreate.as_view('patient_create'), methods=['POST']
)

patient_api.add_url_rule(
    '/patient/<int:patient_id>/<int:responsavel_id>', view_func=PatientDetails.as_view('patient_details'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

