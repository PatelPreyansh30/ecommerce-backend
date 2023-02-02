from base import app
from base.com.vo.product_vo import ProductVO
from base.com.dao.product_dao import ProductDAO, ReviewsDAO
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import make_response


@app.route('/api/a3/products')
@jwt_required()
def get_products():
    product_dao = ProductDAO()
    data = product_dao.get_all_products()
    if len(data) != 0:
        return make_response({"products": data}, 200)
    else:
        return make_response({"msg": "No products found"}, 400)


@app.route('/api/a3/user/reviews')
@jwt_required()
def get_reviews_by_user():
    user_id = get_jwt_identity().get('userId')
    product_review_dao = ReviewsDAO()
    data = product_review_dao.get_reviews_by_user(user_id)
    if len(data) != 0:
        return make_response({"reviews": data}, 200)
    else:
        return make_response({"msg": "No reviews found"}, 400) 