import allure
import pytest
import time

from api.clients.abra_client import AbraClient
from api.clients.postgres_client import PostgresClient
from api.models.abra_model import FavoritesRequestModel
from config import settings


@pytest.mark.e2e
@allure.feature('Favorites')
class TestFavoritesE2E:

    @allure.title('E2E: Seller can add and then remove a product from favorites')
    def test_add_and_remove_favorites_e2e(
            self,
            logged_in_seller: AbraClient,
            autogenerate_product,
            postgres_client: PostgresClient
    ):
        email = settings.seller.email
        user_id = postgres_client.get_user_id(email)
        seller_id = postgres_client.get_seller_id(user_id)
        product_id = autogenerate_product

        with allure.step("Step 1: Add to favorites and verify DB"):
            request_data = FavoritesRequestModel(product_id=product_id)
            response = logged_in_seller.add_to_favorites(request_data=request_data)
            assert response.ok is True, f"API returned error: {response}"
            assert response.result is True, "'result' is False"
            time.sleep(1)
            postgres_client.check_favorite_record(seller_id=seller_id, product_id=product_id)

        with allure.step("Step 2: Verify favorites list"):
            fav_response = logged_in_seller.get_favorites()
            assert fav_response.ok is True, f"API returned error: {fav_response}"
            products_data = fav_response.result.products
            fav_products = [p.id for p in products_data]

            print(f"Favorites list from API: {fav_products}")
            assert product_id in fav_products, f"Product {product_id} not found in {fav_products}"

        with allure.step("Step 3: Remove from favorites and verify DB"):
            delete_response = logged_in_seller.remove_from_favorites(product_id=product_id)
            assert delete_response.ok is True, f"API returned error: {delete_response}"
            time.sleep(1)
            final_db_check = postgres_client.get_favorite_record(seller_id=seller_id, product_id=product_id)
            assert not final_db_check, f"Favorite record for product {product_id} still exists in DB for seller {seller_id}"

        with allure.step("Step 4: Verify favorites list"):
            fav_response = logged_in_seller.get_favorites()
            assert fav_response.ok is True
            fav_products = [p.id for p in fav_response.result.products]
            assert product_id not in fav_products, f"Product {product_id} is still present in favorites list"
