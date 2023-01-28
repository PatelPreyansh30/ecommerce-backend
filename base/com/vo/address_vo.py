import datetime
from base import db, app
from base.com.vo.auth_vo import UserVO


class DeliveryAddressVO(db.Model):
    __tablename__ = 'address_table'
    address_id = db.Column('address_id', db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column('user_id', db.ForeignKey(UserVO.user_id, ondelete= 'CASCADE', onupdate= 'CASCADE'), nullable=False)
    name = db.Column('name', db.String(250), nullable=False)
    address_line1 = db.Column('address_line1', db.Text, nullable=False)
    address_line2 = db.Column('address_line2', db.Text, nullable=False)
    city = db.Column('city', db.String(250), nullable=False)
    postal_code = db.Column('postal_code', db.String(250), nullable=False)
    country = db.Column('country', db.String(250), nullable=False)
    mobile = db.Column('mobile', db.String(250), nullable=False)
    created_at = db.Column('created_at', db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime, default=datetime.datetime.utcnow)
    deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'name': self.name,
            'address_id': self.address_id,
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'city': self.city,
            'postal_code': self.postal_code,
            'country': self.country,
            'mobile': self.mobile,
            'address_line2': self.address_line2,
            # 'created_at': self.created_at,
            # 'updated_at': self.updated_at,
            # 'deleted_at': self.deleted_at
        }
        
with app.app_context():
    db.create_all()