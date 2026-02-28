from typing import Type, TypeVar

import allure
from pydantic import BaseModel
from requests import Response
from deepdiff import DeepDiff

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


@allure.step("Check The Difference Between Objects")
def check_difference_between_objects(
        actual_result, expected_result, exclude_paths: str | list[str] = None
) -> None:
    if isinstance(actual_result, list) and isinstance(expected_result, list):
        comparison_data = (actual_result, expected_result)
    elif isinstance(actual_result, BaseModel):
        comparison_data = (actual_result, expected_result)
    else:
        comparison_data = (MessageToDict(actual_result), MessageToDict(expected_result))

    diff = DeepDiff(
        *comparison_data,
        ignore_order=True,
        exclude_paths=exclude_paths,
    )
    assert not diff, f"Difference: {diff}"