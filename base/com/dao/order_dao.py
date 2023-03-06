from datetime import datetime
from base import db
from base.com.vo.order_vo import OrderDetailVO, OrderItemVO, CartVO
from base.com.vo.product_vo import ProductVO, ProductSubCategoryVO, ProductDiscountVO


class CartDAO():
    def get_user_cart(self, user_id):
        cart = db.session.query(CartVO, ProductVO, ProductSubCategoryVO, ProductDiscountVO).join(
            ProductVO, CartVO.product_id == ProductVO.product_id
        ).join(
            ProductSubCategoryVO, ProductVO.subcategory_id == ProductSubCategoryVO.subcategory_id
        ).join(
            ProductDiscountVO, ProductVO.discount_id == ProductDiscountVO.discount_id
        ).filter(CartVO.user_id == user_id).all()
        data = []
        for item in cart:
            cart_object = {}
            cart_object.update(item[0].as_dict())
            cart_object.update(item[1].as_dict())
            cart_object.update(item[2].as_dict())
            cart_object.update(item[3].as_dict())
            cart_object['isAddedInCart'] = True
            data.append(cart_object)
        return data

    def post_product_in_cart(self, product_id, quantity, user_id):
        cart_obj = CartVO(
            quantity=quantity,
            user_id=user_id,
            product_id=product_id
        )
        db.session.add(cart_obj)
        cart = db.session.query(CartVO, ProductVO, ProductSubCategoryVO, ProductDiscountVO).join(
            ProductVO, CartVO.product_id == ProductVO.product_id
        ).join(
            ProductSubCategoryVO, ProductVO.subcategory_id == ProductSubCategoryVO.subcategory_id
        ).join(
            ProductDiscountVO, ProductVO.discount_id == ProductDiscountVO.discount_id
        ).filter(CartVO.user_id == user_id, CartVO.product_id == product_id).all()

        if len(cart) > 1:
            return None
        data = {}
        for item in cart[0]:
            data.update(item.as_dict())
        db.session.commit()
        return data
