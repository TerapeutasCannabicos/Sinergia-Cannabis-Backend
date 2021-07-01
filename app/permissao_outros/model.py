from app.extensions import db
from app.model import BaseModel
from flask.views import MethodView
from app.utils.filters import filters
from flask import request, jsonify

class PermissaoOutros(BaseModel): 
    __tablename__ = 'permissao'
    id = db.Column(db.Integer, primary_key=True)
    nivel_permissao = db.Column(db.Integer)

    outros_id = db.Column(db.Integer, db.ForeignKey('outros.id'))
    outros = db.relationship("Outros", back_populates="permissao")
