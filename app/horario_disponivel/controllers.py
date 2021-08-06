from flask.views import MethodView
from flask import request, jsonify, render_template
from app.horario_disponivel.model import Horario
from app.extensions import db
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from app.horario_disponivel.schemas import HorarioSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.functions import cpf_check, email_check
from app.permissions import medico_jwt_required

class HorarioMedico(MethodView): #/horario/medico/current/<int:medico_id>
    def get(self, medico_id):
        schema = filters.getSchema(qs=request.args, schema_cls=HorarioSchema)
        horario = Horario.query.get_or_404(medico_id)
        return schema.dump(horario), 200

class HorarioCreate(MethodView): #/horario/medico/create/<int:medico_id>
    decorators = [medico_jwt_required]
    def post(self, medico_id):
        schema = HorarioSchema(medico_id)
        horario = schema.load(request.json)

        horario.save()

        return schema.dump(horario), 201

class HorarioDetails(MethodView): #/horario/medico/create/<int:medico_id>/<int:horario_id>
    def get(self, medico_id, horario_id):
        schema = filters.getSchema(qs=request.args, schema_cls=HorarioSchema)
        horario = Horario.query.get_or_404(id)
        return schema.dump(horario), 200

    def put(self, medico_id, horario_id):
        horario = Horario.query.get_or_404(id)
        schema = HorarioSchema()
        horario = schema.load(request.json, instance = horario)

        horario.save()

        return schema.dump(horario)

    def patch(self, medico_id, horario_id):
        horario = Horario.query.get_or_404(id)
        schema = HorarioSchema()
        horario = schema.load(request.json, instance = horario, partial=True)

        horario.save()

        return schema.dump(horario)

    def delete(self, medico_id, horario_id): 
        horario = Horario.query.get_or_404(id)
        horario.delete(horario)

        return {}, 204
