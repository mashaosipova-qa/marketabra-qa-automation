from typing import Any, Generator

import pytest

from api.clients.abra_client import AbraClient
from api.clients.postgres_client import PostgresClient
from api.models.abra_model import LoginRequestModel
from config import settings


@pytest.fixture
def abra_client() -> AbraClient:
    return AbraClient()

@pytest.fixture
def logged_in_seller() -> Generator[AbraClient, Any, None]:
    abra_client = AbraClient()
    login_request_data = LoginRequestModel(
        email = settings.seller.email,
        password = settings.seller.password
    )
    abra_client.login(login_request_data=login_request_data)
    yield  abra_client

    #abra_client.sign_out()

@pytest.fixture(autouse=True)
def postgres_client() -> PostgresClient:
    return PostgresClient()
