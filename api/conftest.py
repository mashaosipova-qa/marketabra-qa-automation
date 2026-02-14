import pytest

from api.services.auth_api import AuthApi
from api.data.settings import USERS, BASE_URL

@pytest.fixture
def seller_auth_api():
    # Create authorized API session
    user = USERS["seller"]
    api_obj = AuthApi(BASE_URL, user["email"], user["password"])
    yield api_obj

    # Close session
    api_obj.clean_up()