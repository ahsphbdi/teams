from enum import IntEnum, EJECT
from typing import Annotated
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from core.config.jwt import JwtConfig
from database.connection import users_collection


class UserRole(IntEnum):
    ADMIN: int = 2
    NORMAL: int = 3


class User(BaseModel):
    age: int
    name: str
    username: str
    last_name: str
    email: str
    role: UserRole
    model_config = ConfigDict()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_user(username) -> User:
    user = await users_collection.find_one({"username": username})
    return User(**user)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, JwtConfig.SECRET_KEY, algorithms=[JwtConfig.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(username=username)
    if user is None:
        raise credentials_exception
    return user


async def get_admin_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.role == UserRole.ADMIN:
        return current_user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="access denied")
