import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
#'postgres://username:password@localhost:5432/dbname'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '123'
