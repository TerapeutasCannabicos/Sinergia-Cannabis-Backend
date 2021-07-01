from app.extensions import db
import bcrypt
from app.model import BaseModel
from app.association import association_adm_gestor, association_gestor_paciente

class Gestor(BaseModel):
    __tablename__ = 'gestor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    cpf = db.Column(db.String(30),unique=True, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    telefone_secundario = db.Column(db.String(20), default=None)
    endereco = db.Column(db.String(500), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False)
    cep = db.Column(db.String(50), nullable=False) 
    confirmacao_cadastro = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.LargeBinary(128))

    administrador = db.relationship('Administrador', secondary=association_adm_gestor, backref='gestor_adm')
    paciente = db.relationship('Paciente', secondary=association_gestor_paciente, backref='gestor_paciente')

    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)