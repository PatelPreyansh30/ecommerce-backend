from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.vo.product_vo import ProductVO
from base.com.dao.product_dao import ProductDAO, ProductCategoryDAO, ProductReviewsRatingsDAO

product_api_path = '/api/a3/products'


@app.route(f'{product_api_path}')
@jwt_required()
def get_products():
    product_dao = ProductDAO()
    product_category_dao = ProductCategoryDAO()
    category = request.args.get('category')
    if not category:
        return make_response({"msg": "Query param not correct"}, 400)
    else:
        try:
            category_id = product_category_dao.get_category_id_based_category(
                category)
            data = product_dao.get_all_products_based_category(category_id)
            if len(data) != 0:
                return make_response({"products": data}, 200)
            else:
                return make_response({"msg": "No products found"}, 400)
        except AttributeError:
            return make_response({"msg": "No products found for given category"}, 400)


@app.route(f'{product_api_path}/<int:id>')
@jwt_required()
def get_one_product(id):
    product_dao = ProductDAO()
    try:
        data = product_dao.get_single_product(id)
        if not data:
            return make_response({"msg": "No product found"}, 400)
        else:
            return make_response(data, 200)
    except TypeError:
        return make_response({"msg": "Invalid id"}, 400)


@app.route(f'{product_api_path}/reviews/<int:id>')
@jwt_required()
def get_one_product_reviews(id):
    product_review_rating_dao = ProductReviewsRatingsDAO()
    data = product_review_rating_dao.get_reviews_ratings_by_product(id)
    if len(data) == 0:
        return make_response({"msg": "No reviews found"}, 400)
    else:
        return make_response({"reviews": data}, 200)


@app.route(f'{product_api_path}/categories')
@jwt_required()
def get_all_categories():
    product_category_dao = ProductCategoryDAO()
    data = product_category_dao.get_all_categories()
    if len(data) != 0:
        return make_response({"categories": data}, 200)
    else:
        return make_response({"msg": "No categories found"}, 400)


@app.route(f'{product_api_path}/subcategory')
@jwt_required()
def get_subcategories():
    product_category_dao = ProductCategoryDAO()
    category = request.args.get('category')
    if not category:
        return make_response({"msg": "Query param not correct"}, 400)
    else:
        category_id = product_category_dao.get_category_id_based_category(
            category)
        data = product_category_dao.get_subcategory_based_category(category_id)
        if len(data) != 0:
            return make_response({"categories": data}, 200)
        else:
            return make_response({"msg": "No categories found"}, 400)


@app.route('/api/a3/user/reviews')
@jwt_required()
def get_reviews_by_user():
    product_review_dao = ProductReviewsRatingsDAO()
    user_id = get_jwt_identity().get('userId')
    data = product_review_dao.get_reviews_ratings_by_user(user_id)
    if len(data) != 0:
        return make_response({"reviews": data}, 200)
    else:
        return make_response({"msg": "No reviews found"}, 400)
