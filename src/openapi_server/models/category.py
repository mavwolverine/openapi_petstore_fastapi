# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Category(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Category - a model defined in OpenAPI

        id: The id of this Category [Optional].
        name: The name of this Category [Optional].
    """

    id: Optional[int] = Field(alias="id", default=None, example=1)
    name: Optional[str] = Field(alias="name", default=None, example="Dogs")

Category.update_forward_refs()
