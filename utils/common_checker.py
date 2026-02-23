import typing
from typing import Type, TypeVar

import allure
from pydantic import BaseModel
from requests import Response

T = TypeVar("T", bound=BaseModel)

@allure.step("Validate status code")
def check_status_code(
        response: Response,
        expected_status_code: int = 200
) -> None:
    assert response.status_code == expected_status_code,(
        f"Unexpected status code. Expected {expected_status_code}. "
        f"actual {response.status_code},{response.text}"
    )

@allure.step("Validate model")
def validate_model(model: Type[T], response) -> T:
    return model.model_validate(response)

@allure.step("Validate response")
def validate_response(
        model: Type[T],
        response: Response,
        expected_status_code: int = 200,

) -> T:
    check_status_code(response, expected_status_code)
    return validate_model(model, response.json())