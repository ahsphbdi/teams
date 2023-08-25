from fastapi import APIRouter
from .auth import auth_router
from .api import auth_needed_api_routers

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(auth_needed_api_routers)
