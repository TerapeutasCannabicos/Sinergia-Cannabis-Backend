from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_outros.model import Outros
from app.extensions import db, mail
from flask_mail import Message
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from .schemas import OutrosSchema
from app.model import BaseModel
from app.utils.filters import filters

class OutrosCurrent(MethodView): #/outros/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=OutrosSchema) 
        return jsonify(schema.dump(Outros.query.all())), 200


class OutrosCreate(MethodView): #/outros
    def post(self):
        schema = OutrosSchema()
        outros = schema.load(request.json)

        outros.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[outros.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=outros.nome))

        mail.send(msg)

        return schema.dump(outros), 201

class OutrosDetails(MethodView): #/outros/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=OutrosSchema)
        outros = Outros.query.get_or_404(id)
        return schema.dump(outros), 200

    def put(self, id):
        outros = Outros.query.get_or_404(id)
        schema = OutrosSchema()
        outros = schema.load(request.json, instance = outros)

        outros.save()

        return schema.dump(outros)

    def patch(self, id):
        outros = Outros.query.get_or_404(id)
        schema = OutrosSchema()
        outros = schema.load(request.json, instance = outros, partial=True)

        outros.save()

        return schema.dump(outros)

    def delete(self,id): 
        outros = Outros.query.get_or_404(id)
        outros.delete(outros)

        return {}, 204

class OutrosConfirm(MethodView): #outros-confirm
    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        outros = Outros.query.get_or_404(data['identity'])

        if not outros.active:
            outros.active = True 
            outros.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        outros  = Outros.query.filter_by(email=dados['email']).first_or_404()

        if not outros: 
            return {'email não válido!'}

        token = create_acess_token(identity=outros.id, expires_delta=timedelta(minutes=30))
        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[outros.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=outros.nome))
        
        mail.send(msg)

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset
    def patch(self, token):
        try: 
            outros = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        outros = Outros.query.get_or_404(outros['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        outros.password = data['password']
        outros.save()

        return {'msg': 'senha atualizada'}, 200