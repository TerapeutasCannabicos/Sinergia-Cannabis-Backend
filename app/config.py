from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    #DATABASE_URI = 'postgresql://logwmclheiubhf:f39c02fa603263d955c23f48106479456d09c74c0deaacfc72308ff058d2189e@ec2-3-224-7-166.compute-1.amazonaws.com:5432/dapblp3asm4kus'
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

