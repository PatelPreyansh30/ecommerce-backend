from base import db
from base.com.vo.product_vo import ProductVO

class ProductDAO():   

    def get_all_products(self):
        products = ProductVO.query.all()
        
        return products