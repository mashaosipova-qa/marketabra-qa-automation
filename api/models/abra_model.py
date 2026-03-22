from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field



class LoginRequestModel(BaseModel):
    email: Optional[str | int] = None
    password: Optional[str | int] = None

class LoginResponseModel(BaseModel):
    ok: bool
    result: bool
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None

class RefreshTokensRequestModel(BaseModel):
    #The request body is empty here
    pass

class RefreshTokensResponseModel(BaseModel):
    ok: bool
    result: bool
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None

"""Sub-models define the nested structures for images, attributes, bundles, and pricing required by the ProductUploadRequestModel"""
class ProductImageUpload(BaseModel):
    order: int
    image: str

class PropertyValueUpload(BaseModel):
    property_type_id: int
    property_value_id: int
    optional_value: Optional[str] = None

class VariationValueUpload(BaseModel):
    variation_value_id: int
    images: list[ProductImageUpload]

class BundleContent(BaseModel):
    variation_value_id: int
    amount: int

class BundleGrade(BaseModel):
    grade_quantity: int
    grade_discount: int

class BundleUpload(BaseModel):
    name: str
    variation_type_id: int
    content: list[BundleContent]
    bundle_grades: list[BundleGrade]

class VariationPriceUpload(BaseModel):
    price: int
    discount: int
    variation_value_ids: list[int]

"""Main request schema for the Product Upload endpoint. Aggregates product metadata, images, properties, bundles, and pricing."""
class ProductUploadRequestModel(BaseModel):
    name: str
    description: str
    brand: int
    category: int
    images: Optional[list[ProductImageUpload]] = None
    properties: Optional[list[PropertyValueUpload]] = None
    variations: Optional[list[VariationValueUpload]] = None
    bundles: Optional[list[BundleUpload]] = None
    prices: Optional[list[VariationPriceUpload]] = None

class ProductIdModel(BaseModel):
    id: int

class ProductUploadResponseModel(BaseModel):
    ok: bool
    result: Optional[ProductIdModel] = None
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None

class ProductsDeleteResponseModel(BaseModel):
    ok: bool
    result: bool
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None


class FavoritesRequestModel(BaseModel):
    product_id: Optional[str | int] = None

class FavoritesResponseModel(BaseModel):
    ok: bool
    result: bool
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None

class FavoritesListRequestModel(BaseModel):
    query: Optional[str] = None
    limit: int = 100
    offset: int = 0

class ImageModel(BaseModel):
    id: int
    image_url: str

class ProductModel(BaseModel):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: str
    grade_average: Optional[float] = None
    company_name: Optional[str] = None
    company_created_at: Optional[str] = None
    completed_orders_count: Optional[int] = None
    is_favorite: Optional[bool] = None
    category_id: Optional[int] = None
    category_name: Optional[str] = None
    parent_category_name: Optional[str] = None
    grandparent_category_name: Optional[str] = None
    review_count: Optional[int] = None
    product_variation_price_from: float
    product_variation_price_to: float
    images: list[ImageModel] = Field(default_factory=list)

class FavoritesListData(BaseModel):
    total_count: int
    products: list[ProductModel]

class FavoritesListResponseModel(BaseModel):
    ok: bool
    result: Optional[FavoritesListData] = None # Optional in case an error occurs
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None


class FavoritesRemoveRequestModel(BaseModel):
    product_id: int = Field(..., ge=1, le=2147483647)

# Если у тебя еще нет общей модели для простых ответов:
class FavoritesRemoveResponseModel(BaseModel):
    ok: bool
    result: bool
    detail: Optional[str] = None
    error: Optional[str] = None
    error_code: Optional[int] = None

FavoritesListResponseModel.model_rebuild() # Necessary for Pydantic V2 to properly initialize nested model relationships
ProductUploadRequestModel.model_rebuild()



