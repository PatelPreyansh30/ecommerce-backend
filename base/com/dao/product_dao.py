from base import db
from base.com.vo.product_vo import ProductVO, ProductCategoryVO, ProductSubCategoryVO, ProductInventoryVO, ProductReviewRatings


class ProductDAO():
    def get_all_products(self):
        products = ProductVO.query.all()
        datas = db.session.query(ProductVO, ProductCategoryVO,
                                 ProductSubCategoryVO, ProductInventoryVO, ProductReviewRatings).join(
                                     ProductCategoryVO, ProductVO.product_category_id == ProductCategoryVO.product_category_id
        ).join(
            ProductSubCategoryVO, ProductVO.product_subcategory_id == ProductSubCategoryVO.product_subcategory_id
        ).join(
            ProductInventoryVO, ProductVO.product_inventory_id == ProductInventoryVO.product_inventory_id
        ).join(
            ProductReviewRatings, ProductVO.product_review_id == ProductReviewRatings.product_review_rating_id
        ).all()
        dataList = []
        for i in datas:
            datadict={}
            datadict.update(i[0].as_dict())
            datadict.update(i[1].as_dict())
            datadict.update(i[2].as_dict())
            datadict.update(i[3].as_dict())
            datadict.update(i[4].as_dict())
            dataList.append(datadict)
        return dataList
    
    
class ReviewsDAO():
    def get_reviews_by_user(self, user_id):
        reviews = ProductReviewRatings.query.filter_by(user_id=user_id).all()
        return [review.as_dict() for review in reviews]
