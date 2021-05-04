from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_responsavel.model import Responsavel
from app.extensions import db, mail
from flask_mail import Message
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from .schemas import ResponsavelSchema
from app.model import BaseModel
from app.utils.filters import filters 

class ResponsavelCurrent(MethodView): #/responsavel/current
    def get(self):
        schema = filters.getSchema(qs=request.args, schema_cls=ResponsavelSchema) 
        return jsonify(schema.dump(Responsavel.query.all())), 200

class ResponsavelCreate(MethodView): #/responsavel
    def post(self):
        schema = ResponsavelSchema()
        responsavel = schema.load(request.json)

        responsavel.save()

        msg = Message(sender= 'camilamaia@poli.ufrj.br',
                               recipients=[responsavel.email],
                               subject= 'Bem-vindo!', 
                               html=render_template('email.html', nome=responsavel.nome))

        mail.send(msg)

        return schema.dump(responsavel), 201

class ResponsavelDetails(MethodView): #/responsavel/<int:id>
    def get(self,id):
        schema = filters.getSchema(qs=request.args, schema_cls=Responsavelschema)
        responsavel = Responsavel.query.get_or_404(id)
        return schema.dump(responsavel), 200

    def put(self, id):
        responsavel = Responsavel.query.get_or_404(id)
        schema = ResponsavelSchema()
        responsavel = schema.load(request.json, instance = responsavel)

        responsavel.save()

        return schema.dump(responsavel)

    def patch(self, id):
        responsavel = Responsavel.query.get_or_404(id)
        schema = ResponsavelSchema()
        responsavel = schema.load(request.json, instance = responsavel, partial=True)

        responsavel.save()

        return schema.dump(responsavel)

    def delete(self,id): 
        responsavel = Responsavel.query.get_or_404(id)
        responsavel.delete(responsavel)

        return {}, 204

class ResponsavelConfirm(MethodView): #responsavel-confirm
    def get(self, token):
        try:
            data = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        responsavel = Responsavel.query.get_or_404(data['identity'])

        if not responsavel.active:
            responsavel.active = True 
            responsavel.save()

        return render_template('email2.html')

class EmailPassword(MethodView): #pw-email
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            return {"email": "required"}, 400

        responsavel  = Responsavel.query.filter_by(email=dados['email']).first_or_404()

        if not responsavel: 
            return {'email não válido!'}

        token = create_acess_token(identity=responsavel.id, expires_delta=timedelta(minutes=30))
        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[responsavel.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', nome=responsavel.nome))
        
        mail.send(msg)

        return {'msg': 'email enviado'}, 200

class ResetPassword(MethodView): #pw-reset
    def patch(self, token):
        try: 
            responsavel = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401

        responsavel = Responsavel.query.get_or_404(responsavel['identity'])
        data = request.json

        if not data or not data['password']:
            return {"password": "required"}, 400

        responsavel.password = data['password']
        responsavel.save()

        return {'msg': 'senha atualizada'}, 200