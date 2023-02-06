from base import db, app
from base.com.vo.auth_vo import UserVO


class ProductCategoryVO(db.Model):
    __tablename__ = 'product_category_table'
    product_category_id = db.Column(
        'product_category_id', db.Integer, primary_key=True, autoincrement=True)
    product_category_name = db.Column(
        'product_category_name', db.String(255), nullable=False)
    product_category_description = db.Column(
        'product_category_description', db.Text)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'product_category_id': self.product_category_id,
            'product_category_name': self.product_category_name,
            'product_category_description': self.product_category_description
        }


class ProductSubCategoryVO(db.Model):
    __tablename__ = 'product_subcategory_table'
    product_subcategory_id = db.Column(
        'product_subcategory_id', db.Integer, primary_key=True, autoincrement=True)
    product_subcategory_name = db.Column(
        'product_subcategory_name', db.String(255), nullable=False)
    product_subcategory_description = db.Column(
        'product_subcategory_description', db.Text)
    product_category_id = db.Column('product_category_id', db.ForeignKey(
        ProductCategoryVO.product_category_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'product_subcategory_id': self.product_subcategory_id,
            'product_subcategory_name': self.product_subcategory_name,
            'product_subcategory_description': self.product_subcategory_description,
            'product_category_id': self.product_category_id
        }


class ProductInventoryVO(db.Model):
    __tablename__ = 'product_inventory_table'
    product_inventory_id = db.Column(
        'product_inventory_id', db.Integer, primary_key=True, autoincrement=True)
    product_inventory_quantity = db.Column(
        'product_inventory_quantity', db.Integer, nullable=True)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'product_inventory_id': self.product_inventory_id,
            'product_inventory_quantity': self.product_inventory_quantity
        }


class ProductVO(db.Model):
    __tablename__ = 'product_table'
    product_id = db.Column('product_id', db.Integer,
                           primary_key=True, autoincrement=True)
    product_name = db.Column('product_name', db.String(250), nullable=False)
    product_description = db.Column(
        'product_description', db.Text, nullable=False)
    product_price = db.Column('product_price', db.Float, nullable=False)
    product_category_id = db.Column('product_category_id', db.ForeignKey(
        ProductCategoryVO.product_category_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_subcategory_id = db.Column('product_subcategory_id', db.ForeignKey(
        ProductSubCategoryVO.product_subcategory_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_inventory_id = db.Column('product_inventory_id', db.ForeignKey(
        ProductInventoryVO.product_inventory_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_description': self.product_description,
            'product_price': self.product_price,
            'product_category_id': self.product_category_id,
            'product_subcategory_id': self.product_subcategory_id,
            'product_inventory_id': self.product_inventory_id
        }


class ProductRatingVO(db.Model):
    __tablename__ = 'product_rating_table'
    product_rating_id = db.Column('product_rating_id', db.Integer,
                                  primary_key=True, autoincrement=True)
    product_rating = db.Column(
        'product_rating', db.Float, nullable=False)
    product_id = db.Column('product_id', db.ForeignKey(
        ProductVO.product_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'product_rating_id': self.product_rating_id,
            'product_rating': self.product_rating,
            'product_id': self.product_id
        }


class ProductReviewVO(db.Model):
    __tablename__ = 'product_review_table'
    product_review_id = db.Column('product_review_id', db.Integer,
                                  primary_key=True, autoincrement=True)
    product_review_msg = db.Column(
        'product_review_msg', db.Text, nullable=False)
    user_id = db.Column('user_id', db.ForeignKey(
        UserVO.user_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_id = db.Column('product_id', db.ForeignKey(
        ProductVO.product_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    product_rating_id = db.Column('product_rating_id', db.ForeignKey(
        ProductRatingVO.product_rating_id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_at = db.Column('created_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # updated_at = db.Column('updated_at', db.DateTime,
    #                        default=datetime.datetime.utcnow)
    # deleted_at = db.Column('deleted_at', db.DateTime)

    def as_dict(self):
        return {
            'product_review_id': self.product_review_id,
            'product_review_msg': self.product_review_msg,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'product_rating_id': self.product_rating_id
        }


with app.app_context():
    db.create_all()
