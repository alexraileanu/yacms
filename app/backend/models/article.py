from app import db
from app.backend.models.mixins import BaseMixin
import datetime


class Article(BaseMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(length=255))
    slug = db.Column(db.String(length=255))
    content = db.Column(db.Text())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='article', lazy='dynamic')

    type = 'article'

    def __init__(self, title='', content=''):
        self.title = title
        self.content = content

    """
        get an object from the database based on a filter column (if set).
        
        defaults to getting all the objects
    """
    @classmethod
    def get(cls, filter_column=None, filter_value=None):
        if filter_column:
            return cls.query.filter(getattr(cls, filter_column) == filter_value).first_or_404()

        return cls.query.all()
