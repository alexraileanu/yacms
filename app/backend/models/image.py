from app import db
from app.backend.models.mixins import BaseMixin


class Image(db.Model, BaseMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    original_name = db.Column(db.String(length=255))
    thumbnail_name = db.Column(db.String(length=255))
    uid = db.Column(db.String(length=255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    type = 'image'

    def __init__(self, original_name='', path='', uid='', thumbnail=''):
        self.original_name = original_name
        self.path = path
        self.uid = uid
        self.thumbnail = thumbnail
