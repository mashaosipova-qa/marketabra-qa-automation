from api.auth_api import AuthApi
from data.test_data import USERS, BASE_URL


def test_sign_in_as_seller():
    auth = AuthApi(BASE_URL)
    user = USERS["seller"]
    response = auth.sign_in(user["email"], user["password"])
    assert response.status_code == 200
    assert response.json()["ok"] == True
    assert response.json()["result"] == True
