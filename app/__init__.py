# from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config_options
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_uploads import UploadSet, configure_uploads, IMAGES


# bootstrap = Bootstrap()
# db = SQLAlchemy()

# # ...
# def create_app(config_name):
#     app = Flask(__name__)

#     # ....

#     # Initializing flask extensions
#     bootstrap.init_app(app)
#     db.init_app(app)

#     # ...

#     # We will next consider how we can create models
#     #  for our database. And then we can see how we
#     #  can authenticate users.