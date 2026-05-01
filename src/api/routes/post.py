from fastapi import APIRouter, Depends, Request
from typing import Annotated
from src.api.dtos.posts import PostCreation
from src.api.authentication import login_required
from src.services.post import PostService

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
@login_required
async def create_post(
    body: PostCreation,
    service: Annotated[PostService, Depends(PostService)],
    request: Request.request
):

    response = await service.create_post(
        user=request.current_user,
        message=body.message
    )

    return {'post': response}



@router.get("/all-posts")
async def allposts(service: Annotated[PostService, Depends(PostService)]):
    response = await service.get_all_posts()

    return {'users': response}

@router.get('/{user_id}')
async def get_user_posts(user_id: int, service: Annotated[PostService, Depends(PostService)]):
    response = await service.get_users_posts(user_id)

    return {"posts": response}