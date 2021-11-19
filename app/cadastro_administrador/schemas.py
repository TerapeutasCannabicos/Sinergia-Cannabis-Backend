from app.extensions import ma 
from app.cadastro_administrador.model import Administrador
from marshmallow import ValidationError, validates


class AdministradorSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Administrador
        load_instance=True
        ordered=True
    
    id = ma.Integer(dump_only=True)
    nome = ma.String(required=True)
    sobrenome = ma.String(required=True)
    email = ma.Email(required=True)
    cpf = ma.String(required=True)
    celular = ma.String(required=True)
    telefone_secundario = ma.String()
    endereco = ma.String(required=True)
    bairro = ma.String(required=True)
    numero = ma.Integer(required=True)
    complemento = ma.String(required=True)
    cidade = ma.String(required=True)
    estado = ma.String(required=True)
    cep = ma.String(required=True)
    password = ma.String(load_only=True, required=True)

    gestor = ma.Nested('GestorSchema', many=True, dump_only=True)
    patient = ma.Nested('PatientSchema', many=True, dump_only=True)
    medico = ma.Nested('MedicoSchema', many=True, dump_only=True)
    outros = ma.Nested('OutrosSchema', many=True, dump_only=True)
    lawyer = ma.Nested('LawyerSchema', many=True, dump_only=True)

    @validates('nome')
    def validate_nome(self, nome): 
        if nome == '': 
            raise ValidationError('Nome invalido')