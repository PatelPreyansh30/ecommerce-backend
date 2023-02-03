from sqlalchemy import func
from base import db
from base.com.vo.product_vo import ProductVO, ProductCategoryVO, ProductSubCategoryVO, ProductInventoryVO, ProductReviewVO, ProductRatingVO


class ProductCategoryDAO():
    def get_category_id_based_category(self, category_name):
        category = ProductCategoryVO.query.filter_by(
            product_category_name=category_name).first()
        return category.product_category_id

    def get_all_categories(self):
        categories = ProductCategoryVO.query.all()
        return [category.as_dict() for category in categories]

    def get_subcategory_based_category(self, category_id):
        subcategories = ProductSubCategoryVO.query.filter_by(
            product_category_id=category_id).all()
        return [subcategory.as_dict() for subcategory in subcategories]


class ProductDAO():
    def get_all_products_based_category(self, category_id):
        products = ProductVO.query.filter_by(
            product_category_id=category_id).all()
        data_list = []
        for product in products:
            data_dict = {}
            data_dict.update(product.as_dict())
            avg_rating = db.session.query(func.avg(ProductRatingVO.product_rating)).filter_by(
                product_id=product.product_id).scalar()
            avg_rating = 0 if not avg_rating else avg_rating
            data_dict['avg_rating'] = avg_rating
            data_list.append(data_dict)
        return data_list

    def get_single_product(self, product_id):
        product = db.session.query(ProductVO, ProductCategoryVO, ProductSubCategoryVO,
                                   ProductInventoryVO).join(
            ProductCategoryVO, ProductVO.product_category_id == ProductCategoryVO.product_category_id
        ).join(
            ProductSubCategoryVO, ProductVO.product_subcategory_id == ProductSubCategoryVO.product_subcategory_id
        ).join(
            ProductInventoryVO, ProductVO.product_inventory_id == ProductInventoryVO.product_inventory_id
        ).filter(ProductVO.product_id == product_id).first()

        data_dict = {}
        for item in product:
            data_dict.update(item.as_dict())
        return data_dict


class ProductReviewsRatingsDAO():
    def get_reviews_by_user(self, user_id):
        reviews = ProductReviewVO.query.filter_by(user_id=user_id).all()
        return [review.as_dict() for review in reviews]

    def get_ratings_by_user(self, user_id):
        ratings = ProductRatingVO.query.filter_by(user_id=user_id).all()
        return [rating.as_dict() for rating in ratings]
