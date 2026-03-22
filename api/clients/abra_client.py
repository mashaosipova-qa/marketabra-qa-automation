import json
import allure

from api.models.abra_model import LoginRequestModel, LoginResponseModel, RefreshTokensResponseModel, \
    FavoritesResponseModel, FavoritesRequestModel, FavoritesListRequestModel, FavoritesListResponseModel, \
    FavoritesRemoveResponseModel, ProductUploadRequestModel, ProductUploadResponseModel, ProductsDeleteResponseModel
from api.models.error_model import ErrorResponseModel
from typing import Any
from utils.http_client import ClientApi
from utils.common_checker import validate_response




class AbraClient(ClientApi):
    def __init__(self):
        super().__init__()

    @allure.step("POST /auth/sign-in")
    def login(self,
              login_request_data: LoginRequestModel,
              expect_error: bool = False,
              expected_status_code: int = 200
              ) -> LoginResponseModel | ErrorResponseModel:
        response = self.request(
            method="POST",
            url="/auth/sign-in",
            json=login_request_data.model_dump()
        )

        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )
        return validate_response(
            model=LoginResponseModel,
            response=response,
            expected_status_code=expected_status_code

        )

    @allure.step("POST /suppliers/products/add")
    def create_product(self,
                       product_data: ProductUploadRequestModel,
                       expect_error: bool = False,
                       expected_status_code: int = 200
                       ) -> ProductUploadResponseModel | ErrorResponseModel:
        data = product_data.model_dump(exclude_none=True, mode='json')
        response = self.request(
            method="POST",
            url="/suppliers/products/add",
            json=data
        )

        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )

        return validate_response(
            model=ProductUploadResponseModel,
            response=response,
            expected_status_code=expected_status_code
        )

    @allure.step("POST /suppliers/products/delete")
    def delete_products(self,
                        product_ids: list[int],
                        expect_error: bool = False,
                        expected_status_code: int = 200
                        ) -> ProductsDeleteResponseModel | ErrorResponseModel:
        """ Deletes products by their IDs (sets is_active to False).This is a POST request with a list of products ID in the body"""
        response = self.request(
            method="POST",
            url="/suppliers/products/delete",
            data=json.dumps(product_ids)
        )

        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )

        return validate_response(
            model=ProductsDeleteResponseModel,
            response=response,
            expected_status_code=expected_status_code
        )

    @allure.step("GET /suppliers/products")
    def get_products_list(self,
                          expect_error: bool = False,
                          expected_status_code: int = 200,
                          params: dict | None = None
                          ) -> Any:
        """ Retrieves and parses NDJSON response from the products endpoint."""
        response = self.request(
            method="GET",
            url="/suppliers/products",
            params=params
        )

        # Manual status code check since we can't use validate_response directly for NDJSON
        if response.status_code != expected_status_code:
            raise AssertionError(f"Expected status {expected_status_code}, but got {response.status_code}")

        lines = response.text.strip().split('\n')
        products = [
            json.loads(line)
            for line in lines
            if line.strip() and json.loads(line).get('type') == 'product'
        ]

        return products


    @allure.step("GET /suppliers/products/{product_id}/variations")
    def get_product_variations(self,
                               product_id: int,
                               expect_error: bool = False,
                               expected_status_code: int = 200
                               ) -> ProductUploadResponseModel | ErrorResponseModel:

        response = self.request(
            method="GET",
            url=f"/suppliers/products/{product_id}/variations"
        )

        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )

        return validate_response(
            model=ProductUploadResponseModel,  # Ensure this model matches the variation response schema
            response=response,
            expected_status_code=expected_status_code
        )

    @allure.step("POST /auth/sign-in/refresh")
    def refresh_tokens(self,
                      expect_error: bool = False,
                      expected_status_code: int = 200
                      ) -> RefreshTokensResponseModel | ErrorResponseModel:
        response = self.request(
            method="POST",
            url="/auth/sign-in/refresh",
        )
        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )
        return validate_response(
            model=RefreshTokensResponseModel,
            response=response,
            expected_status_code=expected_status_code
        )
    @allure.step("POST /sellers/favorites/add")
    def add_to_favorites(self,
                         request_data: FavoritesRequestModel,
                         expect_error: bool = False,
                         expected_status_code: int = 200
                         ) -> FavoritesResponseModel | ErrorResponseModel:
        response = self.request(
            method="POST",
            url="/sellers/favorites/add",
            json=request_data.model_dump(exclude_none=True) # filters out any fields that have a value of None
        )
        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )
        return validate_response(
            model=FavoritesResponseModel,
            response=response,
            expected_status_code=expected_status_code
        )

    @allure.step("GET /sellers/favorites")
    def get_favorites(self,
                      request_data: FavoritesListRequestModel = FavoritesListRequestModel(),
                      expect_error: bool = False,
                      expected_status_code: int = 200
                      ) -> FavoritesListResponseModel | ErrorResponseModel:
        response = self.request(
            method="GET",
            url="/sellers/favorites",
            # For GET requests, we use params instead of json
            params=request_data.model_dump(exclude_none=True)
        )

        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )

        return validate_response(
            model=FavoritesListResponseModel,
            response=response,
            expected_status_code=expected_status_code
        )
    @allure.step("DELETE /sellers/favorites/remove")
    def remove_from_favorites(self,
                              product_id: int,
                              expect_error: bool = False,
                              expected_status_code: int = 200
                              ) -> FavoritesRemoveResponseModel | ErrorResponseModel:
        response = self.request(
            method="DELETE",
            url="/sellers/favorites/remove",
            params={"product_id": product_id}
        )

        if expect_error:
            return validate_response(
                model=ErrorResponseModel,
                response=response,
                expected_status_code=expected_status_code
            )

        return validate_response(
            model=FavoritesRemoveResponseModel,
            response=response,
            expected_status_code=expected_status_code
        )