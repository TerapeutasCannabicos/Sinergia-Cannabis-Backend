from app.extensions import ma 
from app.cadastro_outros.model import Outros
from marshmallow import ValidationError, validates

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
    rg = ma.String(required=True)
    celular = ma.String(required=True)
    telefone_secundario = ma.String()
    endereço = ma.String(required=True)
    bairro = ma.String(required=True)
    numero = ma.Integer(required=True)
    complemento = ma.String(required=True)
    cidade = ma.String(required=True)
    estado = ma.String(required=True)
    cep = ma.String(required=True) 
    nome_associação = ma.String(required=True)
    password = ma.String(load_only=True, required=True)

    @validates('name')
    def validate_name(self, name): 
        if name == '': 
            raise ValidationError('Invalid Name')