from app import db
import datetime


class Article(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(length=255))
    slug = db.Column(db.String(length=255))
    content = db.Column(db.Text())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title='', content=''):
        print(title)
        self.title = title
        self.content = content
