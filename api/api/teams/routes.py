from typing import Annotated
from bson import ObjectId
from fastapi import APIRouter, Depends
from core.security.auth import User, get_current_user, get_admin_user
from .controller import TeamsController as teams_controller
from .schema import (
    TeamCreateSchema,
    TeamResponseSchema,
    TeamUpdateScema,
    TeamListResponseSchema,
)


router = APIRouter(prefix="/teams", tags=["Teams"])


@router.get(
    "/get/{t_id}/",
    response_model=TeamResponseSchema,
    summary="authenticated user can get information of a",
)
async def get_team(
    t_id: Annotated[str, ...],
):
    return await teams_controller.get_team(t_id)


@router.get(
    "/list/",
    response_model=list[TeamListResponseSchema],
    summary="authenticated user can get list of teams",
)
async def get_teams(
    skip: int = 0,
    limit: int = 100,
):
    return await teams_controller.get_teams(skip, limit)


@router.post(
    "/create/",
    response_model=TeamResponseSchema,
    summary="admin user can create teams",
)
async def create_team(
    current_user: Annotated[User, Depends(get_admin_user)],
    body: Annotated[TeamCreateSchema, ...],
):
    return await teams_controller.create_team(body)


@router.put(
    "/update/{t_id}/",
    response_model=TeamResponseSchema,
    summary="admin user can update teams",
)
async def update_team(
    current_user: Annotated[User, Depends(get_admin_user)],
    t_id: Annotated[str, ...],
    body: Annotated[TeamUpdateScema, ...],
):
    return await teams_controller.update_team(body=body, t_id=t_id)


@router.delete(
    "/delete/{t_id}/",
    summary="admin user can delete teams",
)
async def delete_team(
    current_user: Annotated[User, Depends(get_admin_user)],
    t_id: Annotated[str, ...],
):
    return await teams_controller.delete_team(t_id=t_id)


@router.post(
    "{t_id}/join/", response_model=None, summary="authenticated user can join  on tams"
)
async def join_on_team(
    current_user: Annotated[User, Depends(get_current_user)], t_id: Annotated[str, ...]
):
    return await teams_controller.join_on_team(t_id, current_user)
