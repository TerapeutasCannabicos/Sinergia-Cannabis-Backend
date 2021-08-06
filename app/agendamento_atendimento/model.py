from app.extensions import db 
from app.model import BaseModel

class Agendamento(BaseModel):
    __tablename__ = 'agendamento'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), nullable=False)
    disponivel = db.Column(db.Boolean, default=True)

    administrador_id = db.Column(db.Integer, db.ForeignKey("administrador.id"))
    paciente_id = db.Column(db.Integer, db.ForeignKey("paciente.id"))


