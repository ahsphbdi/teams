from fastapi import APIRouter

from .signup.router import router as signup
from .login.router import router as login

auth_router = APIRouter(prefix="/auth", tags=["Auth"])
auth_router.include_router(signup)
auth_router.include_router(login)
