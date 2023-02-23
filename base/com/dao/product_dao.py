from sqlalchemy import func
from base import db
from base.com.vo.product_vo import ProductVO, ProductCategoryVO, ProductSubCategoryVO, ProductInventoryVO, ProductDiscountVO, ProductReviewVO, ProductRatingVO


class ProductCategoryDAO():
    def get_category_id_based_category(self, category_name):
        category = ProductCategoryVO.query.filter_by(
            category_name=category_name).first()
        return category.category_id

    def get_all_categories(self):
        categories = ProductCategoryVO.query.all()
        return [category.as_dict() for category in categories]

    def get_subcategory_based_category(self, category_id):
        subcategories = ProductSubCategoryVO.query.filter_by(
            category_id=category_id).all()
        return [subcategory.as_dict() for subcategory in subcategories]

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


class ProductDAO():
    def get_all_products_based_category(self, category_id):
        products = ProductVO.query.filter_by(
            category_id=category_id).all()
        data_list = []
        for product in products:
            data_dict = {}
            data_dict.update(product.as_dict())
            avg_rating = db.session.query(func.avg(ProductRatingVO.rating)).filter_by(
                product_id=product.product_id).scalar()
            avg_rating = 0 if not avg_rating else avg_rating
            data_dict['avgRating'] = avg_rating
            data_list.append(data_dict)
        return data_list

    def get_top_products_based_rating(self, category_id):
        products = ProductVO.query.filter_by(
            category_id=category_id).all()
        data_list = []
        for product in products:
            data_dict = {}
            data_dict.update(product.as_dict())
            avg_rating = db.session.query(func.avg(ProductRatingVO.rating)).filter_by(
                product_id=product.product_id).scalar()
            avg_rating = 0 if not avg_rating else avg_rating
            data_dict['avgRating'] = avg_rating
            data_list.append(data_dict)
        data_list = sorted(
            data_list, key=lambda d: d['avgRating'], reverse=True)[:4]
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
        reviews = db.session.query(ProductReviewVO, ProductRatingVO, ProductVO).join(
            ProductRatingVO, ProductReviewVO.rating_id == ProductRatingVO.rating_id
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
            ProductRatingVO, ProductReviewVO.rating_id == ProductRatingVO.rating_id
        ).filter_by(product_id=product_id).all()
        print(reviews)
        data_list = []
        for review in reviews:
            data_dict = {}
            data_dict.update(review[0].as_dict())
            data_dict.update(review[1].as_dict())
            data_list.append(data_dict)
        return data_list
