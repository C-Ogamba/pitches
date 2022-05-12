from turtle import title
from flask import render_template,url_for,flash, redirect
from app.main import main
from ..models import Pitch, User
from flask_login import current_user, login_required
from . forms import Pitches,Comments, Category, Updates


@main.route('/')
def index():
    """view function that displays homepage"""

    categories = Category.get_category()
    main_pitch = Pitches.query.order_by('id').all()
    print(main_pitch)

    title = 'Home'

    return render_template('index.html', title=title, Category=categories, main_pitch=Pitches)

@main.route('/profile')
def profile():

	return render_template('profile.html')


@main.route('/pitches')
def pitches():
	return render_template('pitches.html')  




