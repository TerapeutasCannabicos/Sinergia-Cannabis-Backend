from app.agendamento_atendimento.model import Agendamento
from app.extensions import ma 

class AgendamentoSchema(ma.SQLAlchemySchema):
    class Meta: 
        model = Agendamento 
        load_instance=True 
        ordered=True
    
    id = ma.Integer(dump_only=True)
    date = ma.Date(required=True)
    disponivel = ma.Boolean(dump_only=True)
    paciente_id = ma.Integer(required=True)

    administrador = ma.Nested('AdministradorSchema', dump_only=True)
    paciente = ma.Nested('PacienteSchema', dump_only=True)