import requests
import allure
import json
import typing
import datetime
from curlify2 import Curlify

class AllureHelper():
    def __init__(self, indent: int = 4) -> None:
        self.indent = indent

    def _format_json(self, data: str | dict) -> str:
        try:
            return json.dumps(data, indent=self.indent)
        except (json.JSONDecodeError, TypeError):
            return data

    def _format_request_body(self, request_body: typing.Optional[bytes | str]) -> str:
        if isinstance(request_body, bytes):
            return json.dumps(json.loads(request_body.decode()), indent=self.indent)
        return request_body

    def _attach_response_details(self, response: requests.Response, response_body: str) -> None:
        try:
            allure.attach(
                body=(
                    f"Time: {datetime.datetime.now()}\n"
                    f"Response Code:\n{response.status_code} {response.reason}\n\n"
                    f"Response Headers:\n{json.dumps(dict(response.headers), indent=self.indent)}\n\n"
                    f"Response Cookies:\n{json.dumps(dict(response.cookies), indent=self.indent)}\n\n"
                    f"Response Body:\n{response_body}\n"
                ),
                name=f"Response {response.status_code} {response.reason}",
                attachment_type=allure.attachment_type.TEXT,
            )
        except requests.exceptions.JSONDecodeError:
            pass

    def _attach_request_details(self, response):
        # Extract request info from the response object (works with 'requests' lib)
        request = response.request
        allure.attach(
            body=f"Method: {request.method}\nURL: {request.url}\nBody: {request.body}",
            name="Request Info",
            attachment_type=allure.attachment_type.TEXT
        )

    def _attach_http_response(self, response: requests.Response) -> None:
        response_body = self._format_json(
            response.text
            if response.headers.get("Content-Type") != "application/json"
            else response.json()
        )

        with allure.step("Request details"):
            self._attach_request_details(response)

        with allure.step("Response details"):
            self._attach_response_details(
                response,
                json.loads(response_body),
            )


    def enrich_allure(self, response: requests.Response) -> None:
        if response.history:
            list_of_responses = [res for res in response.history]
            list_of_responses.append(response)
            for response in list_of_responses:
                self._attach_http_response(response)
        else:
            self._attach_http_response(response)
