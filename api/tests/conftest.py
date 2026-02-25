import pytest

from api.clients.abra_client import AbraClient


@pytest.fixture
def abra_client() -> AbraClient:
    return AbraClient()





# from api.services.auth_api import AuthApi
# from api.test_data.app_settings1 import USERS, BASE_URL
#
# @pytest.fixture
# def seller_auth_api():
#     # Create authorized API session
#     user = USERS["seller"]
#     api_obj = AuthApi(BASE_URL, user["email"], user["password"])
#     yield api_obj
#
#     # Close session
#     api_obj.clean_up()