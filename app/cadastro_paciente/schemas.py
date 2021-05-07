from app.extensions import ma 
from app.cadastro_paciente.model import Paciente
from marshmallow import ValidationError, validates

class PacienteSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Paciente
        load_instance=True
        ordered=True    
    
    id = ma.Integer(dump_only=True)
    nome = ma.String(required=True)
    sobrenome = ma.String(required=True)
    email = ma.Email(required=True)
    data_nascimento = ma.Date()
    cpf = ma.String(required=True)
    rg = ma.String(required=True)
    documentos_pessoais = ma.String(required=True) #colocar envio de arquivos
    diagnóstico = ma.String(required=True)   #colocar envio de arquivos
    laudo_médico = ma.String(required=True) #colocar envio de arquivos
    receita_médica = ma.String(required=True) #colocar envio de arquivos
    endereço = ma.String(required=True)
    bairro = ma.String(required=True)
    numero = ma.Integer(required=True)
    complemento = ma.String(required=True)
    cidade = ma.String(required=True)
    estado = ma.String(required=True)
    password = ma.String(load_only=True, required=True)


    @validates('name')
    def validate_name(self, name): 
        if name == '': 
            raise ValidationError('Invalid Name')