from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.dao.product_dao import ProductCategoryDAO

home_api_path = '/api/a5/home'


@app.route('/', methods=['GET'])
def get_home_page():
    return make_response({"msg": "Hello World"}, 200)


@app.route(f'{home_api_path}/categories')
@jwt_required()
def header_categories():
    product_category_dao = ProductCategoryDAO()
    try:
        categories = product_category_dao.get_categories_for_header()
        return make_response({"categories": categories}, 200)
    except Exception as e:
        return make_response({"msg": "Something went wrong, try again"}, 400)