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
        updation = UserInfoVO.query.filter_by(user_id=user_id).update({
            UserInfoVO.user_first_name: first_name,
            UserInfoVO.user_last_name: last_name,
            UserInfoVO.user_dob: dob,
            UserInfoVO.user_mobile: mobile,
            UserInfoVO.user_id: user_id,
            UserInfoVO.updated_at: datetime.datetime.utcnow()
        })
        if updation == 0:
            user_info = UserInfoVO(
                user_first_name=first_name,
                user_last_name=last_name,
                user_dob=dob,
                user_mobile=mobile,
                user_id=user_id,
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow()
            )
            db.session.add(user_info)
        db.session.commit()


class UserProfilePictureDAO():
    def get_user_profile_pic(self, user_id):
        user_profile_pic = UserProfilePictureVO.query.filter_by(
            user_id=user_id).first()
        if not user_profile_pic:
            return None
        return user_profile_pic.as_dict()

    def add_user_profile_pic(self, user_id, encoded_profile_pic):
        updation = UserProfilePictureVO.query.filter_by(user_id=user_id).update({
            UserProfilePictureVO.user_profile_data_url: encoded_profile_pic,
            UserProfilePictureVO.user_id: user_id,
            UserProfilePictureVO.updated_at: datetime.datetime.utcnow(),
        })
        if updation == 0:
            user_profile_pic = UserProfilePictureVO(
                user_profile_data_url=encoded_profile_pic,
                user_id=user_id,
                updated_at=datetime.datetime.utcnow(),
                created_at=datetime.datetime.utcnow(),
            )
            db.session.add(user_profile_pic)
        db.session.commit()
