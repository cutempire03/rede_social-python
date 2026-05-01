from fastapi import APIRouter, Request
from src.api.authentication import login_required

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

# token de um usuário = 820MrsfyEciDN1NxYJsj76yZn5o

@router.get("/")
@login_required
async def informations(request: Request):
    return {'user': request.current_user}