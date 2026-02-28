from __future__ import annotations
from typing import Optional
from pydantic import BaseModel



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



