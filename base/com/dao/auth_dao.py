from base import db
from base.com.vo.auth_vo import UserVO

class UserDAO():
    def add_user(self, user_object):
        db.session.add(user_object)
        db.session.commit()
        
    def get_single_user(self, user_email):
        user_object = UserVO.query.filter_by(user_email = user_email).first()
        return user_object
    

class RefreshTokenDAO():
    def add_refresh_token(self, refresh_token_obj):
        db.session.add(refresh_token_obj)
        db.session.commit()
    