import allure
import psycopg2
from api.clients.abra_client import AbraClient
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
