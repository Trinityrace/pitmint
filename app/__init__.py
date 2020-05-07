from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

# ...
def create_app(config_name):

    app = Flask(__name__)
    #app configs
    app.config.from_object(config_options[config_name])
    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    configure_uploads(app,photos)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')


    return app

#     # ....

#     # Initializing flask extensions
#     bootstrap.init_app(app)
#     db.init_app(app)

#     # ...

#     # We will next consider how we can create models
#     #  for our database. And then we can see how we
#     #  can authenticate users.