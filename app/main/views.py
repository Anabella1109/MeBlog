from flask import render_template,request,redirect,url_for, abort
from . import main
from ..request import get_quote
from .forms import CommentForm,UpdateProfile
from .. import db,photos
from ..models import Quote,Post,User,Comment,Subscription
from flask_login import login_required, current_user
# from ..email import mail_message

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

@main.route('/new/comment/<int:id>', methods = ['GET','POST'])
def add_comment(id):
  post=Post.query.filter_by(id=id).first()
  if pitch is None:
    abort(404)

  form=CommentForm()
  if form.validate_on_submit():
     name=form.name.data
     comment=form.comment.data
     new_comment=Comment(content=comment ,post=post)
     db.session.add(new_comment)  
     db.session.commit() 
     
     return redirect(url_for('main.index'))
  return render_template('comment.html', comment_form=form)