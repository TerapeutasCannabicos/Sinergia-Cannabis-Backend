from flask import Blueprint 
from app.cadastro_responsavel.controllers import (ResponsavelCurrent, ResponsavelCreate, ResponsavelDetails, ResponsavelConfirm, EmailPassword, ResetPassword) 

responsavel_api = Blueprint('responsavel_api', __name__)

responsavel_api.add_url_rule(
    '/responsavel/current', view_func=ResponsavelCurrent.as_view('reponsavel_current'), methods=['GET']
)

responsavel_api.add_url_rule(
    '/responsavel', view_func=ResponsavelCreate.as_view('reponsavel_create'), methods=['POST']
)

responsavel_api.add_url_rule(
    '/responsavel/<int:id>', view_func=ResponsavelDetails.as_view('responsavel_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

responsavel_api.add_url_rule(
    '/responsavel-confirm', view_func=ResponsavelConfirm.as_view('responsavel_confirm'), methods=['GET']
)

responsavel_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_password'), methods=['POST']
)

responsavel_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('reset_password'), methods=['PATCH']
)