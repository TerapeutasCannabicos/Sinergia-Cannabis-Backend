from flask import Blueprint 
from app.cadastro_outros.controllers import (OutrosCurrent, OutrosCreate, OutrosDetails, OutrosConfirm, EmailPassword, ResetPassword) 

outros_api = Blueprint('outros_api', __name__)

outros_api.add_url_rule(
    '/outros/current', view_func=OutrosCurrent.as_view('outros_current'), methods=['GET']
)

outros_api.add_url_rule(
    '/outros', view_func=OutrosCreate.as_view('outros_create'), methods=['GET', 'POST']
)

outros_api.add_url_rule(
    '/outros/<int:id>', view_func=OutrosDetails.as_view('outros_detail'), methods=['GET', 'PUT', 'PATCH', 'DELETE']   
)

outros_api.add_url_rule(
    '/outros-confirm', view_func=OutrosConfirm.as_view('outros_change'), methods=['POST']
)

outros_api.add_url_rule(
    '/pw-email', view_func=EmailPassword.as_view('email_change'), methods=['POST']
)

outros_api.add_url_rule(
    '/pw-reset', view_func=ResetPassword.as_view('password_change'), methods=['POST']
)