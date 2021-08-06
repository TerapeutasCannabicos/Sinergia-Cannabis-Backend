from os import environ
from app.sensive import Sensive as sensive

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

    DEBUG = True

    '''SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    #DATABASE_URI = 'postgresql://ckognfcohxqdzc:6910367063b4fb4cb4e1b4d8919e43b3ba48865be53152b9d018a67f1cc430a0@ec2-3-233-100-43.compute-1.amazonaws.com:5432/d6ml96jigkv1nj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    JWT_SECRET_KEY = environ.get('SECRET_KEY')

    DEBUG = True'''

