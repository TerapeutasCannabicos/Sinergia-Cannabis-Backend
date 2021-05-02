from flask.views import MethodView
from flask import request, jsomify, render_templete
from app.cadastro_paciente.model import Paciente
from app.extensions import db, mail
from flask_mail import Messege
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from .schemas import PacienteSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.google_sheets.spreads import 

class PacienteCurrent(methodView): #/paciente/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=PacienteSchema) 
        return jsonify(schema.dump(Paciente.query.all())), 200


class PacienteCreate(MethodView): #/paciente
    def post(self):
        schema = PacienteSchema()
        paciente = schema.load(request.json)

        paciente.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[paciente.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', name=paciente.name))

        mail.send(msg)

        return schema.dump(paciente), 201

class PacienteDetails(MethodView): #/paciente/<int:id>
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

class ChangePassword(MethodView): #pw-change
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            retun {"email": "required"}, 400

        paciente  = Paciente.query.filter_by(email=dados['email']).first_or_404()

        if not paciente: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[paciente.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', name=paciente.name))
        
        mail.send(msg)

        return (" ", 200)
