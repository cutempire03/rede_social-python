from typing import Annotated
from fastapi import APIRouter, Depends
from src.services.user import UserService
from src.api.dtos.users import UserRegistration, UserLogin

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/register")
async def register(
    body: UserRegistration,
    service: Annotated[UserService, Depends(UserService)]
):

    response = await service.register(
        name=body.name,
        email=body.email,
        password=body.password
    )

    return {'created': response}

@router.post("/login")
async def login(
    body: UserLogin,
    service: Annotated[UserService, Depends(UserService)]
):

    response = await service.login(
        email=body.email,
        password=body.password
    )

    return {'logado': response}

@router.get("/all-users")
async def allUsers(service: Annotated[UserService, Depends(UserService)]):
    return await service.get_all_users()