from flask import render_template,url_for,flash, redirect
from app.auth.forms import LoginForm,SignupForm
from app.main import main
from ..models import Pitch, User


@main.route('/')
@main.route('/index')
def index():
    """view function that displays homepage"""

    title = 'Home'
    return render_template('index.html', title=title)


@main.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account for {form.username.data} has been successfully created')
        return redirect(url_for('index'))
    return render_template('signup.html', title='SignUp', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@blog.com' and form.password.data == 'password':
            flash(f'Login succesful')
            return redirect(url_for('index'))
        else:
                flash(f'login failed')
        return render_template('login.html', title='login', form=form)