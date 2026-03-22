import allure
import psycopg2
import pytest

from api.clients.abra_client import AbraClient
from api.models.abra_model import FavoritesRequestModel, FavoritesResponseModel
from api.models.postgres_model import UserModel
from config import settings
from utils.common_checker import check_difference_between_objects


class PostgresClient(AbraClient):
    @staticmethod
    def get_instance(request: str):
        connection = psycopg2.connect(
            database=settings.db.name,
            user=settings.db.user,
            password=settings.db.password,
            host=settings.db.host,
            port=settings.db.port
        )

        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(request)
                    return cursor.fetchall()
        finally:

            connection.close()

    @allure.step("Get User from Database")
    def get_user_from_db(self,
                         email: str,
                         is_deleted: bool,
                         is_verified: bool
                         ):
        return self.get_instance(
            f"SELECT *"
            f' FROM "user" '
            f" WHERE email = '{email}'"
            f" AND is_deleted = {is_deleted}"
            f" AND is_verified = {is_verified}"
        )

    @allure.step("Check User from Database")
    def check_user_from_db(self,
                           email: str,
                           is_deleted: bool,
                           is_verified: bool,
                           expected_user: UserModel) -> None:
        user_from_db = self.get_user_from_db(email, is_deleted, is_verified)[0]
        actual_user = UserModel(
            email=user_from_db[3],
            is_deleted=user_from_db[1],
            is_verified=user_from_db[0])
        expected_user = UserModel(email=expected_user.email, is_deleted=expected_user.is_deleted, is_verified=expected_user.is_verified)
        check_difference_between_objects(actual_result=actual_user, expected_result=expected_user)

    @allure.step("Get User ID from DB")
    def get_user_id(self, email: str) -> int:
        result = self.get_instance(
            f"SELECT id"
            f' FROM "user" '
            f" WHERE email = '{email}'"
        )
        assert result, f"User with email {email} not found in Database"
        return result[0][0]

    @allure.step("Get favorite record from Database")
    def get_favorite_record(self,
                            seller_id: int,
                            product_id: int
                            ):
        return self.get_instance(
            f"SELECT *"
            f' FROM "seller_favorite" '
            f" WHERE seller_id = {seller_id}"
            f" AND product_id = {product_id}"
        )

    @allure.step("Get Seller ID from User ID")
    def get_seller_id(self, user_id: int) -> int:
        result = self.get_instance(
            f'SELECT id FROM "seller" WHERE user_id = {user_id}'
        )
        assert result, f"Seller profile not found for user_id {user_id}"
        return result[0][0]

    @allure.step("Check favorite record in Database")
    def check_favorite_record(self, seller_id: int, product_id: int) -> None:
        result = self.get_favorite_record(seller_id, product_id)
        print(f"Searching for product: {product_id}")
        print(f"Seller_id: {seller_id}")
        assert result, f"Record for seller {seller_id} and product {product_id} not found in DB"
        assert len(result) == 1, f"Expected exactly 1 record for seller {seller_id}, but found {len(result)}"
        db_seller_id = result[0][0]
        db_product_id = result[0][1]
        with allure.step("Verify seller_id and product_id match"):
            assert db_seller_id == seller_id, f"Expected seller_id {seller_id}, but found {db_seller_id}"
            assert db_product_id == product_id, f"Expected product_id {product_id}, but found {db_product_id}"

