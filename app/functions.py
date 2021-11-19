from app.cadastro_administrador.model import Administrador
from app.cadastro_lawyer.model import Lawyer
from app.cadastro_gestor.model import Gestor
from app.cadastro_medico.model import Medico
from app.cadastro_patient.model import Patient
from app.cadastro_outros.model import Outros
from app.cadastro_responsavel.model import Responsavel
#from app.permissao_outros import PermissaoOutros

def email_check(email):

    administrador = Administrador.query.filter_by(email=email).first()
    lawyer = Lawyer.query.filter_by(email=email).first()
    gestor = Gestor.query.filter_by(email=email).first()
    medico = Medico.query.filter_by(email=email).first()
    outros = Outros.query.filter_by(email=email).first()
    responsavel = Responsavel.query.filter_by(email=email).first()

    if administrador or lawyer or gestor or medico or outros or responsavel:
        return False

    return True

def cpf_check(cpf):

    administrador = Administrador.query.filter_by(cpf=cpf).first()
    lawyer = Lawyer.query.filter_by(cpf=cpf).first()
    gestor = Gestor.query.filter_by(cpf=cpf).first()
    medico = Medico.query.filter_by(cpf=cpf).first()
    outros = Outros.query.filter_by(cpf=cpf).first()
    patient = Patient.query.filter_by(cpf=cpf).first()
    responsavel = Responsavel.query.filter_by(cpf=cpf).first()

    if administrador or lawyer or gestor or medico or outros or patient or responsavel:
        return False

    return True
'''
def adm_permission(permissao_adm, permissao_gestor, permissao_medico, permissao_lawyer):
    if PermissaoOutros.permissao_adm or PermissaoOutros.permissao_lawyer or PermissaoOutros.permissao_gestor or PermissaoOutros.permissao_medico:
        return False 
    
    return True 
'''