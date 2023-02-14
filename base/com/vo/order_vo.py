from datetime import datetime
from base import app, db
from base.com.vo.auth_vo import UserVO
from base.com.vo.product_vo import ProductVO


class OrderDetailVO(db.Model):
    __tablename__ = 'order_detail_table'
    order_detail_id = db.Column(
        'order_detail_id', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    # payment_id = db.Column('payment_id', db.ForeignKey(), nullable=False)
    total = db.Column('total', db.Integer, nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.utcnow, nullable=True)
    updated_at = db.Column('updated_at', db.Integer,
                           default=datetime.utcnow, nullable=True)

    def as_dict(self):
        return {
            'orderDetailId': order_detail_id,
            'userId': user_id,
            # 'payment_id': payment_id,
            'total': total
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
    updated_at = db.Column('updated_at', db.Integer,
                           default=datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'orderItemId': order_item_id,
            'orderDetailId': order_detail_id,
            'productId': product_id,
            'quantity': quantity
        }


with app.app_context():
    db.create_all()
