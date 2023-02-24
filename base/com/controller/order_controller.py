from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.dao.order_dao import CartDAO
from base.com.vo.order_vo import OrderDetailVO, OrderItemVO, CartVO

order_api_path = '/api/a6/order'


@app.route(f'{order_api_path}/cart', methods=['GET', 'POST'])
@jwt_required()
def get_cart_by_user():
    user_id = get_jwt_identity().get('userId')
    cart_dao = CartDAO()

    if request.method == 'GET':
        try:
            cart = cart_dao.get_user_cart(user_id)
            return make_response({'cart': cart}, 200)
        except Exception as e:
            print(e)
            return make_response({'msg': "Something went wrong"}, 400)