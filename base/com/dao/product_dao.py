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
            data_dict['avgRating'] = avg_rating
            data_list.append(data_dict)
        return data_list
    
    def get_top_products_based_rating(self, category_id):
        products = ProductVO.query.filter_by(
            product_category_id=category_id).all()
        data_list = []
        for product in products:
            data_dict = {}
            data_dict.update(product.as_dict())
            avg_rating = db.session.query(func.avg(ProductRatingVO.product_rating)).filter_by(
                product_id=product.product_id).scalar()
            avg_rating = 0 if not avg_rating else avg_rating
            data_dict['avgRating'] = avg_rating
            data_list.append(data_dict)
        data_list = sorted(data_list, key=lambda d: d['avgRating'], reverse=True)[:4]
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
    def get_reviews_ratings_by_user(self, user_id):
        reviews = db.session.query(ProductReviewVO, ProductRatingVO, ProductVO).join(
            ProductRatingVO, ProductReviewVO.product_rating_id == ProductRatingVO.product_rating_id
        ).join(
            ProductVO, ProductReviewVO.product_id == ProductVO.product_id
        ).filter(ProductReviewVO.user_id == user_id).all()
        data_list = []
        for review in reviews:
            data_dict = {}
            data_dict.update(review[0].as_dict())
            data_dict.update(review[1].as_dict())
            data_dict.update(review[2].as_dict())
            data_list.append(data_dict)
        return data_list

    def get_reviews_ratings_by_product(self, product_id):
        reviews = db.session.query(ProductReviewVO, ProductRatingVO).join(
            ProductRatingVO, ProductReviewVO.product_rating_id == ProductRatingVO.product_rating_id
        ).filter_by(product_id=product_id).all()
        print(reviews)
        data_list = []
        for review in reviews:
            data_dict = {}
            data_dict.update(review[0].as_dict())
            data_dict.update(review[1].as_dict())
            data_list.append(data_dict)
        return data_list
