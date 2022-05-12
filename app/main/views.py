from flask import render_template,url_for, redirect, abort, request
from app.main import main
from ..models import Pitch, User, Comments, Category, Votes
from flask_login import current_user, login_required
from . forms import Pitches,Comments, Category, Updates
from .. import db,photos



@main.route('/')
def index():
    """view function that displays homepage"""

    categories = Category.get_category()
    main_pitch = Pitches.query.order_by('id').all()
    print(main_pitch)

    title = 'Home'

    return render_template('index.html', title=title, Category=categories, main_pitch=Pitches)

@main.route('/category/add_pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def add_pitch(id):

    form = Pitches
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content= form.content.data
        add_pitch= Pitch(content=content,category_id=category.id, user_id=current_user)
        add_pitch.save_pich()
        return redirect(url_for('.category', id=category.id))

    return render_template('newpitch.html', category=category,)

@main.route('/categories/<int:id>')
def category(id):
    category = Category.query.get(id)
    if category is None:
        abort(404)
    pitch=Pitch.add_pitch(id)
    return render_template('category.html', pitch=pitch, category=category)

@main.route('/add/category', methods=['GET','POST'])
@login_required
def new_category():
    form = Category()
    if form.validate_on_submit():
        name = form.name.data
        new_category = Pitches(name = name)
        new_category.save_category()
        return redirect(url_for('.index'))
    title = 'New category'
    return render_template('addcategory.html', category_form = form, title = title)

@main.route('/view-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
    all_category = Category.add_categories()
    pitches = Pitch.query.get(id)
    if pitches is None:
        abort(404)
    comment = Comments.add_comments(id)
    count_likes = Votes.query.filter_by(pitches_id=id, vote=1).all()
    count_dislikes = Votes.query.filter_by(pitches_id=id, vote=2).all()
    return render_template('view-pitch.html', pitches = pitches, comment = comment, count_likes=len(count_likes), count_dislikes=len(count_dislikes), category_id = id, categories=all_category)

@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    form = Comments()
    title = 'post comment'
    pitches = Pitch.query.filter_by(id=id).first()
    if pitches is None:
         abort(404)
    if form.validate_on_submit():
        opinion = form.opinion.data
        new_comment = Comments(opinion = opinion, user_id = current_user.id, pitches_id = pitches.id)
        new_comment.save_comment()
        return redirect(url_for('.view_pitch', id = pitches.id))
    return render_template('comment.html', comment_form = form, title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

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

@main.route('/pitch/upvote/<int:id>&<int:vote_type>')
@login_required
def upvote(id,vote_type):
    votes = Votes.query.filter_by(user_id=current_user.id).all()
    print(f'The new vote is {votes}')
    to_str=f'{vote_type}:{current_user.id}:{id}'
    print(f'The current vote is {to_str}')
    if not votes:
        new_vote = Votes(vote=vote_type, user_id=current_user.id, pitches_id=id)
        new_vote.save_vote()
        print('YOU HAVE new VOTED')
    for vote in votes:
        if f'{vote}' == to_str:
            print('YOU CANNOT VOTE MORE THAN ONCE')
            break
        else:
            new_vote = Votes(vote=vote_type, user_id=current_user.id, pitches_id=id)
            new_vote.save_vote()
            print('YOU HAVE VOTED')
            break
    return redirect(url_for('.view_pitch', id=id))














