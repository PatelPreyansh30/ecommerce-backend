import datetime
from base import db
from base.com.vo.order_vo import OrderDetailVO, OrderItemVO, CartVO
from base.com.vo.product_vo import ProductVO


class CartDAO():
    def get_user_cart(self, user_id):
        cart = db.session.query(CartVO, ProductVO).join(
            ProductVO, CartVO.product_id == ProductVO.product_id
        ).filter(CartVO.user_id==user_id).all()
        print(cart)
        data = []
        for item in cart:
            cart_object = {}
            cart_object.update(item[0].as_dict())
            cart_object.update(item[1].as_dict())
            data.append(cart_object)
        return data
