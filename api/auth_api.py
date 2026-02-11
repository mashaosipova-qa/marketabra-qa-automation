import requests
from data.test_data import USERS, BASE_URL

class AuthApi:
    def __init__(self, base_url):
        self.url = f"{base_url}/auth"

    def sign_in(self, email, password):
        data = {'email': email, 'password': password}
        res = (requests.post(f'{self.url}/sign-in', json=data))
        return res

