import datetime
import base64
from base import db, app
from base.com.vo.auth_vo import UserVO
from base.com.vo.product_vo import ProductVO


class UserInfoVO(db.Model):
    __tablename__ = 'user_info_table'
    user_info_id = db.Column('user_info_id', db.Integer,
                             primary_key=True, autoincrement=True)
    user_first_name = db.Column('user_first_name', db.String(255),
                                nullable=False)
    user_last_name = db.Column('user_last_name', db.String(255),
                               nullable=False)
    user_dob = db.Column('user_dob', db.Date,
                         nullable=False)
    user_mobile = db.Column('user_mobile', db.String(
        255), nullable=False, unique=True)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False, unique=True)
    user_profile_data_url = db.Column(
        'user_profile_data_url', db.LargeBinary(length=(2 * 1024 * 1024)), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'firstName': self.user_first_name,
            'lastName': self.user_last_name,
            'dob': self.user_dob,
            'mobile': self.user_mobile,
            'profilePic': f'''data: image/png;base64, {base64.b64encode(self.user_profile_data_url).decode()}''',
        }


class UserFavoriteVO(db.Model):
    __tablename__ = 'user_favorite_table'
    user_favorite_id = db.Column('user_favorite_id', db.Integer,
                                 primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id = db.Column('product_id', db.ForeignKey(
        ProductVO.product_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {'userFavoriteId': self.user_favorite_id}


with app.app_context():
    db.create_all()
