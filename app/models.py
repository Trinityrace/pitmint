from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime;
from sqlalchemy.sql import func
from . import db

#...
@login_manager.user_loader
def load_user(user_id):
    """
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    """
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    #columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")

    # passwords securing
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

#pitches class
class Pitch(db.Model):
    """
    List of pitches in each category 
    """

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String())
    content = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    # author = db.Column(db.String())
    # comment = db.relationship("Comments", backref="pitches", lazy = "dynamic")
    # vote = db.relationship("Votes", backref="pitches", lazy = "dynamic")



    def save_pitch(self):
        """
        Save the pitches 
        """
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def clear_pitches(cls):
    #     Pitch.all_pitches.clear()

    # display pitches
    def get_pitches(id):
        pitches = Pitch.query.order_by(Pitch.posted).all()
        return pitches

    # def get_user():


    # def __repr__(self):
    #     return f'User {self.username}'