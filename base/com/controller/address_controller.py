from datetime import datetime
from flask import request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.exc import UnmappedInstanceError
from base import app
from base.com.dao.address_dao import DeliveryAddressDAO
from base.com.vo.address_vo import DeliveryAddressVO

address_api_path = '/api/a2'
specific_address_api_path = '/api/a2/address'


@app.route(f'{address_api_path}/addresses', methods=['GET', 'POST'])
@jwt_required()
def multiple_delivery_address():
    delivery_address_dao = DeliveryAddressDAO()
    delivery_address_vo = DeliveryAddressVO()
    user_id = get_jwt_identity().get('userId')

    if request.method == 'GET':
        data = delivery_address_dao.get_user_addresses(user_id)
        if len(data) != 0:
            return make_response({"addresses": data}, 200)
        else:
            return make_response({"msg": f"No addesses found for {user_id} user id"}, 404)

    elif request.method == 'POST':
        delivery_address_vo.user_id = user_id
        delivery_address_vo.name = request.json.get("name")
        delivery_address_vo.address_line1 = request.json.get("line1")
        delivery_address_vo.address_line2 = request.json.get("line2")
        delivery_address_vo.city = request.json.get("city")
        delivery_address_vo.postal_code = request.json.get("postalCode")
        delivery_address_vo.country = request.json.get("country")
        delivery_address_vo.mobile = request.json.get("mobile")

        delivery_address_dao.add_address(delivery_address_vo)
        return make_response({"msg": "Address added successfully"}, 201)


@app.route(f'{specific_address_api_path}/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@jwt_required()
def specific_delivery_address(id):
    user_id = get_jwt_identity().get('userId')
    delivery_address_dao = DeliveryAddressDAO()
    delivery_address_vo = DeliveryAddressVO()

    if request.method == 'GET':
        try:
            data = delivery_address_dao.get_user_specific_address(id, user_id)
            return make_response(data, 200)
        except AttributeError as e:
            return make_response({"msg": f"No addesses found for {id} id"}, 404)

    if request.method == 'DELETE':
        try:
            delivery_address_dao.delete_user_specific_address(id, user_id)
            return make_response({"msg": f"Address deleted successfully"}, 200)
        except UnmappedInstanceError as e:
            return make_response({"msg": f"No addesses found for {id} id"}, 404)

    if request.method == 'PUT':
        delivery_address_vo.address_id = id
        delivery_address_vo.user_id = user_id
        delivery_address_vo.name = request.json.get("name")
        delivery_address_vo.address_line1 = request.json.get("line1")
        delivery_address_vo.address_line2 = request.json.get("line2")
        delivery_address_vo.city = request.json.get("city")
        delivery_address_vo.postal_code = request.json.get("postalCode")
        delivery_address_vo.country = request.json.get("country")
        delivery_address_vo.mobile = request.json.get("mobile")
        delivery_address_vo.updated_at = datetime.utcnow()

        delivery_address_dao.update_user_specific_address(delivery_address_vo)
        return make_response({"msg": "Address updated successfully"}, 201)
