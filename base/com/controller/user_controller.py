import datetime
from datetime import datetime
import base64
import sqlalchemy
from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.dao.product_dao import ProductReviewsRatingsDAO
from base.com.dao.user_dao import UserInfoDAO, UserProfilePictureDAO

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


@app.route(f'{user_api_path}/profile', methods=['GET', 'PUT'])
@jwt_required()
def user_profile():
    user_id = get_jwt_identity().get('userId')
    user_info_dao = UserInfoDAO()
    user_profile_pic_dao = UserProfilePictureDAO()

    if request.method == 'GET':
        try:
            profile_data = user_info_dao.get_user_profile(user_id)
            profile_pic = user_profile_pic_dao.get_user_profile_pic(user_id)
            print(len(profile_pic))
            if profile_data and profile_pic:
                profile_data['dob'] = profile_data['dob'].strftime(f"%Y-%m-%d")
                encoded_data = base64.b64encode(profile_pic).decode()

                profile_data['profilePicBase64'] = f'data:image/png;base64,{encoded_data}'
                return make_response(profile_data, 200)
            else:
                return make_response({"msg": "No record found"}, 400)
        except Exception as e:
            print(e)
            return make_response({"msg": "Something went wrong, try again"}, 400)

    elif request.method == 'PUT':
        try:
            first_name = request.json.get('firstName')
            last_name = request.json.get('lastName')
            mobile = request.json.get('mobile')
            dob = request.json.get('dob')
            profile_pic_base64 = request.json.get('profilePicBase64')
            encoded_profile_pic = base64.b64decode(
                profile_pic_base64.split(',')[1])

            user_profile_pic_dao.add_user_profile_pic(
                user_id, encoded_profile_pic)
            user_info_dao.add_user_profile(
                user_id, first_name, last_name, dob, mobile)
            return make_response({"msg": "Profile successfully added"}, 201)
        except sqlalchemy.exc.IntegrityError as e:
            print(e)
            return make_response({"msg": "Your profile already added"}, 400)
        except Exception as e:
            print(e)
            return make_response({"msg": "Something went wrong, try again"}, 400)
