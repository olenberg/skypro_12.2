from flask import Flask, request, render_template, send_from_directory, jsonify
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.get('/uploads/<path:filename>/')
def static_dir(filename):
    return send_from_directory("uploads", filename)


app.run(host='127.0.0.1', port=5000)
