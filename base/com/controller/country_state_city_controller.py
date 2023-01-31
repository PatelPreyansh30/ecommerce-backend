from flask import request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.dao.address_dao import CountryDAO, StateDAO, CityDAO
from base.com.vo.address_vo import CountryVO, StateVO, CityVO

country_state_city_api_path = '/api/a2/location'


@app.route(f'{country_state_city_api_path}/countries', methods=['GET'])
@jwt_required()
def get_country():
    country_dao = CountryDAO()

    data = country_dao.get_countries()
    if len(data) != 0:
        return make_response({"countries": data}, 200)
    else:
        return make_response({"msg": f"No country found"}, 404)


@app.route(f'{country_state_city_api_path}/states', methods=['GET'])
@jwt_required()
def get_states():
    state_dao = StateDAO()

    country_iso_code = request.args.get('country')

    if not country_iso_code:
        return make_response({"msg": "Query param not correct"}, 400)
    else:
        data = state_dao.get_state_based_on_country(country_iso_code)
        if len(data) != 0:
            return make_response({"states": data}, 200)
        else:
            return make_response({"msg": f"No states found"}, 400)


@app.route(f'{country_state_city_api_path}/cities', methods=['GET'])
@jwt_required()
def get_cities():
    city_dao = CityDAO()
    state_iso_code = request.args.get('state')

    if not state_iso_code:
        return make_response({"msg": "Query param not correct"}, 400)
    else:
        data = city_dao.get_citie_based_on_state(state_iso_code)
        if len(data) != 0:
            return make_response({"cities": data}, 200)
        else:
            return make_response({"msg": f"No cities found"}, 400)
