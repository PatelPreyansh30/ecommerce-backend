from base import db
from base.com.vo.auth_vo import UserVO

class UserDAO():
    def add_user(self, user_object):
        db.session.add(user_object)
        db.session.commit()
        
    def get_single_user(self, user_email):
        user_object = UserVO.query.filter_by(user_email = user_email).first()
        return user_object
    
    # def view_subcategory(self):
    #     subcategory_vo_list = db.session.query(SubCategoryVO, CategoryVO).join(CategoryVO,SubCategoryVO.subcategory_category_id == CategoryVO.category_id).all()
    #     return subcategory_vo_list

    # def delete_subcategory(self, subcategory_id):
    #     subcategory_vo_obj = SubCategoryVO.query.get(subcategory_id)
    #     db.session.delete(subcategory_vo_obj)
    #     db.session.commit()
    
    # def edit_subcategory(self, subcategory_vo):
    #     subcategory_vo_obj = SubCategoryVO.query.filter_by(subcategory_id = subcategory_vo.subcategory_id).first()
    #     return subcategory_vo_obj
    
    # def update_subcategory(self, subcategory_vo):
    #     db.session.merge(subcategory_vo)
    #     db.session.commit()

    # def get_subcategory_by_category_id(self, category_id):
    #     subcategory = SubCategoryVO.query.filter_by(subcategory_category_id = category_id)
    #     return subcategory