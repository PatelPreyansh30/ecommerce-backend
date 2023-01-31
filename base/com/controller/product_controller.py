from base import app
from base.com.vo.product_vo import ProductVO
from base.com.dao.product_dao import ProductDAO
from flask_jwt_extended import jwt_required
from flask import make_response

@app.route('/api/a3/products')
@jwt_required()
def get_products():
    product_dao = ProductDAO()
    prod_obj_list = product_dao.get_all_products()
    all_products = list(map(ProductVO.as_dict, prod_obj_list))
    return make_response({"products":all_products}, 200)