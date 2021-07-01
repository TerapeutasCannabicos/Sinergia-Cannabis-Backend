from app.extensions import db

association_adm_gestor = db.Table('association_adm_gestor', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('gestor_id', db.Integer, db.ForeignKey('gestor.id')))

association_adm_paciente = db.Table('association_adm_paciente', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('paciente_id', db.Integer, db.ForeignKey('paciente.id')))

association_adm_medico = db.Table('association_adm_medico', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('medico_id', db.Integer, db.ForeignKey('medico.id')))

association_adm_outros = db.Table('association_adm_outros', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('outros_id', db.Integer, db.ForeignKey('outros.id')))

association_gestor_paciente = db.Table('ssociation_gestor_paciente', db.Model.metadata,
                            db.Column('gestor_id', db.Integer, db.ForeignKey('gestor.id')), 
                            db.Column('paciente_id', db.Integer, db.ForeignKey('paciente.id')))

association_adm_advogado = db.Table('association_adm_advogado', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('advogado_id', db.Integer, db.ForeignKey('advogado.id')))