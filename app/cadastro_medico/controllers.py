from flask.views import MethodView
from flask import request, jsomify, render_templete
from app.cadastro_medico.model import Medico
from app.extensions import db, mail
from flask_mail import Messege
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from .schemas import MedicoSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.google_sheets.spreads import 

class MedicoCurrent(methodView): #/medico/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema) 
        return jsonify(schema.dump(Medico.query.all())), 200


class MedicoCreate(MethodView): #/medico
    def post(self):
        schema = MedicoSchema()
        medico = schema.load(request.json)

        medico.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[medico.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', name=medico.name))

        mail.send(msg)

        return schema.dump(medico), 201

class MedicoDetails(MethodView): #/medico/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=MedicoSchema)
        medico = Medico.query.get_or_404(id)
        return schema.dump(medico), 200

    def put(self, id):
        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        medico = schema.load(request.json, instance = medico)

        medico.save()

        return schema.dump(medico)

    def patch(self, id):
        medico = Medico.query.get_or_404(id)
        schema = MedicoSchema()
        medico = schema.load(request.json, instance = medico, partial=True)

        medico.save()

        return schema.dump(medico)

    def delete(self,id): 
        medico = Medico.query.get_or_404(id)
        medico.delete(medico)

        return {}, 204

class ChangePassword(MethodView): #pw-change
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            retun {"email": "required"}, 400

        medico  = Medico.query.filter_by(email=dados['email']).first_or_404()

        if not medico: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[medico.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', name=medico.name))
        
        mail.send(msg)

        return (" ", 200)
