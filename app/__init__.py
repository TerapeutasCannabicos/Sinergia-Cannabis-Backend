from flask import Flask 
from app.config import Config
from app.extensions import db, migrate, mail, jwt, ma, cors
from flask import current_app

from app.cadastro_responsavel.routes import responsavel_api
from app.cadastro_patient.routes import patient_api
from app.cadastro_medico.routes import medico_api
from app.cadastro_administrador.routes import administrador_api
from app.cadastro_lawyer.routes import lawyer_api
from app.cadastro_gestor.routes import gestor_api
from app.cadastro_outros.routes import outros_api
from app.storage.routes import storage_api
from app.login.routes import login_api
from app.patient_folder.routes import patient_folder_api
from app.agendamento_atendimento.routes import agendamento_api
from app.horario_disponivel.routes import horario_api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    #cors.init_app(app, resources={r"/*":{"origins":"*"}})
    cors.init_app(app)

    app.register_blueprint(responsavel_api)
    app.register_blueprint(patient_api)
    app.register_blueprint(medico_api)
    app.register_blueprint(administrador_api)
    app.register_blueprint(lawyer_api)
    app.register_blueprint(gestor_api)
    app.register_blueprint(outros_api)
    app.register_blueprint(storage_api)
    app.register_blueprint(login_api)
    app.register_blueprint(patient_folder_api)
    app.register_blueprint(agendamento_api)
    app.register_blueprint(horario_api)

    @property
    def algorithm(self):
        return current_app.config["JWT_ALGORITHM"]

    def decode_algorithms(self):
        algorithms = current_app.config["JWT_DECODE_ALGORITHMS"]
        if not algorithms:
            return [self.algorithm]
        if self.algorithm not in algorithms:
            algorithms.append(self.algorithm)
        return algorithms

    def test_default_configs(app):
        with app.test_request_context():
            assert algorithm == "HS256"
            assert decode_algorithms == ["HS256"]
            

    return app