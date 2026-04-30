from fastapi import APIRouter, Depends
from src.datalayer.models.user import UserModel
from typing import Annotated
from src.authenticaion import verify_token

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

# token de um usuário = 820MrsfyEciDN1NxYJsj76yZn5o

@router.post("/")
async def informations(current_user: Annotated[UserModel, Depends(verify_token)]):
    return {'user': current_user}