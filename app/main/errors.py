from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourfour(error):
  return render_template('errors/404.html'),404