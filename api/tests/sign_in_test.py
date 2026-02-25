import allure
import pytest

from api.clients.abra_client import AbraClient
from api.models.abra_model import LoginRequestModel, LoginResponseModel, RefreshTokensResponseModel
from config import settings
from utils.common_checker import check_difference_between_objects


@pytest.mark.api
class TestSignIn:
    @allure.title('Successful login as Seller')
    def test_login(
            self,
            abra_client: AbraClient,
            email=settings.EMAIL_SELLER,
            password=settings.PASSWORD_SELLER
    ):
            login_request_data = LoginRequestModel(
                email = email,
                password = password
        )
            login_response = abra_client.login(login_request_data=login_request_data)
            expected_response = LoginResponseModel(
            ok=True,
            result=True,
            detail=None,
            error=None,
            error_code=None
            )
            check_difference_between_objects(actual_result=login_response, expected_result=expected_response)


    @allure.title('Successful token refresh')
    def test_token_refresh(
            self,
            abra_client: AbraClient

    ):
            login_request_data = LoginRequestModel(
                email = settings.EMAIL_SELLER,
                password = settings.PASSWORD_SELLER
        )
            login_response = abra_client.login(login_request_data=login_request_data)
            current_csrf_token = login_response.get_csrf_token()
            refresh_token = abra_client.refresh_tokens(current_csrf_token=current_csrf_token)
            expected_response = RefreshTokensResponseModel(
                ok=True,
                result=True,
                detail="",
                error="",
                error_code=0
            )
            check_difference_between_objects(actual_result=login_response, expected_result=expected_response)






