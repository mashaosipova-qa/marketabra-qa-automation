import pytest
import allure

from api.clients.postgres_client import PostgresClient
from config import settings
from api.models.abra_model import FavoritesResponseModel, FavoritesRequestModel, FavoritesListResponseModel, \
    FavoritesRemoveResponseModel
from utils.common_checker import check_difference_between_objects
from api.clients.abra_client import AbraClient


@pytest.mark.smoke
@allure.feature('Favorites')
class TestFavorites:

    @allure.title('Successfully add product to favorites')
    def test_add_to_favorites(
            self,
            logged_in_seller: AbraClient,
            autogenerate_product
    ):
        product_id = autogenerate_product
        request_data = FavoritesRequestModel(product_id=product_id)
        response = logged_in_seller.add_to_favorites(request_data=request_data)
        expected_response = FavoritesResponseModel(
            ok=True,
            result=True
        )
        check_difference_between_objects(actual_result=response, expected_result=expected_response)

    @allure.title('Successfully get favorites list')
    def test_get_favorites_list(
            self,
            logged_in_seller: AbraClient,
            autogenerate_product
    ):
        # Request the list of favorites
        response = logged_in_seller.get_favorites()
        expected_response = FavoritesListResponseModel(
            ok=True,
            result=response.result
        )
        check_difference_between_objects(actual_result=response, expected_result=expected_response)
        # We expect a successful response and a list (even if empty)
        assert response.result is not None
        assert isinstance(response.result.products, list), "Expected 'products' to be of type list"
        assert len(response.result.products) == response.result.total_count
        print(len(response.result.products))


    @allure.title('Successfully remove product from favorites (Smoke)')
    def test_remove_from_favorites_smoke(
            self,
            logged_in_seller: AbraClient,
            autogenerate_product
    ):
        product_id = autogenerate_product
        add_request = FavoritesRequestModel(product_id=product_id)
        add_response = logged_in_seller.add_to_favorites(request_data=add_request)
        assert add_response.ok is True, "Failed to add product to favorites during setup"
        response = logged_in_seller.remove_from_favorites(product_id=product_id)
        expected = FavoritesRemoveResponseModel(ok=True, result=True)
        check_difference_between_objects(actual_result=response, expected_result=expected)
