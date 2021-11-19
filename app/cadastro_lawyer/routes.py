from flask import Blueprint 
from app.cadastro_lawyer.controllers import (LawyerLista, LawyerCreate, LawyerDetails, LawyerConfirm, EmailPassword, ResetPassword) 

lawyer_api = Blueprint('lawyer_api', __name__)

lawyer_api.add_url_rule(
    '/lawyer/lista', view_func=LawyerLista.as_view('lawyer_lista'), methods=['GET']
)

lawyer_api.add_url_rule(
    '/lawyer', view_func=LawyerCreate.as_view('lawyer_create'), methods=['POST']
)

lawyer_api.add_url_rule(
    '/lawyer/<int:id>', view_func=LawyerDetails.as_view('lawyer_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

lawyer_api.add_url_rule(
    '/lawyer-confirm', view_func=LawyerConfirm.as_view('lawyer_confirm'), methods=['GET']
)

lawyer_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_password'), methods=['POST']
)

lawyer_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('reset_password'), methods=['PATCH']
)