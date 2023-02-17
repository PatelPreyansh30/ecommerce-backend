from flask import request, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from base import app
from base.com.dao.auth_dao import UserDAO
from base.com.vo.auth_vo import UserVO

auth_api_path = "/api/a1/auth"


@app.route(f'{auth_api_path}/register', methods=['POST'])
def auth_register():
    email = request.json.get("email")
    password = request.json.get('password')

    if not email or not password:
        return make_response({"msg": "Invalid data"}, 400)
    else:
        user_dao = UserDAO()
        user_vo = UserVO()
        user_vo.user_email = email
        user_vo.user_password = generate_password_hash(password)

        try:
            existing_user = user_dao.get_single_user(email)
            user_dao.add_user(user_vo)
            return make_response({"msg": "Successfully added"}, 201)
        except Exception as e:
            return make_response({"msg": "Email already exists"}, 400)


@app.route(f'{auth_api_path}/login', methods=['POST'])
def auth_login():
    email = request.json.get("email")
    password = request.json.get('password')

    if not email or not password:
        return make_response({"msg": "Invalid data"}, 400)
    else:
        user_dao = UserDAO()

        existing_user = user_dao.get_single_user(email)
        if not existing_user == None:
            isPasswordTrue = check_password_hash(
                existing_user.user_password, password)
            if isPasswordTrue:
                access_token = create_access_token(
                    identity={"email": email, "userId": existing_user.user_id})
                refresh_token = create_refresh_token(
                    identity={"email": email, "userId": existing_user.user_id})

                return make_response({"accessToken": access_token, "refreshToken": refresh_token, "user": {"email": existing_user.user_email, "user_id": existing_user.user_id}}, 201)
            else:
                return make_response({"msg": "Invalid credential"}, 400)
        else:
            return make_response({"msg": "User doesn't exists"}, 400)


@app.route(f'{auth_api_path}/get-access-token', methods=['GET'])
@jwt_required(refresh=True)
def get_access_token():
    user_dao = UserDAO()
    identity = get_jwt_identity()
    user = user_dao.get_single_user(identity.get('email'))
    if user:
        access_token = create_access_token(identity=identity)
        return make_response({"accessToken": access_token, "user": identity}, 201)
    return make_response({"msg": "User doesn't exists"}, 401)
