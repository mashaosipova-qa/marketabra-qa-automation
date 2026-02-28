import allure
import pytest

from api.clients.abra_client import AbraClient
from api.clients.postgres_client import PostgresClient
from api.models.abra_model import LoginRequestModel, LoginResponseModel, RefreshTokensResponseModel
from api.models.postgres_model import UserModel
from config import settings
from utils.common_checker import check_difference_between_objects


@pytest.mark.api
class TestSignIn:
    @allure.title('Successful login as Seller')
    def test_login(
        self,
        abra_client: AbraClient,
        postgres_client: PostgresClient,
        email=settings.seller.email,
        password=settings.seller.password
    ):
        login_request_data = LoginRequestModel(
            email=email,
            password=password
            )
        login_response = abra_client.login(login_request_data=login_request_data)
        expected_response = LoginResponseModel(
            ok=True,
            result=True,
            )
        check_difference_between_objects(actual_result=login_response, expected_result=expected_response)
        postgres_client.check_user_from_db(
            is_deleted=False,
            is_verified=True,
            email=email,
            expected_user=UserModel(
                email=email,
                is_verified=True,
                is_deleted=False
            )
        )
        assert len(postgres_client.get_user_from_db(email=email, is_deleted=False, is_verified=True)) == 1



    @allure.title('Successful token refresh')
    def test_token_refresh(
        self,
        logged_in_seller: AbraClient,
    ):
        response = logged_in_seller.refresh_tokens()
        expected_response = RefreshTokensResponseModel(
            ok=True,
            result=True
        )
        check_difference_between_objects(actual_result=response, expected_result=expected_response)






