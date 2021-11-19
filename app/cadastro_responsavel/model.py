from app.extensions import db 
import bcrypt
from app.model import BaseModel

class Responsavel(BaseModel):
    __tablename__ = 'responsavel'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    cpf = db.Column(db.String(30),unique=True)
    rg = db.Column(db.String(30),unique=True)
    celular = db.Column(db.String(20), nullable=True)
    telefone_secundario = db.Column(db.String(20), default=None)
    endereco = db.Column(db.String(500), nullable=True)
    bairro = db.Column(db.String(200), nullable=True)
    numero = db.Column(db.String(30), nullable=True)
    complemento = db.Column(db.String(50), nullable=True)
    cidade = db.Column(db.String(200), nullable=True)
    estado = db.Column(db.String(200), nullable=True)
    cep = db.Column(db.String(50), nullable=True)
    confirmacao_cadastro = db.Column(db.Boolean, default=True) 
    password_hash = db.Column(db.LargeBinary(128))  

    patient = db.relationship('Patient', backref='responsavel_patient')

    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)

    #sistema de adimin só o Responsável pode criar o cadastro do patient