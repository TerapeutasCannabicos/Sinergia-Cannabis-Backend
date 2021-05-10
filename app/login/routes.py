from flask import Blueprint 
from app.login.controllers import (UserLogin)

login_api = Blueprint('login_api', __name__)

login_api.add_url_rule(
    '/login', view_func=UserLogin.as_view('usuario_login'), methods=['POST']  
)