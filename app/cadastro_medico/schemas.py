from app.extensions import ma 
from app.cadastro_medico.model import Medico
from marshmallow import ValidationError, validates
from app.agendamento_atendimento.schemas import AgendamentoSchema
from app.horario_disponivel.schemas import HorarioSchema

class MedicoSchema(ma.SQLAlchemySchema):

    class Meta:

        model = Medico
        load_instance=True
        ordered=True

    id = ma.Integer(dump_only=True)
    nome = ma.String(required=True)
    sobrenome = ma.String(required=True)
    especialidade = ma.String(required=True)
    sexo = ma.String(required=True)
    bio = ma.String()
    foto_perfil = ma.String(required=True)
    email = ma.Email(required=True)
    facebook = ma.String()
    twitter = ma.String()
    instagram = ma.String()
    cpf = ma.String(required=True)
    rg = ma.String(required=True)
    celular = ma.String(required=True)
    telefone_secundario = ma.String()
    endereco = ma.String(required=True)
    bairro = ma.String(required=True)
    numero = ma.String(required=True)
    complemento = ma.String(required=True)
    cidade = ma.String(required=True)
    estado = ma.String(required=True)
    cep = ma.String(required=True) 
    confirmacao_cadastro = ma.Boolean(required=False)
    password = ma.String(load_only=True, required=True)

    patient = ma.Nested('PatientSchema', dump_only=True)
    administrador = ma.Nested('AdministradorSchema', dump_only=True)
    anotacoesmedico = ma.Nested('AnotacoesMedicoSchema', many=True, dump_only=True)
    horario = ma.Nested(HorarioSchema, many=True, dump_only=True)
    agendamento = ma.Nested(AgendamentoSchema, many=True,  dump_only=True)

    @validates('nome')
    def validate_nome(self, nome): 
        if nome == '': 
            raise ValidationError('Nome invalido')

       