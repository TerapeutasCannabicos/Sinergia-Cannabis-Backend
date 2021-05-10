from app.extensions import ma 
from app.cadastro_gestor.model import Gestor
from marshmallow import ValidationError, validates

class GestorSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Gestor
        load_instance=True
        ordered=True
    
    id = ma.Integer(dump_only=True)
    nome = ma.String(required=True)
    sobrenome = ma.String(required=True)
    email = ma.Email(required=True)
    cpf = ma.String(required=True)
    celular = ma.String(required=True)
    telefone_secundario = ma.String()
    endereço = ma.String(required=True)
    bairro = ma.String(required=True)
    numero = ma.Integer(required=True)
    complemento = ma.String(required=True)
    cidade = ma.String(required=True)
    estado = ma.String(required=True)
    cep = ma.String(required=True) 
    nome_associacao = ma.String(required=True)
    password = ma.String(load_only=True, required=True)

    paciente = ma.Nested('PacienteSchema', many=True, dump_only=True)
    administrador = ma.Nested('AdministradorSchema', many=True, dump_only=True)


    @validates('nome')
    def validate_nome(self, nome): 
        if nome == '': 
            raise ValidationError('Nome invalido')