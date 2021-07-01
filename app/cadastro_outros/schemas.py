from app.extensions import ma 
from app.cadastro_outros.model import Outros
from marshmallow import ValidationError, validates
from app.permissao_outros.schemas import PermissaoSchema

class OutrosSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Outros
        load_instance=True
        ordered=True
    
    id = ma.Integer(dump_only=True)
    cargo = ma.String(required=True)
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
    confirmacao_cadastro = ma.Boolean(dump_only=True)
    password = ma.String(load_only=True, required=True)

    paciente = ma.Nested('PacienteSchema', many=True, dump_only=True)
    administrador = ma.Nested('AdministradorSchema', many=True, dump_only=True)
    permissao = ma.Nested(PermissaoSchema, many=True, dump_only=True)

    @validates('nome')
    def validate_nome(self, nome): 
        if nome == '': 
            raise ValidationError('Nome invalido')