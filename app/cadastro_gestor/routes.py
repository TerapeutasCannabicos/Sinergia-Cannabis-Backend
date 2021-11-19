from flask import Blueprint 
from app.cadastro_gestor.controllers import (GestorLista, GestorCreate, GestorDetails, GestorConfirm, EmailPassword, ResetPassword) 

gestor_api = Blueprint('gestor_api', __name__)

gestor_api.add_url_rule(
    '/gestor/lista', view_func=GestorLista.as_view('gestor_lista'), methods=['GET']
)

gestor_api.add_url_rule(
    '/gestor', view_func=GestorCreate.as_view('gestor_create'), methods=['POST']
)

gestor_api.add_url_rule(
    '/gestor/<int:id>', view_func=GestorDetails.as_view('gestor_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

gestor_api.add_url_rule(
    '/gestor-confirm', view_func=GestorConfirm.as_view('gestor_confirm'), methods=['GET']
)

gestor_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_password'), methods=['POST']
)

gestor_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('reset_password'), methods=['PATCH']
)