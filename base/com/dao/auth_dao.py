import datetime
from werkzeug.security import generate_password_hash
from base import db
from base.com.vo.auth_vo import UserVO


class UserDAO():
    def add_user(self, user_object):
        db.session.add(user_object)
        db.session.commit()

    def get_single_user(self, user_email):
        user_object = UserVO.query.filter_by(user_email=user_email).first()
        return user_object

    def update_password_with_user(self, user_id, user_new_password):
        updation = UserVO.query.filter_by(user_id=user_id).update({
            UserVO.user_password: generate_password_hash(user_new_password),
            UserVO.updated_at: datetime.datetime.utcnow()
        })
        db.session.commit()
        return False if updation == 0 else True
