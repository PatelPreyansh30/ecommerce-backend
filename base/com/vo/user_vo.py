import datetime
from base import db, app
from base.com.vo.auth_vo import UserVO


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
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.datetime.utcnow)

    def as_dict(self):
        return {
            'userInfoId': self.user_info_id,
            'firstName': self.user_first_name,
            'lastName': self.user_last_name,
            'dob': self.user_dob,
            'mobile': self.user_mobile,
        }


with app.app_context():
    db.create_all()
