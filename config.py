# class Config:
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcoder@localhost/pit'

import os
class Config:
  '''
    General configuration parent class
  '''
  SECRET_KEY = os.environ.get("SECRET_KEY")
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://john:passcoder@localhost/pit'


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