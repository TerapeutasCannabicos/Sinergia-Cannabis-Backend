from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_administrador.model import Administrador
from app.extensions import db, mail
from flask_mail import Message
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from .schemas import AdministradorSchema
from app.model import BaseModel
from app.utils.filters import filters

class AdministradorCurrent(MethodView): #/administrador/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=AdministradorSchema) 
        return jsonify(schema.dump(Administrador.query.all())), 200


class AdministradorCreate(MethodView): #/administrador
    def post(self):
        schema = AdministradorSchema()
        administrador = schema.load(request.json)

        administrador.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[administrador.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=administrador.nome))

        mail.send(msg)

        return schema.dump(administrador), 201

class AdministradorDetails(MethodView): #/administrador/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=AdministradorSchema)
        administrador = Administrador.query.get_or_404(id)
        return schema.dump(administrador), 200

    def put(self, id):
        administrador = Administrador.query.get_or_404(id)
        schema = AdministradorSchema()
        administrador = schema.load(request.json, instance = administrador)

        administrador.save()

        return schema.dump(administrador)

    def patch(self, id):
        administrador = Administrador.query.get_or_404(id)
        schema = AdministradorSchema()
        administrador = schema.load(request.json, instance = administrador, partial=True)

        administrador.save()

        return schema.dump(administrador)

    def delete(self,id): 
        administrador = Administrador.query.get_or_404(id)
        administrador.delete(administrador)

        return {}, 204

class ChangePassword(MethodView): #pw-change
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        administrador  = Administrador.query.filter_by(email=dados['email']).first_or_404()

        if not administrador: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[administrador.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=administrador.nome))
        
        mail.send(msg)

        return (" ", 200)