import logging

from flask import Blueprint, request, render_template, abort
from utils import get_posts_by_word
from json import JSONDecodeError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    search_query = request.args.get('s')
    logging.info(f'Выполнен поиск по запросу "{search_query}"')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    return render_template('post_list.html', search_query=search_query, posts=posts)
