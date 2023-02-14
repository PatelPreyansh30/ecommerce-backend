import datetime
from base import db, app
from base.com.vo.auth_vo import UserVO


class DeliveryAddressVO(db.Model):
    __tablename__ = 'address_table'
    address_id = db.Column('address_id', db.Integer,
                           primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    name = db.Column('name', db.String(255), nullable=False)
    address_line1 = db.Column('address_line1', db.Text, nullable=False)
    address_line2 = db.Column('address_line2', db.Text, nullable=False)
    area = db.Column('area', db.String(255), nullable=False)
    city = db.Column('city', db.String(255), nullable=False)
    state = db.Column('state', db.String(255), nullable=False)
    country = db.Column('country', db.String(255), nullable=False)
    postal_code = db.Column('postal_code', db.String(255), nullable=False)
    mobile = db.Column('mobile', db.String(255), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'name': self.name,
            'addressId': self.address_id,
            'line1': self.address_line1,
            'line2': self.address_line2,
            'area': self.area,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'postalCode': self.postal_code,
            'mobile': self.mobile,
        }


class CountryVO(db.Model):
    __tablename__ = 'country_table'
    country_id = db.Column('country_id', db.Integer,
                           primary_key=True, autoincrement=True)
    country_name = db.Column('country_name', db.String(
        255), nullable=False, unique=True)

    def as_dict(self):
        return self.country_name


class StateVO(db.Model):
    __tablename__ = 'state_table'
    state_id = db.Column('state_id', db.Integer,
                         primary_key=True, autoincrement=True)
    state_name = db.Column('state_name', db.String(255), nullable=False, unique=True)
    country_name = db.Column('country_name', db.ForeignKey(CountryVO.country_name, ondelete='CASCADE', onupdate='CASCADE'),
                             nullable=False)

    def as_dict(self):
        return self.state_name


class CityVO(db.Model):
    __tablename__ = 'city_table'
    city_id = db.Column('city_id', db.Integer,
                        primary_key=True, autoincrement=True)
    city_name = db.Column('city_name', db.String(255),
                          nullable=False, unique=True)
    state_name = db.Column('state_name', db.ForeignKey(StateVO.state_name, ondelete='CASCADE', onupdate='CASCADE'),
                           nullable=False)

    def as_dict(self):
        return self.city_name


with app.app_context():
    db.create_all()
