from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

# ...
def create_app(config_name):
    app = Flask(__name__)

    # ....

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # ...

    # We will next consider how we can create models
    #  for our database. And then we can see how we
    #  can authenticate users.