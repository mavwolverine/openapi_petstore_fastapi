# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

try:
    from fastapi._compat import RequiredParam
except ImportError:
    # FastAPI < 0.115.1
    from fastapi._compat import Required as RequiredParam

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.api_response import ApiResponse
from openapi_server.models.pet import Pet, PetStoreStatus
from openapi_server.security_api import get_token_petstore_auth, get_token_api_key


router = APIRouter()


@router.post(
    "/pet",
    responses={
        200: {"model": Pet, "description": "Successful operation"},
        405: {"description": "Invalid input"},
    },
    tags=["pet"],
    summary="Add a new pet to the store",
    response_model_by_alias=True,
    operation_id="addPet"
)
async def add_pet(
    pet: Pet = Body(RequiredParam, description="Create a new pet in the store"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> Pet:
    """Add a new pet to the store"""
    ...


@router.delete(
    "/pet/{petId}",
    responses={
        400: {"description": "Invalid pet value"},
    },
    tags=["pet"],
    summary="Deletes a pet",
    response_model_by_alias=True,
    operation_id="deletePet"
)
async def delete_pet(
    petId: int = Path(..., description="Pet id to delete"),
    api_key: str = Header(None, alias="api_key", description=""),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> None:
    """"""
    ...


@router.get(
    "/pet/findByStatus",
    responses={
        200: {"model": List[Pet], "description": "successful operation"},
        400: {"description": "Invalid status value"},
    },
    tags=["pet"],
    summary="Finds Pets by status",
    response_model_by_alias=True,
    operation_id="findPetsByStatus"
)
async def find_pets_by_status(
    status: PetStoreStatus = Query('available', description="Status values that need to be considered for filter"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> List[Pet]:
    """Multiple status values can be provided with comma separated strings"""
    ...


@router.get(
    "/pet/findByTags",
    responses={
        200: {"model": List[Pet], "description": "successful operation"},
        400: {"description": "Invalid tag value"},
    },
    tags=["pet"],
    summary="Finds Pets by tags",
    response_model_by_alias=True,
    operation_id="findPetsByTags",
    deprecated=True
)
async def find_pets_by_tags(
    tags: List[str] = Query(None, description="Tags to filter by"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> List[Pet]:
    """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing."""
    ...


@router.get(
    "/pet/{petId}",
    responses={
        200: {"model": Pet, "description": "successful operation"},
        400: {"description": "Invalid ID supplied"},
        404: {"description": "Pet not found"},
    },
    tags=["pet"],
    summary="Find pet by ID",
    response_model_by_alias=True,
    operation_id="getPetById",
)
async def get_pet_by_id(
    petId: int = Path(..., description="ID of pet to return"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
    token_api_key: TokenModel = Security(
        get_token_api_key
    ),
) -> Pet:
    """Returns a single pet"""
    ...


@router.put(
    "/pet",
    responses={
        200: {"model": Pet, "description": "Successful operation"},
        400: {"description": "Invalid ID supplied"},
        404: {"description": "Pet not found"},
        405: {"description": "Validation exception"},
    },
    tags=["pet"],
    summary="Update an existing pet",
    response_model_by_alias=True,
    operation_id="updatePet"
)
async def update_pet(
    pet: Pet = Body(RequiredParam, description="Update an existent pet in the store"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> Pet:
    """Update an existing pet by Id"""
    ...


@router.post(
    "/pet/{petId}",
    responses={
        405: {"description": "Invalid input"},
    },
    tags=["pet"],
    summary="Updates a pet in the store with form data",
    response_model_by_alias=True,
    operation_id="updatePetWithForm",
)
async def update_pet_with_form(
    petId: int = Path(..., description="ID of pet that needs to be updated"),
    name: str = Query(None, description="Name of pet that needs to be updated"),
    status: str = Query(None, description="Status of pet that needs to be updated"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> None:
    """"""
    ...


@router.post(
    "/pet/{petId}/uploadImage",
    responses={
        200: {"model": ApiResponse, "description": "successful operation"},
    },
    tags=["pet"],
    summary="uploads an image",
    response_model_by_alias=True,
    operation_id="uploadFile"
)
async def upload_file(
    petId: int = Path(..., description="ID of pet to update"),
    additional_metadata: str = Query(None, alias="additionalMetadata", description="Additional Metadata"),
    body: str = Body(None, description="", media_type="application/octet-stream"),
    token_petstore_auth: TokenModel = Security(
        get_token_petstore_auth, scopes=["write:pets", "read:pets"]
    ),
) -> ApiResponse:
    """"""
    ...
