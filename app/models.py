from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from .import login_manager
from app import db


# @login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    pass_secure = db.Column(db.String(255))

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pitches = db.relationship('Pitch', backref='user', lazy="dynamic")
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Pitch(db.Model):
    __tablename__='pitches'
    # __table_args__ = {'extend_existing': True}
   

    pitch_id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # timestamp = db.column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def __repr__(self):
        '''
        Function to display user pitch
        '''
        return '<Pitch {}>'.format(self.body)

class Comments(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer, primary_key=True)
    opinion = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.pitch_id"))

    def create_comments(self):
        db.session.add(self)
        db.session.commit()
        return self

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        '''
        Function to display user comments
        '''
        return '<Comments {}>'.format(self.body)

class Category(db.Model):
    __tablename__='category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_category(self):
        category = Category.query.all()
        return category


    def __repr__(self):
        '''
        Function to display user comments
        '''
        return '<Category {}>'.format(self.body)

class Votes(db.Model):
    __tablename__='votes'

    id = db.Column(db.Integer, primary_key=True)



    


    
