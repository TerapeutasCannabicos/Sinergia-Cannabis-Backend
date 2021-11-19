from os import environ
#from app.sensive import Sensive as sensive

'''class StorageConfig:
    PROJECT_NAME = sensive.PROJECT_NAME

    AWS_ACCESS_KEY_ID = sensive.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = sensive.AWS_SECRET_ACCESS_KEY
    AWS_REGION = sensive.AWS_REGION
    AWS_BUCKET_ENDPOINT = sensive.AWS_BUCKET_ENDPOINT 
    AWS_BUCKET_NAME = sensive.AWS_BUCKET_NAME
    AWS_PROJECT_NAME = sensive.AWS_PROJECT_NAME
    AWS_ALLOWED_FORMATS = ['jpg','png','pdf']

class Config:

    SQLALCHEMY_DATABASE_URI = sensive.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = sensive.SQLALCHEMY_TRACK_MODIFICATIONS
    JSON_SORT_KEYS = sensive.JSON_SORT_KEYS

    MAIL_SERVER = sensive.MAIL_SERVER
    MAIL_PORT = sensive.MAIL_PORT
    MAIL_USERNAME = sensive.MAIL_USERNAME
    MAIL_PASSWORD = sensive.MAIL_PASSWORD
    MAIL_USE_TLS = sensive.MAIL_USE_TLS
    MAIL_USE_SSL = sensive.MAIL_USE_SSL

    JWT_SECRET_KEY = sensive.JWT_SECRET_KEY

    DEBUG = True'''


class StorageConfig:
    PROJECT_NAME = environ.get('PROJECT_NAME')

    AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID') 
    AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = environ.get('AWS_REGION') 
    AWS_BUCKET_ENDPOINT = environ.get('AWS_BUCKET_ENDPOINT') 
    AWS_BUCKET_NAME = environ.get('AWS_BUCKET_NAME') 
    AWS_PROJECT_NAME = environ.get('AWS_PROJECT_NAME') 
    AWS_ALLOWED_FORMATS = ['jpg','png','pdf']

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    #DATABASE_URI = 'postgresql://dciapspmiuagea:3b15b1505e2ea892e902f5885c08825d0f754c83b16bfd3766f5a386722eeab9@ec2-54-158-247-97.compute-1.amazonaws.com:5432/d3d5ver1sv0pj4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    JWT_SECRET_KEY = environ.get('SECRET_KEY')

    DEBUG = True

