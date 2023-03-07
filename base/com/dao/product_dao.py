from sqlalchemy import desc
import datetime
from base import db
from base.com.vo.product_vo import ProductVO, ProductCategoryVO, ProductSubCategoryVO, ProductInventoryVO, ProductDiscountVO, ProductReviewVO
from base.com.vo.user_vo import UserInfoVO, UserVO


class ProductCategoryDAO():
    def get_category_id_based_category(self, category_name):
        category = ProductCategoryVO.query.filter_by(
            category_name=category_name).first()
        return category.category_id

    def get_all_categories(self):
        categories = ProductCategoryVO.query.all()
        return [category.as_dict() for category in categories]

    def get_categories_for_header(self):
        categories = db.session.query(ProductCategoryVO).all()
        categories_data = []
        for category in categories:
            data_dict = {}
            data_dict['categoryName'] = category.category_name
            subcategories = ProductSubCategoryVO.query.filter_by(
                category_id=category.category_id).all()
            subcategories_data = []
            for subcategory in subcategories:
                subcategories_data.append(subcategory.subcategory_name)
            data_dict['subCategories'] = subcategories_data
            categories_data.append(data_dict)
        return categories_data

class ProductSubCategoryDAO():
    def get_subcategory_id_based_subcategory(self, subcategory_name):
        subcategory = ProductSubCategoryVO.query.filter_by(
            subcategory_name=subcategory_name).first()
        return subcategory.subcategory_id

    def get_subcategory_based_category(self, category_id):
        subcategories = ProductSubCategoryVO.query.filter_by(
            category_id=category_id).all()
        return [subcategory.as_dict() for subcategory in subcategories]

class ProductDAO():
    def get_all_products_based_category(self, category_id):
        products = db.session.query(ProductVO,ProductSubCategoryVO,ProductDiscountVO).join(
            ProductSubCategoryVO,ProductVO.subcategory_id == ProductSubCategoryVO.subcategory_id
        ).join(
            ProductDiscountVO,ProductVO.discount_id== ProductDiscountVO.discount_id
        ).filter(
           ProductVO.category_id==category_id).all()
        data_list = []
        for product in products:
            data_dict = {}
            data_dict.update(product[0].as_dict())
            data_dict.update(product[1].as_dict())
            data_dict.update(product[2].as_dict())
            data_list.append(data_dict)
        return data_list

    def get_all_products_based_subcategory(self, subcategory_id):
        products = ProductVO.query.filter_by(
            subcategory_id=subcategory_id).all()
        data_list = []
        for product in products:
            data_dict = {}
            data_dict.update(product.as_dict())
            data_list.append(data_dict)
        return data_list

    def get_top_products_based_rating(self, category_id):
        products = ProductVO.query.filter_by(
            category_id=category_id).order_by(desc(ProductVO.average_rating)).all()
        data_list = []
        for product in products:
            data_dict = {}
            data_dict.update(product.as_dict())
            data_list.append(data_dict)
        return data_list

    def get_single_product(self, product_id):
        product = db.session.query(ProductVO, ProductCategoryVO, ProductSubCategoryVO,
                                   ProductInventoryVO, ProductDiscountVO).join(
            ProductCategoryVO, ProductVO.category_id == ProductCategoryVO.category_id
        ).join(
            ProductSubCategoryVO, ProductVO.subcategory_id == ProductSubCategoryVO.subcategory_id
        ).join(
            ProductInventoryVO, ProductVO.inventory_id == ProductInventoryVO.inventory_id
        ).join(
            ProductDiscountVO, ProductVO.discount_id == ProductDiscountVO.discount_id
        ).filter(ProductVO.product_id == product_id).first()

        data_dict = {}
        for item in product:
            data_dict.update(item.as_dict())
        return data_dict


class ProductReviewsRatingsDAO():
    def get_reviews_ratings_by_user(self, user_id):
        reviews = db.session.query(ProductReviewVO, ProductVO).join(
            ProductVO, ProductReviewVO.product_id == ProductVO.product_id
        ).filter(ProductReviewVO.user_id == user_id).all()
        data_list = []
        for review in reviews:
            data_dict = {}
            data_dict.update(review[0].as_dict())
            data_dict.update(review[1].as_dict())
            data_list.append(data_dict)
        return data_list

    def get_reviews_ratings_by_product(self, product_id):
        reviews = db.session.query(ProductReviewVO, UserInfoVO).join(
            UserInfoVO, ProductReviewVO.user_id == UserInfoVO.user_id
        ).filter(ProductReviewVO.product_id == product_id).all()
        data_list = []
        for review in reviews:
            data_dict = {}
            data_dict.update(review[0].as_dict())
            data_dict.update(review[1].as_dict())
            data_list.append(data_dict)
        return data_list

    def add_product_review(self, user_id, product_id, review_msg, rating, rating_count, avg_rating):
        review = ProductReviewVO(
            review_msg=review_msg,
            rating=rating,
            product_id=product_id,
            user_id=user_id
        )
        updation_of_product = ProductVO.query.filter_by(product_id=product_id).update({
            ProductVO.product_id: product_id,
            ProductVO.average_rating: ((rating_count*avg_rating)+rating)/(rating_count+1),
            ProductVO.rating_count: rating_count+1,
            ProductVO.updated_at: datetime.datetime.now()
        })
        db.session.add(review)
        db.session.commit()

    def check_user_review_for_product(self, user_id, product_id):
        review = db.session.query(ProductReviewVO).filter(
            ProductReviewVO.user_id == user_id, ProductReviewVO.product_id == product_id).first()
        return review
