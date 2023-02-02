from base import app
from base.com.vo.product_vo import ProductVO
from base.com.dao.product_dao import ProductDAO
from flask_jwt_extended import jwt_required
from flask import make_response

@app.route('/api/a3/products')
@jwt_required()
def get_products():
    product_dao = ProductDAO()
    data = product_dao.get_all_products()
    if len(data) != 0:
        return make_response({"products":data}, 200)
    else:
        return make_response({"msg":"No products found"}, 400)