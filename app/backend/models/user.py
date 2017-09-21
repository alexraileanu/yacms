from app import db
from flask_user import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))
    is_enabled = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    articles = db.relationship('Article', backref='author', lazy='dynamic')

    def __init__(self, username=None, password=None, is_enabled=True, confirmed_at=None):
        self.username = username
        self.password = password
        self.is_enabled = is_enabled
        self.confirmed_at = confirmed_at
