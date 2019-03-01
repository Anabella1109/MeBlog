from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User
from .. import db
from flask_login import login_user
from .forms import LoginForm
from flask_login import login_user,logout_user,login_required
# from ..email import mail_message
# from flask_fontawesome import FontAwesome

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User(id=1,username="Anabella1109",email='bellaxbx1109',pass_secure="bellamava")
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "MeBlog login"
    return render_template('auth/login.html',login_form = login_form,title=title)
