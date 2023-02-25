from base import db
from base.com.vo.user_vo import UserInfoVO, UserFavoriteVO
from base.com.vo.product_vo import ProductVO, ProductSubCategoryVO, ProductDiscountVO
import datetime


class UserInfoDAO():
    def get_user_profile(self, user_id):
        user_info = UserInfoVO.query.filter_by(user_id=user_id).first()
        if not user_info:
            return None
        return user_info.as_dict()

    def add_user_profile(self, user_id, first_name, last_name, dob, mobile, encoded_profile_pic):
        updation = UserInfoVO.query.filter_by(user_id=user_id).update({
            UserInfoVO.user_first_name: first_name,
            UserInfoVO.user_last_name: last_name,
            UserInfoVO.user_dob: dob,
            UserInfoVO.user_mobile: mobile,
            UserInfoVO.user_profile_data_url: encoded_profile_pic,
            UserInfoVO.user_id: user_id,
            UserInfoVO.updated_at: datetime.datetime.utcnow()
        })
        if updation == 0:
            user_info = UserInfoVO(
                user_first_name=first_name,
                user_last_name=last_name,
                user_dob=dob,
                user_mobile=mobile,
                user_profile_data_url=encoded_profile_pic,
                user_id=user_id,
                created_at=datetime.datetime.utcnow(),
                updated_at=datetime.datetime.utcnow()
            )
            db.session.add(user_info)
        db.session.commit()


class UserFavoriteDAO():
    def get_user_favorites(self, user_id):
        user_favorites = db.session.query(
            UserFavoriteVO, ProductVO, ProductSubCategoryVO, ProductDiscountVO).join(
            ProductVO, UserFavoriteVO.product_id == ProductVO.product_id
        ).join(
            ProductSubCategoryVO, ProductVO.subcategory_id == ProductSubCategoryVO.subcategory_id
        ).join(
            ProductDiscountVO, ProductVO.discount_id == ProductDiscountVO.discount_id
        ).filter(UserFavoriteVO.user_id == user_id).all()
        data = []
        for favorites in user_favorites:
            data_dict = {}
            data_dict.update(favorites[0].as_dict())
            data_dict.update(favorites[1].as_dict())
            data_dict.update(favorites[2].as_dict())
            data_dict.update(favorites[3].as_dict())
            data.append(data_dict)
        return data

    def post_user_favorites(self, user_id, product_id):
        user_favorite = UserFavoriteVO(
            user_id=user_id,
            product_id=product_id
        )
        db.session.add(user_favorite)
        favorites = db.session.query(
            UserFavoriteVO, ProductVO, ProductSubCategoryVO, ProductDiscountVO).join(
                ProductVO, UserFavoriteVO.product_id == ProductVO.product_id
        ).join(
            ProductSubCategoryVO, ProductVO.subcategory_id == ProductSubCategoryVO.subcategory_id
        ).join(
            ProductDiscountVO, ProductVO.discount_id == ProductDiscountVO.discount_id
        ).filter(UserFavoriteVO.user_id == user_id, UserFavoriteVO.product_id == product_id).all()

        if len(favorites) > 1:
            return None
        data = {}
        for item in favorites[0]:
            data.update(item.as_dict())
        db.session.commit()
        return data
