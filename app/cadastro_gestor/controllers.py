from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_gestor.model import Gestor
from app.extensions import db, mail
from flask_mail import Message
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from .schemas import GestorSchema
from app.model import BaseModel
from app.utils.filters import filters

class GestorCurrent(MethodView): #/gestor/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=GestorSchema) 
        return jsonify(schema.dump(Gestor.query.all())), 200


class GestorCreate(MethodView): #/gestor
    def post(self):
        schema = GestorSchema()
        gestor = schema.load(request.json)

        gestor.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[gestor.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=gestor.nome))

        mail.send(msg)

        return schema.dump(gestor), 201

class GestorDetails(MethodView): #/gestor/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=GestorSchema)
        gestor = Gestor.query.get_or_404(id)
        return schema.dump(gestor), 200

    def put(self, id):
        gestor = Gestor.query.get_or_404(id)
        schema = GestorSchema()
        gestor = schema.load(request.json, instance = gestor)

        gestor.save()

        return schema.dump(gestor)

    def patch(self, id):
        gestor = Gestor.query.get_or_404(id)
        schema = GestorSchema()
        gestor = schema.load(request.json, instance = gestor, partial=True)

        gestor.save()

        return schema.dump(gestor)

    def delete(self,id): 
        gestor = Gestor.query.get_or_404(id)
        gestor.delete(gestor)

        return {}, 204

class ChangePassword(MethodView): #pw-change
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        gestor  = Gestor.query.filter_by(email=dados['email']).first_or_404()

        if not gestor: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[gestor.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=gestor.nome))
        
        mail.send(msg)

        return (" ", 200)