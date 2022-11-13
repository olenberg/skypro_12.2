import logging

from flask import Flask, Blueprint, request, render_template
from utils import save_picture, add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Нет картинки или текста'

    if picture.filename.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
        logging.info('Файл имеет неверное расширение')
        return 'Неверное расширение'

    try:
        picture_path = save_picture(picture)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'

    post = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)

