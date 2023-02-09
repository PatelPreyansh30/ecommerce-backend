from base import db
from base.com.vo.user_vo import UserInfoVO


class UserInfoDAO():
    def get_user_profile(self, user_id):
        user_info = UserInfoVO.query.filter_by(user_id=user_id).first()
        if not user_info:
            return None
        return user_info.as_dict()

    def add_user_profile(self, user_obj):
        db.session.add(user_obj)
        db.session.commit()