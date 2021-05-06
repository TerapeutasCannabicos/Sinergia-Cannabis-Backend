from app.extensions import db

association_table = db.Table('association', db.Model.metadata,
                            db.Column('administrador', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('gestor', db.Integer, db.ForeignKey('gestor.id')))

association_table2 = db.Table('association2', db.Model.metadata,
                            db.Column('administrador', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('paciente', db.Integer, db.ForeignKey('paciente.id')))

association_table3 = db.Table('association3', db.Model.metadata,
                            db.Column('administrador', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('medico', db.Integer, db.ForeignKey('medico')))

association_table4 = db.Table('association4', db.Model.metadata,
                            db.Column('administrador', db.Integer, db.ForeignKey('administrador.id')), 
                            db.Column('outros', db.Integer, db.ForeignKey('outros')))

association_table5 = db.Table('association5', db.Model.metadata,
                            db.Column('gestor', db.Integer, db.ForeignKey('gestor.id')), 
                            db.Column('paciente', db.Integer, db.ForeignKey('paciente')))