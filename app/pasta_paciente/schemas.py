from app.extensions import ma 
from app.pasta_paciente.model import AnotacoesMedico

class AnotacoesMedicoSchema(ma.SQLAlchemySchema):

    class Meta:

        model = AnotacoesMedico
        load_instance=True
        ordered=True    
    
    id = ma.Integer(dump_only=True)
    texto = ma.String()