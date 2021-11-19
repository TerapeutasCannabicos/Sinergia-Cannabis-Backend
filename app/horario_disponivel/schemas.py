from app.horario_disponivel.model import Horario
from app.extensions import ma 

class HorarioSchema(ma.SQLAlchemySchema):
    class Meta: 
        model = Horario
        load_instance=True 
        ordered=True
    
    id = ma.Integer(dump_only=True)
    date = ma.DateTime(required=True, format='%d/%m/%y-%H:%M:%S')
    disponivel = ma.Boolean(required=False)
    medico_id = ma.Integer(required=False)

    agendamento = ma.Nested('AgendamentoSchema', dump_only=True)