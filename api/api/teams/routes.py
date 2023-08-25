from typing import Annotated
from core.security.auth import User, get_current_user
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.post(
    "/join/", response_model=None, summary="authenticated user can join  on tams"
)
async def join_on_teams(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user.username
