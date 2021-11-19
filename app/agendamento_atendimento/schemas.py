from app.agendamento_atendimento.model import Agendamento
from app.extensions import ma 

class AgendamentoSchema(ma.SQLAlchemySchema):
    class Meta: 
        model = Agendamento 
        load_instance=True 
        ordered=True
    
    id = ma.Integer(dump_only=True)
    date = ma.DateTime(required=True, format='%d/%m/%y-%H:%M:%S')
    active = ma.Boolean(required=False)
    patient_id = ma.Integer(required=False)
    administrador_id = ma.Integer(required=False)
    medico_id = ma.Integer(required=False)
    horario_id = ma.Integer(required=False)

    horario = ma.Nested('HorarioSchema', dump_only=True, exclude = ['agendamento'])