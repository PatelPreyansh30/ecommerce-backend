from base import db,app

class Product_categoryVO(db.Model):
    __tablename__ = 'product_category'
    product_category_id = db.Column('product_category_id', db.Integer, primary_key = True,autoincrement = True)
    product_category_name = db.Column('product_category_name', db.String(250), nullable = False)
    product_category_description = db.Column('product_category_description', db.Text, nullable=False)
    

    def as_dict(self):
        return {
            'product_category_id': self.product_category_id,
            'product_category_name': self.product_category_name,
            'product_category_description': self.product_category_description,
        }


class Product_inventoryVO(db.Model):
    __tablename__ = 'product_inventory'
    product_inventory_id = db.Column('product_inventory_id', db.Integer, primary_key = True,autoincrement = True)
    product_inventory_quantity = db.Column('product_inventory_quantity', db.Integer)
    

    def as_dict(self):
        return {
            'product_inventory_id': self.product_inventory_id,
            'product_inventory_quantity': self.product_inventory_quantity,
        }
    

class ProductVO(db.Model):
    __tablename__ = 'product'
    product_id = db.Column('product_id', db.Integer, primary_key = True,autoincrement = True)
    product_name = db.Column('product_name', db.String(250), nullable = False)
    product_description = db.Column('product_description', db.Text, nullable=False)
    product_price = db.Column('product_price', db.Float, nullable=False)
    product_category_id = db.Column('product_category_id', db.ForeignKey(Product_categoryVO.product_category_id, ondelete= 'CASCADE', onupdate= 'CASCADE'), nullable= False, unique=True)
    product_inventory_id = db.Column('product_inventory_id', db.ForeignKey(Product_inventoryVO.product_inventory_id, ondelete= 'CASCADE', onupdate= 'CASCADE'), nullable= False, unique=True)

    # def serialize(self):
    #     return {"id": self.id,
    #             "product_name": self.product_name,
    #             "product_description": self.product_description}
            
    def as_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_description': self.product_description,
            'product_price': self.product_price,
            'product_category_id': self.product_category_id,
            'product_inventory_id': self.product_inventory_id,
        }

    

with app.app_context():
    db.create_all()