from flask import *
from base import app


@app.route('/', methods=['GET'])
def get_home_page():
    return "Hello World"
