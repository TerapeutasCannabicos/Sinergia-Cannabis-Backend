from flask.views import MethodView
from flask import request, jsonify, render_template
from app.horario_disponivel.model import Horario
from app.cadastro_medico.model import Medico
from app.extensions import db
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
from app.horario_disponivel.schemas import HorarioSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.permissions import medico_required
from app.permissions_with_id import medico_jwt_required
from app.model import BaseModel

#Ele não tá pegando a rota pelo id do médico, mas pelo id do horário
class HorarioMedico(MethodView): #/horario/medico/current/<int:medico_id>
    decorators = [medico_jwt_required]
    def get(self, medico_id):
        data = request.json
        schema = filters.getSchema(qs=request.args, schema_cls=HorarioSchema)
        #medico = Medico.query.get_or_404(horario)
        medico = Medico.query.filter_by(horario=data['horario'])
        #horario = Horario.query.get_or_404(medico_id)
        return schema.dump(medico), 200

#colocar um if para caso o horário já ter sido criado
class HorarioCreate(MethodView): #/horario/medico/create/<int:medico_id>
    decorators = [medico_jwt_required]
    def post(self, medico_id):
        schema = HorarioSchema()
        data = request.json
        data["medico_id"] = medico_id
        horario = schema.load(data)
        horario.save()

        return schema.dump(horario), 201

class HorarioDetails(MethodView): #/horario/medico/details/<int:medico_id>/<int:horario_id>
    decorators = [medico_jwt_required]
    def get(self, medico_id, horario_id):
        schema = filters.getSchema(qs=request.args, schema_cls=HorarioSchema)
        horario = Horario.query.get_or_404(horario_id)
        return schema.dump(horario), 200

    def delete(self, medico_id, horario_id): 
        horario = Horario.query.get_or_404(horario_id)
        horario.delete(horario)

        return {}, 204
