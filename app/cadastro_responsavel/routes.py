from flask import Blueprint 
from app.cadastro_responsavel.controllers import (ResponsavelCurrent, ResponsavelCreate, ResponsavelDetails, ChangePassword) 

responsavel_api = Blueprint('responsavel_api', __name__)

responsavel_api.add_url_rule(
    '/responsavel/current', view_func=ResponsavelCurrent.as_view('reponsavel_current'), methods=['GET']
)

responsavel_api.add_url_rule(
    '/responsavel', view_func=ResponsavelCreate.as_view('reponsavel_create'), methods=['GET', 'POST']
)

responsavel_api.add_url_rule(
    '/responsavel/<int:id>', view_func=ResponsavelDetails.as_view('responsavel_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

responsavel_api.add_url_rule(
    '/pw-change', view_func=ChangePassword.as_view('password_change'), methods=['POST']
)