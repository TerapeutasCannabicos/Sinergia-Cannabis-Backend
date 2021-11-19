from app.extensions import ma 
from app.cadastro_patient.model import Patient
from marshmallow import ValidationError, validates

class PatientSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Patient
        load_instance=True
        ordered=True    
    
    id = ma.Integer(dump_only=True)
    nome = ma.String(required=True)
    sobrenome = ma.String(required=True)
    data_nascimento = ma.String(required=True)
    cpf = ma.String(required=True)
    rg = ma.String(required=True)
    documentos_pessoais = ma.String(required=True) #colocar envio de arquivos
    diagnostico = ma.String(required=True)   #colocar envio de arquivos
    laudo_medico = ma.String(required=True) #colocar envio de arquivos
    receita_medica = ma.String(required=True) #colocar envio de arquivos
    endereco = ma.String(required=True)
    bairro = ma.String(required=True)
    numero = ma.Integer(required=True)
    complemento = ma.String(required=True)
    cidade = ma.String(required=True)
    estado = ma.String(required=True)
    cep = ma.String(required=True) 
    permissao_calendario = ma.Boolean(required=False)

    responsavel = ma.Nested('ResponsavelSchema', dump_only=True)
    gestor = ma.Nested('GestorSchema', many=True, dump_only=True)
    medico = ma.Nested('MedicoSchema', dump_only=True)
    outros = ma.Nested('OutrosSchema', dump_only=True)
    administrador = ma.Nested('AdministradorSchema', many=True, dump_only=True)
    lawyer = ma.Nested('LawyerSchema', dump_only=True)
    agendamento = ma.Nested('AgendamentoSchema', many=True, dump_only=True)

    @validates('nome')
    def validate_nome(self, nome): 
        if nome == '': 
            raise ValidationError('Nome invalido')