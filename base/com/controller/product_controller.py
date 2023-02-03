from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.vo.product_vo import ProductVO
from base.com.dao.product_dao import ProductDAO, ReviewsRatingsDAO


@app.route('/api/a3/products')
@jwt_required()
def get_products():
    product_dao = ProductDAO()
    category = request.args.get('category')
    if not category:
        return make_response({"msg": "Query param not correct"}, 400)
    else:
        data = product_dao.get_all_products_based_category(category)
        if len(data) != 0:
            return make_response({"products": data}, 200)
        else:
            return make_response({"msg": "No products found"}, 400)


@app.route('/api/a3/user/reviews')
@jwt_required()
def get_reviews_by_user():
    user_id = get_jwt_identity().get('userId')
    product_review_dao = ReviewsRatingsDAO()
    data = product_review_dao.get_reviews_by_user(user_id)
    if len(data) != 0:
        return make_response({"reviews": data}, 200)
    else:
        return make_response({"msg": "No reviews found"}, 400)


@app.route('/api/a3/user/ratings')
@jwt_required()
def get_ratings_by_user():
    user_id = get_jwt_identity().get('userId')
    product_rating_dao = ReviewsRatingsDAO()
    data = product_rating_dao.get_ratings_by_user(user_id)
    if len(data) != 0:
        return make_response({"ratings": data}, 200)
    else:
        return make_response({"msg": "No ratings found"}, 400)
