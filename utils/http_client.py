from typing import Optional
import requests
import typing
from config import settings
from utils.allure_helper import AllureHelper



class ClientApi:
    def __init__(self) -> None:
        self.settings = settings
        self.env = settings.ENVIRONMENT
        self.base_url = settings.BASE_URL_API
        self.allure_helper = AllureHelper()
        self._session = self._initialize_session()

    @staticmethod
    def _initialize_session() -> requests.Session:
        return requests.Session()


    def request(self,
        method: str,
        url: typing.Optional[str] = None,
        params: typing.Optional[dict] = None,
        headers: typing.Optional[dict] = None,
        cookies: typing.Optional[dict] = None,
        files: typing.Optional[dict] = None,
        json: typing.Optional[dict] = None,
        data: typing.Optional[dict | str | list] = None,
        verify: bool = False,
        timeout: typing.Optional[float] = None,
    ) -> requests.Response:
        response = self._session.request(
            method=method,
            url=self.base_url + url,
            headers=headers,
            params=params,
            cookies=cookies,
            json=json,
            data=data,
            files=files,
            verify=verify,
            timeout=timeout
        )
        self.allure_helper.enrich_allure(response)
        return response




