from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from core.security.password import verify_password
from core.security.jwt import create_access_token
from core.config.jwt import JwtConfig
from database.connection import users_collection


class LoginController:
    async def login(form_data: OAuth2PasswordRequestForm):
        user = await users_collection.find_one({"username": form_data.username})
        if not user:
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )
        if not verify_password(form_data.password, user["hashed_password"]):
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )
        return {
            "access_token": create_access_token(data={"sub": user["username"]}),
            "expire": {"minutes": JwtConfig.ACCESS_TOKEN_EXPIRE_MINUTES},
        }
