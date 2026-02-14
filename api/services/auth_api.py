import requests

class AuthApi:
    def __init__(self, base_url, email, password):
        self.url = f"{base_url}/auth"
        self.session = requests.Session()
        self.sign_in(email, password)

    def sign_in(self, email, password):
        data = {'email': email, 'password': password}
        res = (self.session.post(f'{self.url}/sign-in', json=data))
        return res

    def get_current(self):
        res = self.session.get(f'{self.url}/sign-in/current')
        return res.status_code, res.json()

    def clean_up(self):
        self.session.delete(f'{self.url}/sign-out')