from crypt import methods
from turtle import title
from flask import render_template, redirect, url_for, flash, request
from app.auth import bp
from . import auth
from .. import db

user = User()

@auth.route('/register', methods=["GET", "POST"])
def login():
    """
    view function that displays on login page"""
    form = LoginForm()
    if form.validate_on_submit():
        """creates user variable after successful login"""

        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            """condition to handle invalid user input"""

            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Username or Password')
    title = 'Login'

    return render_template('auth/login.html', title=title, form=form )