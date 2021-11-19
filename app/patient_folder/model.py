from app.extensions import db 
from app.model import BaseModel

class AnotacoesMedico(BaseModel):
    __tablename__ = 'anotacoesmedico'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(1000))

    medico_id = db.Column(db.Integer, db.ForeignKey("medico.id"))