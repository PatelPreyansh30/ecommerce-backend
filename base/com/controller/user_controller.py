import base64
import sqlalchemy
from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.dao.product_dao import ProductReviewsRatingsDAO
from base.com.dao.user_dao import UserInfoDAO, UserFavoriteDAO, UserFavoriteVO
from base.com.dao.auth_dao import UserDAO

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

    if request.method == 'GET':
        try:
            profile_data = user_info_dao.get_user_profile(user_id)

            if profile_data:
                profile_data['dob'] = profile_data['dob'].strftime(f"%Y-%m-%d")
                encoded_data = base64.b64encode(
                    profile_data['profilePic']).decode()

                profile_data['profilePic'] = f'data:image/png;base64,{encoded_data}'
                return make_response(profile_data, 200)
            else:
                return make_response({"msg": "No record found"}, 400)
        except Exception as e:
            return make_response({"msg": "Something went wrong, try again"}, 400)

    elif request.method == 'PUT':
        try:
            first_name = request.json.get('firstName')
            last_name = request.json.get('lastName')
            mobile = request.json.get('mobile')
            dob = request.json.get('dob')
            profile_pic_base64 = request.json.get('profilePic')
            encoded_profile_pic = base64.b64decode(
                profile_pic_base64.split(',')[1])

            user_info_dao.add_user_profile(
                user_id, first_name, last_name, dob, mobile, encoded_profile_pic)
            return make_response({"msg": "Profile successfully added"}, 201)
        except sqlalchemy.exc.IntegrityError as e:
            return make_response({"msg": "Your profile already added"}, 400)
        except Exception as e:
            return make_response({"msg": "Something went wrong, try again"}, 400)


@app.route(f'{user_api_path}/update-password', methods=['PUT'])
@jwt_required()
def user_update_password():
    user_id = get_jwt_identity().get('userId')
    user_dao = UserDAO()

    if request.method == 'PUT':
        user_new_password = request.json.get('newPassword')
        updation_status = user_dao.update_password_with_user(
            user_id, user_new_password)

        if updation_status:
            return make_response({"msg": "Profile password successfully updated"}, 201)
        else:
            return make_response({"msg": "Error occured, Please try again"}, 400)


@app.route(f'{user_api_path}/favorites', methods=['GET', 'POST'])
@jwt_required()
def user_favorites():
    user_id = get_jwt_identity().get('userId')
    user_favorite_dao = UserFavoriteDAO()
    user_favorite_vo = UserFavoriteVO()
    if request.method == 'GET':
        data = user_favorite_dao.get_user_favorites(user_id)
        if len(data) != 0:
            return make_response({"favorites": data}, 200)
        else:
            return make_response({"msg": "No favorites found"}, 400)

    elif request.method == 'POST':
        product_id = request.json.get('productId')
        if not product_id:
            return make_response({"msg": "Invalid body"}, 400)
        else:
            try:
                res = user_favorite_dao.post_user_favorites(
                    user_id, product_id)
                if not res:
                    return make_response({'msg': 'Product already added'}, 400)
                return make_response({"favorite": res, "msg": "Successfully added in favorites"}, 201)
            # except sqlalchemy.exc.IntegrityError:
            #     return make_response({"msg": "Error while storing in database"}, 400)
            except Exception as e:
                print(e)
                return make_response({"msg": "Something went wrong, try again"}, 400)
