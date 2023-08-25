from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .controller import LoginController as login_controller

router = APIRouter()


@router.post("/login/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return await login_controller.login(form_data)
