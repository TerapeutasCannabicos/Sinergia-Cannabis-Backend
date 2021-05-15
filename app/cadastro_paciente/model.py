from app.extensions import db
import bcrypt
from app.model import BaseModel
from app.association import association_table2, association_table5
from app.storage.storage import storage

class Paciente(BaseModel):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    data_nascimento = db.Column(db.Date(), nullable=False) 
    cpf = db.Column(db.String(30),unique=True, nullable=False)
    rg = db.Column(db.String(30),unique=True, nullable=False)
    documentos_pessoais = db.Column(db.String(2000), nullable=False)
    diagnostico = db.Column(db.String(2000), nullable=False)
    laudo_medico = db.Column(db.String(2000), nullable=False)
    receita_medica = db.Column(db.String(2000), nullable=False)
    endereço = db.Column(db.String(500), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False) 
    confirmacao_cadastro = db.Column(db.Boolean, nullable=False)
    password_hash = db.Column(db.LargeBinary(128))

    responsavel_id = db.Column(db.Integer, db.ForeignKey('responsavel.id')) 
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id')) 
    outros_id = db.Column(db.Integer, db.ForeignKey('outros.id')) 
    administrador = db.relationship('Administrador', secondary=association_table2, backref='paciente2')
    gestor = db.relationship('Gestor', secondary=association_table5, backref='paciente5')
    advogado = db.relationship('Advogado', back_populates='paciente')

    @property
    def password(self):
        raise AttributeError('Password é somente para escrita')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password:str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)

#Documentos pessoais

    def delete_documentos_pessoais(self):
        if self.documentos_pessoais:
            storage.delete_object(file_key=self.documentos_pessoais)

    @property
    def documentos_pessoais_url(self) -> str:
        if self.documentos_pessoais:
            return storage.get_url(file_key=self.documentos_pessoais)
        return None

    @documentos_pessoais_url.setter
    def documentos_pessoais_url(self, documentos_pessoais_url):
        self.delete_documentos_pessoais()

        self.documentos_pessoais = documentos_pessoais_url

        return {}, 204

#Diagnóstico

    def delete_diagnostico(self):
        if self.diagnostico:
            storage.delete_object(file_key=self.diagnostico)

    @property
    def diagnostico_url(self) -> str:
        if self.diagnostico:
            return storage.get_url(file_key=self.diagnostico)
        return None

    @diagnostico_url.setter
    def diagnostico_url(self, diagnostico_url):
        self.delete_diagnostico()

        self.diagnostico = diagnostico_url

        return {}, 204

#Laudo médico

    def delete_laudo_medico(self):
        if self.laudo_medico:
            storage.delete_object(file_key=self.laudo_medico)

    @property
    def laudo_medico_url(self) -> str:
        if self.laudo_medico:
            return storage.get_url(file_key=self.laudo_medico)
        return None

    @laudo_medico_url.setter
    def laudo_medico_url(self, laudo_medico_url):
        self.delete_laudo_medico()

        self.laudo_medico = laudo_medico_url

        return {}, 204

#receita_medica

    def delete_receita_medica(self):
        if self.receita_medica:
            storage.delete_object(file_key=self.receita_medica)

    @property
    def receita_medica_url(self) -> str:
        if self.receita_medica:
            return storage.get_url(file_key=self.receita_medica)
        return None

    @receita_medica_url.setter
    def receita_medica_url(self, receita_medica_url):
        self.receita_medica_medico()

        self.receita_medica = receita_medica_url

        return {}, 204





