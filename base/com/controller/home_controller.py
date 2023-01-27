from base import app


@app.route('/', ['GET'])
def get_home_page():
    return "Hello World"
