from app import create_app,db
from flask_script import Manager, Server
#from app.models import User, Pitch, Comments, PitchCategory
from app.models import User
from flask_migrate import Migrate, MigrateCommand

# \ backslash