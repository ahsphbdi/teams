from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from pymongo.errors import DuplicateKeyError
from core.repository.crud import BaseCRUD
from database.connection import users_collection
from core.security import get_password_hash
from .schema import UserCreateSchema


class SignUpController:
    def __init__(self, model):
        self.model = model

    async def create(self, body: UserCreateSchema):
        hashed_password = get_password_hash(body.password1)
        user_data = jsonable_encoder(
            {
                "age": body.age,
                "name": body.name,
                "last_name": body.last_name,
                "email": body.email,
                "hashed_password": hashed_password,
            }
        )
        try:
            await users_collection.insert_one(user_data)
        except DuplicateKeyError:
            raise HTTPException(
                detail="user with this email address alredy registered",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return {
            "age": body.age,
            "name": body.name,
            "last_name": body.last_name,
            "email": body.email,
        }
