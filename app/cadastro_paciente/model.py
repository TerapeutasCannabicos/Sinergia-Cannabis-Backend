from app.extensions import db
import bcrypt
from app.model import BaseModel
from app.association import association_table2, association_table5

class Paciente(BaseModel):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    #data_nascimento = db.Column(db.Date(), nullable=False) #Coloco DateTime ou String??
    cpf = db.Column(db.String(30),unique=True, nullable=False) #Uso String ou Integer??
    rg = db.Column(db.String(30),unique=True, nullable=False)
    documentos_pessoais = db.Column(db.String(2000), nullable=False) #colocar envio de arquivos
    diagnóstico = db.Column(db.String(2000), nullable=False)   #colocar envio de arquivos
    laudo_médico = db.Column(db.String(2000), nullable=False) #colocar envio de arquivos
    receita_médica = db.Column(db.String(2000), nullable=False) #colocar envio de arquivos
    endereço = db.Column(db.String(500), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False) 
    password_hash = db.Column(db.LargeBinary(128))

    responsavel_id = db.Column(db.Integer, db.ForeignKey('responsavel.id')) 
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id')) 
    outros_id = db.Column(db.Integer, db.ForeignKey('outros.id')) 
    administrador = db.relationship('Administrador2', secondary=association_table2, backref='paciente')
    gestor = db.relationship('Gestor', secondary=association_table5, backref='paciente')


    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)

#Token
#sistema de adimin só o Responsável pode criar o cadastro do paciente

