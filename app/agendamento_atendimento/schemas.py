from app.agendamento_atendimento.model import Agendamento
from app.extensions import ma 

class AgendamentoSchema(ma.SQLAlchemySchema):
    class Meta: 
        model = Agendamento 
        load_instance=True 
        ordered=True
    
    id = ma.Integer(dump_only=True)
    date = ma.DateTime(required=True)