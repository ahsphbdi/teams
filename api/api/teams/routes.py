from typing import Annotated
from core.security.auth import User, get_current_user, get_admin_user
from fastapi import APIRouter, Depends
from .controller import TeamsController as teams_controller
from .schema import TeamCreateSchema, TeamResponseSchema, TeamUpdateScema


router = APIRouter(prefix="/teams", tags=["Teams"])


@router.get(
    "/get/{t_id}/",
    response_model=TeamResponseSchema,
    summary="authenticated user can join  on tams",
)
async def get_team(
    current_user: Annotated[User, Depends(get_current_user)], t_id: Annotated[str, ...]
):
    return await teams_controller.get_team(t_id)


@router.get(
    "/list/",
    response_model=list[TeamResponseSchema],
    summary="authenticated user can join  on tams",
)
async def get_teams(
    current_user: Annotated[User, Depends(get_current_user)],
    skip: int = 0,
    limit: int = 100,
):
    return await teams_controller.get_teams(skip, limit)


@router.post(
    "/create/",
    response_model=TeamResponseSchema,
    summary="authenticated user can join  on tams",
)
async def create_team(
    current_user: Annotated[User, Depends(get_admin_user)],
    body: Annotated[TeamCreateSchema, ...],
):
    return await teams_controller.create_team(body)


@router.put(
    "/update/{t_id}/",
    response_model=TeamResponseSchema,
    summary="authenticated user can join  on tams",
)
async def update_team(
    current_user: Annotated[User, Depends(get_admin_user)],
    body: Annotated[TeamUpdateScema, ...],
):
    return current_user.username


@router.delete(
    "/delete/{t_id}/",
    summary="authenticated user can join  on tams",
)
async def delete_team(current_user: Annotated[User, Depends(get_admin_user)]):
    return {"message": "ok"}


@router.post(
    "/join/", response_model=None, summary="authenticated user can join  on tams"
)
async def join_on_team(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user.username
