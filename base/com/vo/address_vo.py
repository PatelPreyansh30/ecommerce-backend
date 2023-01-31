import datetime
from base import db, app
from base.com.vo.auth_vo import UserVO


class DeliveryAddressVO(db.Model):
    __tablename__ = 'address_table'
    address_id = db.Column('address_id', db.Integer,
                           primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    name = db.Column('name', db.String(250), nullable=False)
    address_line1 = db.Column('address_line1', db.Text, nullable=False)
    address_line2 = db.Column('address_line2', db.Text, nullable=False)
    city = db.Column('city', db.String(250), nullable=False)
    postal_code = db.Column('postal_code', db.String(250), nullable=False)
    country = db.Column('country', db.String(250), nullable=False)
    mobile = db.Column('mobile', db.String(250), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.datetime.utcnow)
    deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'name': self.name,
            'address_id': self.address_id,
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'city': self.city,
            'postal_code': self.postal_code,
            'country': self.country,
            'mobile': self.mobile,
            'address_line2': self.address_line2,
        }


class CountryVO(db.Model):
    __tablename__ = 'country_table'
    country_id = db.Column('country_id', db.Integer,
                           primary_key=True, autoincrement=True)
    country_name = db.Column('country_name', db.String(255), nullable=False)
    country_iso_code = db.Column(
        'country_iso_code', db.String(255), nullable=False, unique=True)

    def as_dict(self):
        return {
            'country_id': self.country_id,
            'country_name': self.country_name,
            'country_iso_code': self.country_iso_code
        }


class StateVO(db.Model):
    __tablename__ = 'state_table'
    state_id = db.Column('state_id', db.Integer,
                         primary_key=True, autoincrement=True)
    state_name = db.Column('state_name', db.String(255), nullable=False)
    state_iso_code = db.Column('state_iso_code', db.String(
        255), nullable=False, unique=True)
    country_iso_code = db.Column('country_iso_code', db.ForeignKey(CountryVO.country_iso_code, ondelete='CASCADE', onupdate='CASCADE'),
                                 nullable=False)

    def as_dict(self):
        return {
            'state_id': self.state_id,
            'state_name': self.state_name,
            'country_iso_code': self.country_iso_code,
            'state_iso_code': self.state_iso_code
        }


class CityVO(db.Model):
    __tablename__ = 'city_table'
    city_id = db.Column('city_id', db.Integer,
                        primary_key=True, autoincrement=True)
    city_name = db.Column('city_name', db.String(255),
                          nullable=False, unique=True)
    state_iso_code = db.Column('state_iso_code', db.ForeignKey(StateVO.state_iso_code, ondelete='CASCADE', onupdate='CASCADE'),
                               nullable=False)

    def as_dict(self):
        return {
            'city_id': self.city_id,
            'city_name': self.city_name,
            'state_iso_code': self.state_iso_code
        }


with app.app_context():
    db.create_all()
