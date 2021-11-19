from app.extensions import db

association_adm_gestor = db.Table('association_adm_gestor', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('gestor_id', db.Integer, db.ForeignKey('gestor.id')))

association_adm_patient = db.Table('association_adm_patient', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('patient_id', db.Integer, db.ForeignKey('patient.id')))

association_adm_medico = db.Table('association_adm_medico', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('medico_id', db.Integer, db.ForeignKey('medico.id')))

association_adm_outros = db.Table('association_adm_outros', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('outros_id', db.Integer, db.ForeignKey('outros.id')))

association_gestor_patient = db.Table('ssociation_gestor_patient', db.Model.metadata,
                            db.Column('gestor_id', db.Integer, db.ForeignKey('gestor.id')), 
                            db.Column('patient_id', db.Integer, db.ForeignKey('patient.id')))

association_adm_lawyer = db.Table('association_adm_lawyer', db.Model.metadata,
                            db.Column('administrador_id', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('lawyer_id', db.Integer, db.ForeignKey('lawyer.id')))