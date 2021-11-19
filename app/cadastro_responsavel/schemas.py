from app.extensions import ma 
from app.cadastro_responsavel.model import Responsavel
from marshmallow import ValidationError, validates

class ResponsavelSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Responsavel
        load_instance=True
        ordered=True   
    
    id = ma.Integer(dump_only=True)
    nome = ma.String(required=True)
    sobrenome = ma.String(required=True)
    email = ma.Email(required=True)
    cpf = ma.String()
    rg = ma.String()
    celular = ma.String(required=True)
    telefone_secundario = ma.String()
    endereco = ma.String()
    bairro = ma.String()
    numero = ma.String()
    complemento = ma.String()
    cidade = ma.String()
    estado = ma.String()
    cep = ma.String() 
    confirmacao_cadastro = ma.Boolean(dump_only=True)
    password = ma.String(load_only=True, required=True)

    patient = ma.Nested('PatientSchema', many=True, dump_only=True)

    @validates('nome')
    def validate_nome(self, nome): 
        if nome == '': 
            raise ValidationError('Nome invalido')