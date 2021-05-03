from app.extensions import ma 
from app.cadastro_gestor.model import Gestor

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
    password = ma.String(load_only=True, required=True)