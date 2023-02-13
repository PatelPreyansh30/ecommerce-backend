from base import db
from base.com.vo.user_vo import UserInfoVO
import datetime


class UserInfoDAO():
    def get_user_profile(self, user_id):
        user_info = UserInfoVO.query.filter_by(user_id=user_id).first()
        if not user_info:
            return None
        return user_info.as_dict()

    def add_user_profile(self, user_id, first_name, last_name, dob, mobile, encoded_profile_pic):
        updation = UserInfoVO.query.filter_by(user_id=user_id).update({
            UserInfoVO.user_first_name: first_name,
            UserInfoVO.user_last_name: last_name,
            UserInfoVO.user_dob: dob,
            UserInfoVO.user_mobile: mobile,
            UserInfoVO.user_profile_data_url: encoded_profile_pic,
            UserInfoVO.user_id: user_id,
            UserInfoVO.updated_at: datetime.datetime.utcnow()
        })
        if updation == 0:
            user_info = UserInfoVO(
                user_first_name=first_name,
                user_last_name=last_name,
                user_dob=dob,
                user_mobile=mobile,
                user_profile_data_url=encoded_profile_pic,
                user_id=user_id,
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow()
            )
            db.session.add(user_info)
        db.session.commit()
