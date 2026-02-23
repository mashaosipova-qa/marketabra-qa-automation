from __future__ import annotations

from typing import Optional
from pydantic import BaseModel

class LocModel(BaseModel):
    loc: Optional[list]
    msg: str
    type: str


class ErrorResponseModel(BaseModel):
    detail: list[LocModel]
