from app.extensions import db 
import bcrypt
from app.model import BaseModel

class Responsavel(BaseModel):
    __tablename__ = 'responsavel'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    celular = db.Column(db.String(20), nullable=False)
    telefone_secundario = db.Column(db.String(20), default=None)
    endereço = db.Column(db.String(500), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False) 
    password_hash = db.Column(db.LargeBinary(128))  

    pacientes = db.relationship('Pacientes', backref='responsavel')  

    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)

    #sistema de adimin só o Responsável pode criar o cadastro do paciente