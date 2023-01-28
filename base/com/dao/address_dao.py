import json
from base import db
from base.com.vo.address_vo import DeliveryAddressVO


class DeliveryAddressDAO():

    def add_address(self, address_object):
        db.session.add(address_object)
        db.session.commit()
        
    def get_user_addresses(self, user_id):
        all_data = DeliveryAddressVO.query.filter_by(user_id = user_id).all()
        return [data.as_dict() for data in all_data]