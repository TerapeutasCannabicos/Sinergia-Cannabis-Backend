from app.extensions import db
import bcrypt
from app.model import BaseModel
from app.association import association_table3

class Medico(BaseModel):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.String(2000), default=True)
    Bio = db.Column(db.String(100), default=True)
    foto_perfil = db.Column(db.String(2000), default=True)   #colocar envio de arquivos
    email = db.Column(db.String(200), nullable=False, unique=True)
    facebook = db.Column(db.String(100), default=True)
    twitter = db.Column(db.String(100), default=True)
    instagram = db.Column(db.String(100), default=True)
    cpf = db.Column(db.String(30),unique=True, nullable=False)
    rg = db.Column(db.String(30),unique=True, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    telefone_secundario = db.Column(db.String(20), default=None)
    endereço = db.Column(db.String(500), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False)
    cep = db.Column(db.String(50), nullable=False) 
    password_hash = db.Column(db.LargeBinary(128))

    paciente = db.relationship('Paciente', backref='medico') 
    administrador = db.relationship('Administrador', secondary=association_table3, backref='medico3')

    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)

#foto_perfil

    def delete_foto_perfil(self):
        if self.foto_perfil:
            storage.delete_object(file_key=self.foto_perfil)

    @property
    def foto_perfil_url(self) -> str:
        if self.foto_perfil:
            return storage.get_url(file_key=self.foto_perfil)
        return None

    @foto_perfil_url.setter
    def foto_perfil_url(self, foto_perfil_url):
        self.delete_foto_perfil()

        self.foto_perfil = foto_perfil_url

        return {}, 204