from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import sqlalchemy
from base import app
from base.com.dao.product_dao import ProductReviewsRatingsDAO
from base.com.dao.user_dao import UserInfoDAO
from base.com.vo.user_vo import UserInfoVO

user_api_path = '/api/a4/user'


@app.route(f'{user_api_path}/reviews')
@jwt_required()
def get_reviews_by_user():
    product_review_dao = ProductReviewsRatingsDAO()
    user_id = get_jwt_identity().get('userId')
    data = product_review_dao.get_reviews_ratings_by_user(user_id)
    if len(data) != 0:
        return make_response({"reviews": data}, 200)
    else:
        return make_response({"msg": "No reviews found"}, 400)


@app.route(f'{user_api_path}/profile', methods=['GET', 'POST'])
@jwt_required()
def get_user_profile():
    if request.method == 'GET':
        user_info_dao = UserInfoDAO()
        user_id = get_jwt_identity().get('userId')
        data = user_info_dao.get_user_profile(user_id)
        if data:
            return make_response({"profile": data}, 200)
        else:
            return make_response({"msg": "No record found"}, 400)
    elif request.method == 'POST':
        try:
            user_info_dao = UserInfoDAO()
            user_info_vo = UserInfoVO()
            user_id = get_jwt_identity().get('userId')

            user_info_vo.user_first_name = request.json.get('firstName')
            user_info_vo.user_last_name = request.json.get('lastName')
            user_info_vo.user_mobile = request.json.get('mobile')
            user_info_vo.user_dob = request.json.get('dob')
            user_info_vo.user_id = user_id

            user_info_dao.add_user_profile(user_info_vo)
            return make_response({"msg": "Profile successfully aaded"}, 201)
        except sqlalchemy.exc.IntegrityError as e:
            return make_response({"msg": "Error occured while inserting data"}, 400)
        except Exception as e:
            return make_response({"msg": "Something went wrong, try again"}, 400)
