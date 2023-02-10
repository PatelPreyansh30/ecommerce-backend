from base import db
from base.com.vo.user_vo import UserInfoVO, UserProfilePictureVO


class UserInfoDAO():
    def get_user_profile(self, user_id):
        user_info = UserInfoVO.query.filter_by(user_id=user_id).first()
        if not user_info:
            return None
        return user_info.as_dict()

    def add_user_profile(self, user_obj):
        db.session.add(user_obj)
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

    def add_user_profile_pic(self, user_obj):
        db.session.add(user_obj)
        db.session.commit()

    def update_user_profile_pic(self, user_obj):
        db.session.merge(user_obj)
        db.session.commit()
