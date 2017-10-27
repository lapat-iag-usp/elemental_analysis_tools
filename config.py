import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
SQLALCHEMY_DATABASE_URI = 'postgres://elemental:elemental@192.168.100.71:5432/elemental'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '123'
