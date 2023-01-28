from base import db, app


class UserVO(db.Model):
    __tablename__ = 'user_table'
    user_id = db.Column('user_id', db.Integer, primary_key = True, autoincrement = True)
    user_email = db.Column('user_email', db.String(250), nullable= False, unique= True)
    user_password = db.Column('user_password', db.String(250), nullable= False)

    def as_dict(self):
        return {
            'user_id': self.user_id,
            'user_email': self.user_email,
            'user_password': self.user_password
        }

# class RefreshTokenVO(db.Model):
#     __tablename__ : 'user_refresh_token'
#     refresh_token_id = db.Column('refresh_token_id', db.Integer, primary_key = True, autoincrement = True)
#     refresh_token = db.Column('refresh_token', db.Text, nullable=False)
#     refresh_user_id = db.Column('refresh_user_id', db.ForeignKey(UserVO.user_id, ondelete= 'CASCADE', onupdate= 'CASCADE'), nullable= False, unique=True)

#     def as_dict(self):
#         return {
#             'refresh_token_id': self.refresh_token_id,
#             'refresh_token': self.refresh_token,
#             'refresh_user_id': self.refresh_user_id
#         }
        
with app.app_context():
    db.create_all()