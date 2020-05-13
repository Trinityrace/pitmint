import os
class Config:
  '''
    General configuration parent class
  '''
  SECRET_KEY = os.environ.get("SECRET_KEY")
  #app.config['SECRET_KEY']='covid'
  SECRET_KEY ="covid"

  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql+psycopg2://john:passcoder@localhost/pyt')
  MAIL_SERVER= 'smtp.gnail.com'
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USERNAME= os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
  '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  # pass
  

class TestConfig(Config):
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcoder@localhost/pyt_test'

class DevConfig(Config):
  '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
  '''
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcoder@localhost/pyt'

  DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
}