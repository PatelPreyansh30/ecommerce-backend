from flask import make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from base import app
from base.com.vo.product_vo import ProductVO
from base.com.dao.product_dao import ProductDAO, ProductCategoryDAO, ProductReviewsRatingsDAO, ProductSubCategoryDAO

product_api_path = '/api/a3/products'

@app.route(f'{product_api_path}')
@jwt_required()
def get_products():
    product_dao = ProductDAO()
    category = request.args.get('category')
    subcategory = request.args.get('subcategory')
    if category:
        # if not category:
        #     return make_response({"msg": "Query param not correct"}, 400)
        # else:
        product_category_dao = ProductCategoryDAO()
        try:
            category_id = product_category_dao.get_category_id_based_category(
                category)
            data = product_dao.get_all_products_based_category(category_id)
            if len(data) != 0:
                return make_response({"products": data}, 200)
            else:
                return make_response({"msg": "No products found"}, 400)
        except AttributeError:
            return make_response({"msg": "No products found for given category"}, 400)
    elif subcategory:
        product_subcategory_dao = ProductSubCategoryDAO()
        try:
            subcategory_id = product_subcategory_dao.get_subcategory_id_based_subcategory(
                subcategory)
            data = product_dao.get_all_products_based_subcategory(subcategory_id)
            if len(data) != 0:
                return make_response({"products": data}, 200)
            else:
                return make_response({"msg": "No products found"}, 400)
        except AttributeError:
            return make_response({"msg": "No products found for given subcategory"}, 400)


@app.route(f'{product_api_path}/<int:id>')  # Products by id
@jwt_required()
def get_one_product(id):
    product_dao = ProductDAO()
    try:
        data = product_dao.get_single_product(id)
        if not data:
            return make_response({"msg": "No product found"}, 400)
        else:
            return make_response(data, 200)
    except TypeError:
        return make_response({"msg": "Invalid id"}, 400)


@app.route(f'{product_api_path}/reviews', methods=['POST'])
@jwt_required()
def add_product_review():
    user_id = get_jwt_identity().get('userId')
    product_review_rating_dao = ProductReviewsRatingsDAO()
    if request.method == 'POST':
        try:
            review_msg = request.json.get("reviewMsg")
            rating = request.json.get("rating")
            product_id = request.json.get("productId")
            rating_count = request.json.get("productRatingCount")
            avg_rating = request.json.get("productAvgRating")

            existing_review = product_review_rating_dao.check_user_review_for_product(
                user_id, product_id)
            if existing_review == None:
                product_review_rating_dao.add_product_review(
                    user_id, product_id, review_msg, rating, rating_count, avg_rating)
                return make_response({"msg": "Review successfully added"}, 201)
            else:
                return make_response({"msg": "You have already add review"}, 201)
        except Exception as e:
            print(e)
            return make_response({"msg": "Something went wrong, try again"}, 400)


@app.route(f'{product_api_path}/reviews/<int:id>')
@jwt_required()
def get_one_product_reviews(id):
    product_review_rating_dao = ProductReviewsRatingsDAO()
    data = product_review_rating_dao.get_reviews_ratings_by_product(id)
    if len(data) == 0:
        return make_response({"msg": "No reviews found"}, 400)
    else:
        return make_response({"reviews": data}, 200)


@app.route(f'{product_api_path}/categories')  # For all categories
@jwt_required()
def get_all_categories():
    product_category_dao = ProductCategoryDAO()
    data = product_category_dao.get_all_categories()
    if len(data) != 0:
        return make_response({"categories": data}, 200)
    else:
        return make_response({"msg": "No categories found"}, 400)


@app.route(f'{product_api_path}/subcategory')  # For all subcategories
@jwt_required()
def get_subcategories():
    product_category_dao = ProductCategoryDAO()
    category = request.args.get('category')
    if not category:
        return make_response({"msg": "Query param not correct"}, 400)
    else:
        category_id = product_category_dao.get_category_id_based_category(
            category)
        data = product_category_dao.get_subcategory_based_category(category_id)
        if len(data) != 0:
            return make_response({"categories": data}, 200)
        else:
            return make_response({"msg": "No categories found"}, 400)


@app.route(f'{product_api_path}/get-top-products')
@jwt_required()
def get_top_products():
    product_dao = ProductDAO()
    product_category_dao = ProductCategoryDAO()
    category = request.args.get('category')
    if not category:
        return make_response({"msg": "Query param not correct"}, 400)
    else:
        try:
            category_id = product_category_dao.get_category_id_based_category(
                category)
            data = product_dao.get_top_products_based_rating(category_id)
            # print(data)
            if len(data) != 0:
                return make_response({"products": data}, 200)
            else:
                return make_response({"msg": "No products found"}, 400)
        except AttributeError:
            return make_response({"msg": "No products found for given category"}, 400)
