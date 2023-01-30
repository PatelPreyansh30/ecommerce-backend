import datetime
from base import db, app


class UserVO(db.Model):
    __tablename__ = 'user_table'
    user_id = db.Column('user_id', db.Integer,
                        primary_key=True, autoincrement=True)
    user_email = db.Column('user_email', db.String(250),
                           nullable=False, unique=True)
    user_password = db.Column('user_password', db.String(250), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.datetime.utcnow)
    deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'user_id': self.user_id,
            'user_email': self.user_email
        }


with app.app_context():
    db.create_all()
