from utils.http_client import ClientApi
from utils.common_checker import validate_response
import allure
from api.models.abra_model import LoginRequestModel, LoginResponseModel, RefreshTokensRequestModel
from api.models.error_model import ErrorResponseModel



class AbraClient(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step("POST /auth/sign-in")
    def login(self,
              login_request_data: LoginRequestModel,
              expect_error: bool = False,
              expected_status_code: int = 200
              ) -> LoginResponseModel | ErrorResponseModel:
        response = self.request(
            method="POST",
            url="/auth/sign-in",
            json=login_request_data.model_dump()
        )

        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )
        return validate_response(
            model=LoginResponseModel,
            response=response,
            expected_status_code=expected_status_code
        )
    @allure.step("POST /auth/sign-in/refresh")
    def refresh_tokens(self,
                      csrf_token: str,
                      expect_error: bool = False,
                      expected_status_code: int = 200
                      ) -> RefreshTokensRequestModel | ErrorResponseModel:
        headers = {"X-CSRF-TOKEN": csrf_token}
        response = self.request(
            method="POST",
            url="/auth/sign-in/refresh",
            headers=headers
        )
        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )
        return validate_response(
            model=RefreshTokensRequestModel,
            response=response,
            expected_status_code=expected_status_code
        )
