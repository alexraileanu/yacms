from app.backend import backend
from app.backend.models.image import Image
from flask import request, jsonify
from flask_user import login_required, current_user
from werkzeug.utils import secure_filename
from os import path
from app import app
from uuid import uuid4
from pathlib import Path
from PIL import Image as PILImage


@backend.route('/image/add', methods=['POST', 'GET'])
@login_required
def image_add():
    file = request.files['file']
    original_filename = secure_filename(file.filename)
    exists = Image.exists('original_name', original_filename)
    current_image = current_user.image.first()

    if exists:
        return jsonify({'msg': 'Image already exists', 'cat': 'error'})

    extension = Path(original_filename).suffix
    uniq = uuid4().hex
    uuid = '{}{}'.format(uniq, extension)
    thumbnail_name = '{}_thumb.{}'.format(uniq, extension)
    save_path = path.join(app.config['UPLOAD_FOLDER'], uuid)
    file.save(save_path)

    im = PILImage.open(save_path)
    im.thumbnail((128, 128))
    im.save(path.join(app.config['UPLOAD_FOLDER'], thumbnail_name))

    image = current_image or Image()
    image.original_name = original_filename
    image.thumbnail_name = thumbnail_name
    image.path = save_path
    image.uid = uuid

    current_user.image.append(image)
    msg, cat = image.save()

    return jsonify({'msg': msg, 'cat': cat})
