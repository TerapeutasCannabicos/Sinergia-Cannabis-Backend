from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
jwt = JWTManager()
ma = Marshmallow() 
cors = CORS()
