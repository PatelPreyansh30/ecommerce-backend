from base import db
from base.com.vo.user_vo import UserInfoVO, UserProfilePictureVO
import datetime


class UserInfoDAO():
    def get_user_profile(self, user_id):
        user_info = UserInfoVO.query.filter_by(user_id=user_id).first()
        if not user_info:
            return None
        return user_info.as_dict()

    def add_user_profile(self, user_id, first_name, last_name, dob, mobile):
        UserInfoVO.query.filter_by(user_id=user_id).update({
            UserInfoVO.user_first_name: first_name,
            UserInfoVO.user_last_name: last_name,
            UserInfoVO.user_dob: dob,
            UserInfoVO.user_mobile: mobile,
            UserInfoVO.updated_at: datetime.datetime.utcnow()
        })
        db.session.commit()

    def update_user_profile(self, user_obj):
        db.session.merge(user_obj)
        db.session.commit()


class UserProfilePictureDAO():
    def get_user_profile_pic(self, user_id):
        user_profile_pic = UserProfilePictureVO.query.filter_by(
            user_id=user_id).first()
        if not user_profile_pic:
            return None
        return user_profile_pic.as_dict()

    def add_user_profile_pic(self, user_id, encoded_data):
        UserProfilePictureVO.query.filter_by(user_id=user_id).update({
            UserProfilePictureVO.user_profile_data_url: encoded_data,
            UserProfilePictureVO.updated_at: datetime.datetime.utcnow(),
        })
        db.session.commit()

    def update_user_profile_pic(self, user_obj):
        db.session.merge(user_obj)
        db.session.commit()
