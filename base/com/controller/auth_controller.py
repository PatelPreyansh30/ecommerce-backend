from flask import request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from base import app
from base.com.dao.auth_dao import UserDAO, RefreshTokenDAO
from base.com.vo.auth_vo import UserVO, RefreshTokenVO

@app.route('/api/a1/auth/register', methods=['POST'])
def auth_register():
    email = request.json.get("email")
    password = request.json.get('password')
        
    if not email or not password:
        return make_response({"message": "Invalid data"}, 400)
    else:
        user_dao = UserDAO()
        user_vo = UserVO()
            
        user_vo.user_email = email
        user_vo.user_password = generate_password_hash(password)
            
        try:
            existing_user = user_dao.get_single_user(email)
            user_dao.add_user(user_vo)
            return make_response({"message": "Successfully added"}, 201)
            
        except Exception as e:
            return make_response({"message": "Email already exists"}, 400)

@app.route('/api/a1/auth/login', methods=['POST'])
def auth_login():
    email = request.json.get("email")
    password = request.json.get('password')
    
    if not email or not password:
        return make_response({"message": "Invalid data"}, 400)
    else:
        user_dao = UserDAO()

        existing_user = user_dao.get_single_user(email)
        if not existing_user == None:
            isPasswordTrue = check_password_hash(existing_user.user_password, password)
            if isPasswordTrue:
                
                access_token = create_access_token(identity=email)
                refresh_token = create_refresh_token(identity=email)
                refresh_token_dao = RefreshTokenDAO()
                refresh_token_vo = RefreshTokenVO()
                
                refresh_token_vo.refresh_token = refresh_token
                refresh_token_vo.refresh_user_id = existing_user.user_id
                
                try:
                    refresh_token_dao.add_refresh_token(refresh_token_vo)
                    return make_response({"accessToken": access_token, "refreshToken": refresh_token}, 201)
                except:
                    return make_response({"message": "Some error occured while storing the refresh token"}, 400)    
            else:
                return make_response({"message": "Invalid credential"}, 400)
            
        else:
            return make_response({"message": "User doesn't exists"}, 400)

@app.route('/api/a1/auth/get-access-token', methods=['POST'])
@jwt_required(refresh=True)
def get_access_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return make_response({"accessToken": access_token}, 201)