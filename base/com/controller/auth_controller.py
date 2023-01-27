from flask import request, make_response
from base import app
from base.com.dao.auth_dao import UserDAO
from base.com.vo.auth_vo import UserVO


@app.route('/api/a1/auth/register', methods=['POST'])
def auth_register():
    email = request.json.get("email")
    password = request.json.get('password')
    
    if not email or not password:
        return make_response({"message": "Invalid data", "statusCode": 400}, 400)
    else:
        user_dao = UserDAO()
        user_vo = UserVO()
        
        user_vo.user_email = email
        user_vo.user_password = password
        
        try:
            existing_user = user_dao.get_single_user(email)
            print(existing_user)
            user_dao.add_user(user_vo)
            return make_response({"message": "Successfully added", "statusCode": 201}, 201)
        
        except Exception as e:
            return make_response({"message": "Email already exists", "statusCode": 400}, 400)