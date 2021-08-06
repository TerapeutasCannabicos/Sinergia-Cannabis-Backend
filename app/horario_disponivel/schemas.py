from app.horario_disponivel.model import Horario
from app.extensions import ma 

class Horario(ma.SQLAlchemySchema):
    class Meta: 
        model = Horario
        load_instance=True 
        ordered=True
    
    id = ma.Integer(dump_only=True)
    date = ma.DateTime(required=True)
    disponivel = ma.Boolean(dump_only=True)

    medico = ma.Nested('MedicoSchema', many=True, dump_only=True)