from flask.views import MethodView
from flask import request, jsomify, render_templete
from app.cadastro_responsavel.model import Responsavel
from app.extensions import db, mail
from flask_mail import Messege
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
from .schemas import ResponsavelSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.google_sheets.spreads import 

class ResponsavelCurrent(methodView): #/responsavel/current
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
                               html=render_template('email.html', name=responsavel.name))

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

class ChangePassword(MethodView): #pw-change
    def post(self):
        dados = request.json
        
        if not dados or not dados['email']:
            retun {"email": "required"}, 400

        responsavel = Responsavel.query.filter_by(email=dados['email']).first_or_404()

        if not responsavel: 
            return {'email não válido!'}

        msg = Message(sender='camilamaia@poli.ufrj.br',
                              recipients=[responsavel.email],
                              subject='Recuperação de Senha',
                              html=render_template('pw.html', name=responsavel.name))
        
        mail.send(msg)

        return (" ", 200)
