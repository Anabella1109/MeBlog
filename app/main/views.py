from flask import render_template,request,redirect,url_for, abort
from . import main
from ..request import get_quote
# from .forms import ReviewForm,UpdateProfile
from .. import db,photos
from ..models import Quote
from flask_login import login_required, current_user
# import markdown2 
# from flask_fontawesome import FontAwesome

@main.route('/')
def index():
  '''
    View root page function that returns the index page and its data
    '''

  quote=get_quote()
  title="Home| Welcome to MeBlog"

  return render_template('index.html',title=title,quote=quote)