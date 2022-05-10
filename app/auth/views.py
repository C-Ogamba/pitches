from flask import render_template, redirect, url_for, flash, request
from . import auth
from .. import db
from app.models import User
from app.auth.forms import LoginForm, SignupForm

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

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,
                    password=form.password.data, name=form.name.data, role_id=2)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to Pitches","email/welcome_user",user.email,user=user)
        return redirect(request.args.get('next') or url_for('main.index'))
    title = "New Account"
    return render_template('signup.html', form=form, title=title)

@auth.route('/logout')
@login_required
def logout():
    """Function that handles logout"""
    logout_user()
    return redirect(url_for("main.index"))
