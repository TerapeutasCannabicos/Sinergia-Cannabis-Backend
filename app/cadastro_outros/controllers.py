from flask.views import MethodView
from flask import request, jsonify, render_template
from app.cadastro_outros.model import Outros
from app.permissao_outros.model import PermissaoOutros
from app.extensions import mail
from flask_mail import Message
from flask_jwt_extended import decode_token
from app.cadastro_outros.schemas import OutrosSchema
from app.model import BaseModel
from app.utils.filters import filters
from app.permissions import advogado_jwt_required, administrador_jwt_required, medico_jwt_required, gestor_jwt_required 
from app.functions import cpf_check, email_check
import json

#/<int:medico_id>
class PermissionOutros(MethodView): #permission/outros

    def get(self): 

        outros = Outros.query.filter_by(permissao_adm=False)
        schema = filters.getSchema(qs=request.args, schema_cls=OutrosSchema, many=True)
        json_outros = jsonify(schema.dump(outros))
        json_outros = json_outros.json
        dicionario = {"outros": json_outros}

        return json.dumps(dicionario), 200

class PermissaoAdm(MethodView):   #/permissao/adm/outros/<int:id>
    def patch(self,id):
        outros = Outros.query.get_or_404(id)
        schema = OutrosSchema()
        outros = schema.load(request.json, instance = outros, partial=True)

        outros.save()

        return schema.dump(outros)
'''
        permissao_outros = Outros.query.get_or_404(id)
        permissao_outros.permissao = PermissaoOutros(outros_id = permissao_outros.id)
        permissao_outros[1].nivel_permissao == 1
'''


class OutrosCurrent(MethodView): #/outros/current
    def get(self):        
        schema = filters.getSchema(qs=request.args, schema_cls=OutrosSchema) 
        return jsonify(schema.dump(Outros.query.all())), 200


class OutrosCreate(MethodView): #/outros
    def post(self):
        schema = OutrosSchema()
        outros = schema.load(request.json)

        if not email_check(outros.email) or not cpf_check(outros.cpf):
            return {'error': 'Usuário já cadastrado'} 

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
'''
class Advogado 

        if PermissaoOutros.permissao_adm == True: 
            return administrador_jwt_required
        elif PermissaoOutros.permissao_gestor == True:
            return gestor_jwt_required
        elif PermissaoOutros.permissao_medico == True:
            return medico_jwt_required
        elif PermissaoOutros.permissao_advogado == True:
            return advogado_jwt_required
'''