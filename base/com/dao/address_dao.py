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
    def get_state_based_on_country(self, country_iso_code):
        states = db.session.query(StateVO, CountryVO).join(
            CountryVO, StateVO.country_iso_code == CountryVO.country_iso_code).filter_by(country_iso_code=country_iso_code).all()
        return states


class CityDAO():
    def get_citie_based_on_state(self, state_iso_code):
        cities = db.session.query(CountryVO, StateVO, CityVO).join(
            StateVO, CountryVO.country_iso_code == StateVO.country_iso_code).join(
                CityVO, CityVO.state_iso_code == StateVO.state_iso_code).filter(CityVO.state_iso_code == state_iso_code).all()
        return cities
