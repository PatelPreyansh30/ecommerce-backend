import json
from base import db
from base.com.vo.address_vo import DeliveryAddressVO, CountryVO, StateVO, CityVO


class DeliveryAddressDAO():
    def add_address(self, address_object):
        db.session.add(address_object)
        db.session.commit()

    def get_user_addresses(self, user_id):
        all_data = DeliveryAddressVO.query.filter_by(user_id=user_id).all()
        return [data.as_dict() for data in all_data]

    def get_user_specific_address(self, address_id, user_id):
        data = DeliveryAddressVO.query.filter_by(
            address_id=address_id, user_id=user_id).first()
        return data.as_dict()

    def delete_user_specific_address(self, address_id, user_id):
        user_obj = DeliveryAddressVO.query.filter_by(
            address_id=address_id, user_id=user_id).first()
        db.session.delete(user_obj)
        db.session.commit()

    def update_user_specific_address(self, address_obj):
        db.session.merge(address_obj)
        db.session.commit()


class CountryDAO():
    def get_countries(self):
        countries = CountryVO.query.all()
        return [data.as_dict() for data in countries]


class StateDAO():
    def get_states(self):
        states = StateVO.query.all()
        return [data.as_dict() for data in states]

    def get_state_based_on_country(self, country_id):
        states = StateVO.query.filter_by(country_id=country_id).all()
        return [data.as_dict() for data in states]


class CityDAO():
    def get_cities(self):
        countries = CountryVO.query.all()
        return [data.as_dict() for data in countries]

    def get_citie_based_on_state(self, state_id):
        cities = CityVO.query.filter_by(state_id=state_id).all()
        return [data.as_dict() for data in cities]

    def get_citie_based_on_country(self, country_id):
        cities = CityVO.query.filter_by(country_id=country_id).all()
        return [data.as_dict() for data in cities]
