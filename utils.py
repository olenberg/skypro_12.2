import json


def load_posts():
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_word(word):
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture):
    filename = picture.filename
    path = f'uploads/{filename}'
    picture.save(path)
    return path
