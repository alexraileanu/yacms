import click
from app import app, db
from app.backend.models.user import User
from app.backend import user_manager
from sqlalchemy.exc import SQLAlchemyError


@app.cli.command()
def seed():
    """
    Add initial users to the db.
    """
    user = User(username='demo', password=user_manager.hash_password('demo'))
    try:
        db.session.add(user)
        db.session.commit()
        click.echo('added user {} to the db'.format(user.username))
    except SQLAlchemyError as e:
        click.echo('error occurred: {}'.format(str(e)))
