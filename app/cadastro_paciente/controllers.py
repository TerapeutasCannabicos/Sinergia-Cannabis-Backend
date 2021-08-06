from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_paciente.model import Paciente
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import decode_token
from .schemas import PacienteSchema
from app.utils.filters import filters 
from app.permissions import responsavel_paciente_required, responsavel_required
from app.permissions_with_id import responsavel_paciente_jwt_required

class PacienteLista(MethodView): #/paciente/lista
    decorators = [responsavel_paciente_required]
    def get(self):

        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema, many=True) 
        return jsonify(schema.dump(Paciente.query.all())), 200


class PacienteCreate(MethodView): #/paciente
    decorators = [responsavel_required]
    def post(self):
        schema = PacienteSchema()
        paciente = schema.load(request.json)

        paciente.save()

        return schema.dump(paciente), 201

class PacienteDetails(MethodView): #/paciente/<int:id>
    decorators = [responsavel_paciente_jwt_required]
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema)
        paciente = Paciente.query.get_or_404(id)
        return schema.dump(paciente), 200

    def put(self, id):
        paciente = Paciente.query.get_or_404(id)
        schema = PacienteSchema()
        paciente = schema.load(request.json, instance = paciente)

        paciente.save()

        return schema.dump(paciente)

    def patch(self, id):
        paciente = Paciente.query.get_or_404(id)
        schema = PacienteSchema()
        paciente = schema.load(request.json, instance = paciente, partial=True)

        paciente.save()

        return schema.dump(paciente)

    def delete(self,id): 
        paciente = Paciente.query.get_or_404(id)
        paciente.delete(paciente)

        return {}, 204