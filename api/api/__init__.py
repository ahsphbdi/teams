from fastapi import APIRouter, Depends
from core.security.auth import get_current_user
from .teams.routes import router as team_router

auth_needed_api_routers = APIRouter(dependencies=[Depends(get_current_user)])

auth_needed_api_routers.include_router(team_router)
