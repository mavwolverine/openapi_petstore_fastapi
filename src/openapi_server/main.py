# coding: utf-8

"""
    Swagger Petstore - OpenAPI 3.0

    This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the pet store, we've switched to the design first approach! You can now help us improve the API whether it's by making changes to the definition itself or to the code. That way, with time, we can improve the API in general, and expose some of the new features in OAS3.  Some useful links: - [The Pet Store repository](https://github.com/swagger-api/swagger-petstore) - [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)

    The version of the OpenAPI document: 1.0.17
    Contact: apiteam@swagger.io
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from openapi_server.apis.pet_api import router as PetApiRouter
from openapi_server.apis.store_api import router as StoreApiRouter
from openapi_server.apis.user_api import router as UserApiRouter

app = FastAPI(
    title="Swagger Petstore - OpenAPI 3.0",
    description="This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the pet store, we&#39;ve switched to the design first approach! You can now help us improve the API whether it&#39;s by making changes to the definition itself or to the code. That way, with time, we can improve the API in general, and expose some of the new features in OAS3.  Some useful links: - [The Pet Store repository](https://github.com/swagger-api/swagger-petstore) - [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)",
    version="1.0.17",
    openapi_tags=[
        {
            "name": "pet",
            "description": "Everything about your Pets",
            "externalDocs": {
                "description": "Find out more",
                "url": 'http://swagger.io',
            }
        },
        {
            "name": "store",
            "description": "Access to Petstore orders",
            "externalDocs": {
                "description": "Find out more about our store",
                "url": 'http://swagger.io',
            }
        },
        {
            "name": "user",
            "description": "Operations about user"
        }
    ]
)

app.include_router(PetApiRouter)
app.include_router(StoreApiRouter)
app.include_router(UserApiRouter)
