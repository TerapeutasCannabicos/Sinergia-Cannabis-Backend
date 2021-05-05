from flask import Flask 
from app.config import Config
from app.extensions import db, migrate, mail, ma

from app.cadastro_responsavel.routes import responsavel_api
from app.cadastro_paciente.routes import paciente_api
from app.cadastro_medico.routes import medico_api
from app.cadastro_administrador.routes import administrador_api
from app.cadastro_advogado.routes import advogado_api
from app.cadastro_gestor.routes import gestor_api
from app.cadastro_outros.routes import outros_api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)

    app.register_blueprint(responsavel_api)
    app.register_blueprint(paciente_api)
    app.register_blueprint(medico_api)
    app.register_blueprint(administrador_api)
    app.register_blueprint(advogado_api)
    app.register_blueprint(gestor_api)
    app.register_blueprint(outros_api)

    return app