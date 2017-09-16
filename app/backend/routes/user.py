from app.backend import backend, user_manager
from app.backend.models.user import User
from app import db


@backend.route('/create-demo-user')
def create_demo_user():
    user = User(
        username='demo',
        password=user_manager.hash_password('demo'),
    )
    db.session.add(user)
    db.session.commit()
