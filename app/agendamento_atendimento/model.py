from app.extensions import db 
from app.model import BaseModel

class Agendamento(BaseModel):
    __tablename__ = 'agendamento'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    active = db.Column(db.Boolean, default=False)

    administrador_id = db.Column(db.Integer, db.ForeignKey('administrador.id'), nullable=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    horario_id = db.Column(db.Integer, db.ForeignKey('horario.id'), nullable=True)
    horario = db.relationship("Horario", back_populates='agendamento')
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'), nullable=False)
    
#mudar para confirmado
