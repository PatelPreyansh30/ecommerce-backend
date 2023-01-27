from flask import request, make_response
from base import app


@app.route('/api/a1/auth/register', methods=['POST'])
def auth_register():
    email = request.json.get("email")
    password = request.json.get('password')
    if not email or not password:
        return make_response({"message": "Invalid data", "statusCode": 400}, 400)
    else:
        return make_response({"message": "Successfully added", "statusCode": 201}, 201)