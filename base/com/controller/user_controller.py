import datetime
import base64
import sqlalchemy
from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.dao.product_dao import ProductReviewsRatingsDAO
from base.com.dao.user_dao import UserInfoDAO, UserProfilePictureDAO
from base.com.vo.user_vo import UserInfoVO, UserProfilePictureVO

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
    if request.method == 'GET':
        user_info_dao = UserInfoDAO()
        user_id = get_jwt_identity().get('userId')
        data = user_info_dao.get_user_profile(user_id)
        if data:
            return make_response({"profile": data}, 200)
        else:
            return make_response({"msg": "No record found"}, 400)

    elif request.method == 'PUT':
        try:
            user_info_dao = UserInfoDAO()
            user_info_vo = UserInfoVO()
            user_id = get_jwt_identity().get('userId')
            user_info_id = request.args.get('userInfoId')

            user_info_vo.user_first_name = request.json.get('firstName')
            user_info_vo.user_last_name = request.json.get('lastName')
            user_info_vo.user_mobile = request.json.get('mobile')
            user_info_vo.user_dob = request.json.get('dob')
            user_info_vo.user_id = user_id
            user_info_vo.updated_at = datetime.datetime.utcnow()
            if not user_info_id:
                user_info_dao.add_user_profile(user_info_vo)
                return make_response({"msg": "Profile successfully added"}, 201)
            elif user_info_id:
                user_info_vo.user_info_id = user_info_id
                user_info_dao.update_user_profile(user_info_vo)
                return make_response({"msg": "Profile successfully updated"}, 201)
        except sqlalchemy.exc.IntegrityError as e:
            return make_response({"msg": "Error occured while inserting data"}, 400)
        except Exception as e:
            return make_response({"msg": "Something went wrong, try again"}, 400)


@app.route(f'{user_api_path}/profile-pic', methods=['GET', 'PUT'])
@jwt_required()
def user_profile_pic():
    user_id = get_jwt_identity().get('userId')
    user_profile_pic_dao = UserProfilePictureDAO()
    user_profile_pic_vo = UserProfilePictureVO()

    if request.method == 'GET':
        try:
            profile_pic = user_profile_pic_dao.get_user_profile_pic(user_id)
            if profile_pic:
                encoded_data = base64.b64encode(
                    profile_pic['userProfileDataUrl']).decode()
                profile_pic['userProfileDataUrl'] = f'data:image/png;base64,{encoded_data}'
                return make_response(profile_pic, 200)
            else:
                return make_response({"msg": "No record found"}, 400)
        except Exception as e:
            return make_response({"msg": "Some error occured, please try again"}, 400)

    if request.method == 'PUT':
        try:
            user_profile_pic_vo.user_id = user_id
            user_profile_pic_vo.updated_at = datetime.datetime.utcnow()

            user_profile_data_url = request.json.get(
                'profilePic')
            encoded_data = base64.b64decode(
                user_profile_data_url.split(',')[1])
            user_profile_pic_vo.user_profile_data_url = encoded_data

            user_profile_pic_dao.add_user_profile_pic(user_profile_pic_vo)
            return make_response({"msg": "Profile picture successfully added"}, 201)
        except Exception as e:
            return make_response({"msg": "Something went wrong, try again"}, 400)
