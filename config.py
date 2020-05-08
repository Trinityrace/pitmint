import os
class Config:
  '''
    General configuration parent class
  '''
  SECRET_KEY = os.environ.get("SECRET_KEY")
  WTF_CSRF_SECRET_KEY=("covid")
  SECRET_KEY=("covid")
  # SECRET_KEY = os.random(32)
  # app.config['SECRET_KEY'] = covid
  # app.config.update(dict(
  #   SECRET_KEY="powerful secretkey",
  #   WTF_CSRF_SECRET_KEY="a csrf secret key"
  #   ))

  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcoder@localhost/pit'
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
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcoder@localhost/pit_test'

class DevConfig(Config):
  '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
  '''
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcoder@localhost/pit'

  DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
}