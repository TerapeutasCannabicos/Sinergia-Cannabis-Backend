from app.extensions import db 
from app.model import BaseModel

class Agendamento(BaseModel):
    __tablename__ = 'agendamento'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    acess = db.Column(db.Boolean, default=False)
