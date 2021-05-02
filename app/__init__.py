from flask import Flask 
from app.config import Config
from app.extensions import db, migrate, mail, ma

from app.cadastro_responsavel.routes import responsavel_api
from app.cadastro_paciente.routes import paciente_api
from app.cadastro_medico.routes import medico_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)

    app.register_blueprint(responsavel_api)
    app.register_blueprint(paciente_api)
    app.register_blueprint(medico_api)

    return app