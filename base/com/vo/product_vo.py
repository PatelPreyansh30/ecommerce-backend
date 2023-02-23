import datetime
from base import db, app
from base.com.vo.auth_vo import UserVO


class ProductCategoryVO(db.Model):
    __tablename__ = 'product_category_table'
    category_id = db.Column(
        'category_id', db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(
        'category_name', db.String(255), nullable=False)
    category_description = db.Column(
        'category_description', db.Text)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'categoryId': self.category_id,
            'categoryName': self.category_name,
            'categoryDescription': self.ategory_description
        }


class ProductSubCategoryVO(db.Model):
    __tablename__ = 'product_subcategory_table'
    subcategory_id = db.Column(
        'subcategory_id', db.Integer, primary_key=True, autoincrement=True)
    subcategory_name = db.Column(
        'subcategory_name', db.String(255), nullable=False)
    subcategory_description = db.Column(
        'subcategory_description', db.Text)
    category_id = db.Column('category_id', db.ForeignKey(
        ProductCategoryVO.category_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'subcategoryId': self.subcategory_id,
            'subcategoryName': self.subcategory_name,
            'subcategoryDescription': self.subcategory_description
        }


class ProductInventoryVO(db.Model):
    __tablename__ = 'product_inventory_table'
    inventory_id = db.Column(
        'inventory_id', db.Integer, primary_key=True, autoincrement=True)
    inventory_quantity = db.Column(
        'inventory_quantity', db.Integer, nullable=True)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'inventoryId': self.inventory_id,
            'inventoryQuantity': self.inventory_quantity
        }


class ProductDiscountVO(db.Model):
    __tablename__ = 'product_discount_table'
    discount_id = db.Column('discount_id', db.Integer,
                            primary_key=True, autoincrement=True)
    discount_name = db.Column('discount_name', db.String(255), nullable=False)
    discount_percent = db.Column(
        'discount_percent', db.Integer, nullable=False)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'discountId': self.discount_id,
            'discountName': self.discount_name,
            'discountPercent': self.discount_percent
        }


class ProductVO(db.Model):
    __tablename__ = 'product_table'
    product_id = db.Column('product_id', db.Integer,
                           primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(250), nullable=False)
    description = db.Column(
        'description', db.Text, nullable=False)
    price = db.Column('price', db.Float, nullable=False)
    category_id = db.Column('category_id', db.ForeignKey(
        ProductCategoryVO.category_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    subcategory_id = db.Column('subcategory_id', db.ForeignKey(
        ProductSubCategoryVO.subcategory_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    inventory_id = db.Column('inventory_id', db.ForeignKey(
        ProductInventoryVO.inventory_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    discount_id = db.Column('discount_id', db.ForeignKey(
        ProductDiscountVO.discount_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'productId': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }


class ProductRatingVO(db.Model):
    __tablename__ = 'product_rating_table'
    rating_id = db.Column('rating_id', db.Integer,
                          primary_key=True, autoincrement=True)
    rating = db.Column(
        'rating', db.Float, nullable=False)
    product_id = db.Column('product_id', db.ForeignKey(
        ProductVO.product_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'ratingId': self.rating_id,
            'rating': self.rating
        }


class ProductReviewVO(db.Model):
    __tablename__ = 'product_review_table'
    review_id = db.Column('review_id', db.Integer,
                          primary_key=True, autoincrement=True)
    review_msg = db.Column(
        'review_msg', db.Text, nullable=False)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id = db.Column('product_id', db.ForeignKey(
        ProductVO.product_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    rating_id = db.Column('rating_id', db.ForeignKey(
        ProductRatingVO.rating_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    created_at = db.Column('created_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column('updated_at', db.DateTime,
                           default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            'reviewId': self.review_id,
            'reviewMsg': self.review_msg,
            'updatedAt': self.updated_at
        }


with app.app_context():
    db.create_all()
