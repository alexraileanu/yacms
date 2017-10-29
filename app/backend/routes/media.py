from app.backend import backend
from app import app
from flask import send_from_directory


@backend.route('/media/<path:filename>')
def media_file(filename):
    """
        I know, I know. Flask is not intended for serving images.
    """
    media_folder = app.config['MEDIA_FOLDER']
    return send_from_directory(media_folder, filename)
