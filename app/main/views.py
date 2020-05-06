from flask import Flask, render_template, url_for, request, redirect, url_for, abort

from .forms import PitchForm, UpdateProfile
from . import main

from ..models import User, Pitch
from flask_login import login_required, current_user
from .. import db
from .. import photos

app = Flask(__name__)

#app.config['SECRET_KEY']= 'covid'


@main.route('/')
def index():
    pitch = Pitch.query.order_by('posted').all()


    title = 'Welcome'
    return render_template('index.html', title = title, pitch=pitch)




#Route for adding a new pitch
@main.route('/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
  form = PitchForm()
  if form.validate_on_submit():
    content = form.content.data
    new_pitch= Pitch(content=content, user_id = current_user.id)
    new_pitch.save_pitch()
    return redirect(url_for('.index', ))
  return render_template('new_pitch.html', pitch_form=form)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)

  return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)

  form = UpdateProfile()
  if form.validate_on_submit():
    user.bio = form.bio.data
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@app.route("/home/")
def home():
  return render_template('index.html', pitchs=pitchs)

@main.route("/about")
def about():
  return render_template('about.html',title='About')

if __name__ =='__main__':
  app.run(debug=True)
