from flask import request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.dao.address_dao import DeliveryAddressDAO
from base.com.vo.address_vo import DeliveryAddressVO


@app.route('/api/a1/addresses', methods=['GET','POST'])
@jwt_required()
def delivery_address():
    if request.method == 'GET':
        delivery_address_dao = DeliveryAddressDAO()
        data = delivery_address_dao.get_user_addresses(get_jwt_identity().get('userId'))
        return make_response({"data": data}, 200)
        
    elif request.method == 'POST':
        delivery_address_dao = DeliveryAddressDAO()
        delivery_address_vo = DeliveryAddressVO()
        
        delivery_address_vo.user_id = get_jwt_identity().get('userId')
        delivery_address_vo.name = request.json.get("name")
        delivery_address_vo.address_line1 = request.json.get("line1")
        delivery_address_vo.address_line2 = request.json.get("line2")
        delivery_address_vo.city = request.json.get("city")
        delivery_address_vo.postal_code = request.json.get("postalCode")
        delivery_address_vo.country = request.json.get("country")
        delivery_address_vo.mobile = request.json.get("mobile")
        
        delivery_address_dao.add_address(delivery_address_vo)
        return make_response({"msg": "Address added successfully"}, 201)
    
        