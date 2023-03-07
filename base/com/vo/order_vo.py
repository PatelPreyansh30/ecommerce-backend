from datetime import datetime
from base import app, db
from base.com.vo.auth_vo import UserVO
from base.com.vo.product_vo import ProductVO


class OrderDetailVO(db.Model):
    __tablename__ = 'order_detail_table'
    order_detail_id = db.Column(
        'order_detail_id', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # payment_id = db.Column('payment_id', db.ForeignKey(), nullable=False)
    total = db.Column('total', db.Integer, nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.utcnow, nullable=False)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'orderDetailId': self.order_detail_id,
            'userId': self.user_id,
            # 'payment_id': self.payment_id,
            'total': self.total
        }


class OrderItemVO(db.Model):
    __tablename__ = 'order_item_table'
    order_item_id = db.Column(
        'order_item_id', db.Integer, primary_key=True, autoincrement=True)
    order_detail_id = db.Column('order_detail_id', db.ForeignKey(
        OrderDetailVO.order_detail_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id = db.Column('product_id', db.ForeignKey(
        ProductVO.product_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    quantity = db.Column('quantity', db.Integer, nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.utcnow, nullable=False)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'orderItemId': self.order_item_id,
            'productId': self.product_id,
            'quantity': self.quantity
        }


class CartVO(db.Model):
    __tablename__ = 'cart_table'
    cart_id = db.Column('cart_id', db.Integer,
                        primary_key=True, autoincrement=True)
    quantity = db.Column('quantity', db.Integer, nullable=False)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id = db.Column('product_id', db.ForeignKey(
        ProductVO.product_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.utcnow, nullable=False)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'cartId': self.cart_id,
            'quantity': self.quantity,
            'productId': self.product_id
        }

with app.app_context():
    db.create_all()
