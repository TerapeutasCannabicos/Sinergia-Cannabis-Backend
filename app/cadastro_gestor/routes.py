from flask import Blueprint 
from app.cadastro_gestor.controllers import (GestorCurrent, GestorCreate, GestorDetails, ChangePassword) 

gestor_api = Blueprint('gestor_api', __name__)

gestor_api.add_url_rule(
    '/gestor/current', view_func=GestorCurrent.as_view('gestor_current'), methods=['GET']
)

gestor_api.add_url_rule(
    '/gestor', view_func=GestorCreate.as_view('gestor_create'), methods=['GET', 'POST']
)

gestor_api.add_url_rule(
    '/gestor/<int:id>', view_func=GestorDetails.as_view('gestor_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

gestor_api.add_url_rule(
    '/pw-change', view_func=ChangePassword.as_view('password_change'), methods=['POST']
)