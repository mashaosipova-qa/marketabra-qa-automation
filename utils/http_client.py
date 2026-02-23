import requests







class ClientApi:


    def request(self,
                method: str,
                url: str,
                params: typing.Optional[dict] = None,
                headers: typing.Optional[dict] = None,
                cookies: typing.Optional[dict] = None,
                files: typing.Optional[dict] = None,
                json: typing.Optional[dict] = None,
                data: typing.Optional[dict | str | list] = None,
                allow_redirects: bool = True,
                cert: typing.Optional[str | tuple] = None,
                verify: bool = False,
                timeout: typing.Optional[float] = None,
                ) -> requests.Response:
        response = self._session.request(
            method=method,
            url=special_url
                or f"https://{self.service}.{self.base_url}.{self.env}{url}",
            headers=headers,
            params=params,
            cookies=cookies,
            json=json,
            data=data,
            files=files,
            allow_redirects=allow_redirects,
            cert=cert,
            verify=verify,
            timeout=timeout,
        )
        self.allure_helper.enrich_allure(response)
        return response
                ):



