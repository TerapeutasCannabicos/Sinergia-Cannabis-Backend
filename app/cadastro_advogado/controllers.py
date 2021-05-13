from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_advogado.model import Advogado
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import jwt_required, decode_token
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

class AdvogadoConfirm(MethodView): #advogado-confirm
    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        advogado = Advogado.query.get_or_404(data['identity'])

        if not advogado.active:
            advogado.active = True 
            advogado.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email
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

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset
    def patch(self, token):
        try: 
            advogado = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        advogado = Advogado.query.get_or_404(advogado['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        advogado.password = data['password']
        advogado.save()

        return {'msg': 'senha atualizada'}, 200