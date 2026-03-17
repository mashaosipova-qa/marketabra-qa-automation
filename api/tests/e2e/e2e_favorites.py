@allure.title('Check that added product is in favorites list')
def test_get_favorites_list(
        self,
        logged_in_seller: AbraClient,
        product_id=settings.test_data.default_product_id
):
    # 1. Сначала добавляем товар (как в прошлом тесте)
    req_data = FavoritesRequestModel(product_id=product_id)
    logged_in_seller.add_to_favorites(request_data=req_data)

    # 2. Получаем список избранного
    response = logged_in_seller.get_favorites()

    # 3. Проверяем, что ответ успешный и товар есть в списке
    assert response.ok is True
    # Проверяем, есть ли наш product_id среди id всех продуктов в списке
    product_ids = [p.id for p in response.result.products]
    assert product_id in product_ids, f"Product {product_id} not found in favorites"


    # @allure.title('Successfully remove product from favorites')
    # def test_remove_from_favorites(
    #         self,
    #         logged_in_seller: AbraClient,
    #         autogenerate_product
    # ):
    #     product_id = autogenerate_product
    #     add_request = FavoritesRequestModel(product_id=product_id)
    #     logged_in_seller.add_to_favorites(request_data=add_request)
    #     current_favorites = logged_in_seller.get_favorites()
    #     favorites_ids = [f.id for f in current_favorites.result.products]
    #     assert product_id in favorites_ids, f"Product ID {product_id} was not added to favorites"
    #     response = logged_in_seller.remove_from_favorites(product_id=product_id)
    #     expected_response = FavoritesRemoveResponseModel(
    #         ok=True,
    #         result=True
    #     )
    #     check_difference_between_objects(actual_result=response, expected_result=expected_response)
    #     post_favorites = logged_in_seller.get_favorites()
    #     post_ids = [f.id for f in post_favorites.result.products]
    #     assert product_id not in post_ids, f"Product ID {product_id} is still in favorites after removal"