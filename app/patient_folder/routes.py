from flask import Blueprint 
from app.patient_folder.controllers import (PatientFolderList, AcessoLawyer, AnotacoesMedicasLista, AnotacoesMedicasCreate, AnotacoesMedicasDetails) 

patient_folder_api = Blueprint('patient_folder_api', __name__)

patient_folder_api.add_url_rule(
    '/patientfolder/medico/<int:medico_id>', view_func=PatientFolderList.as_view('patientfolder_medico'), methods=['GET']
)

patient_folder_api.add_url_rule(
    '/patientfolder/lawyer/<int:lawyer_id>', view_func=AcessoLawyer.as_view('patientfolder_lawyer'), methods=['GET']
)

patient_folder_api.add_url_rule(
    '/anotacoesmedicas/lista/<int:medico_id>', view_func=AnotacoesMedicasLista.as_view('anotacoesmedicas_lista'), methods=['GET']
)

patient_folder_api.add_url_rule(
    '/anotacoesmedicas/create/<int:medico_id>', view_func=AnotacoesMedicasCreate.as_view('anotacoesmedicas_create'), methods=['POST']
)

patient_folder_api.add_url_rule(
    '/anotacoesmedicas/details/<int:medico_id>', view_func=AnotacoesMedicasDetails.as_view('anotacoesmedicas_details'), methods=['GET', 'PUT', 'PATCH', 'DELETE']
)


