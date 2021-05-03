from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_advogado.model import Advogado
from app.extensions import db, mail
from flask_mail import Message
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from .schemas import AdvogadoSchema
from app.model import BaseModel
from app.utils.filters import filters

class AdvogadoCurrent(MethodView): #/advogado/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=AdvogadoSchema) 
        return jsonify(schema.dump(Advogado.query.all())), 200


class AdvogadoCreate(MethodView): #/advogado
    def post(self):
        schema = AdvogadoSchema()
        advogado = schema.load(request.json)

        advogado.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[advogado.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=advogado.nome))

        mail.send(msg)

        return schema.dump(advogado), 201

class AdvogadoDetails(MethodView): #/advogado/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=AdvogadoSchema)
        advogado = Advogado.query.get_or_404(id)
        return schema.dump(advogado), 200

    def put(self, id):
        advogado = Advogado.query.get_or_404(id)
        schema = AdvogadoSchema()
        advogado = schema.load(request.json, instance = advogado)

        advogado.save()

        return schema.dump(advogado)

    def patch(self, id):
        advogado = Advogado.query.get_or_404(id)
        schema = AdvogadoSchema()
        advogado = schema.load(request.json, instance = advogado, partial=True)

        advogado.save()

        return schema.dump(advogado)

    def delete(self,id): 
        advogado = Advogado.query.get_or_404(id)
        advogado.delete(advogado)

        return {}, 204

class ChangePassword(MethodView): #pw-change
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        advogado  = Advogado.query.filter_by(email=dados['email']).first_or_404()

        if not advogado: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[advogado.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=advogado.nome))
        
        mail.send(msg)

        return (" ", 200)