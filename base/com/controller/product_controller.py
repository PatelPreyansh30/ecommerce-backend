from base import app
from base.com.vo.product_vo import ProductVO
from base.com.dao.product_dao import ProductDAO
from flask import jsonify,make_response

@app.route('/api/a1/products')
def get_products():
    product_dao = ProductDAO()
    prod_obj_list = product_dao.get_all_products()
    all_products = list(map(ProductVO.as_dict, prod_obj_list))
    return jsonify(all_products)