from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_mail import Mail
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
ma = Marshmallow() 
