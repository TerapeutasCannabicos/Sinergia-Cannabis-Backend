from app.extensions import db
import bcrypt
from app.model import BaseModel
from app.association import association_adm_outros

class Outros(BaseModel):
    __tablename__ = 'outros'
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(100), nullable=False)
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
    permissao_adm = db.Column(db.Boolean, default=False)
    nivel_permissao = db.Column(db.Integer, default=None)
    password_hash = db.Column(db.LargeBinary(128))

    patient = db.relationship('Patient', backref='outros_patient') 
    administrador = db.relationship('Administrador', secondary=association_adm_outros, backref='outros_adm')

    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)