from fastapi import APIRouter, status
from .schema import UserResponseSchema, UserCreateSchema
from .controller import SignUpController as signup_controller
from database.model import User

router = APIRouter(tags=["Signup"])


@router.post(
    "/signup/",
    status_code=status.HTTP_200_OK,
    response_model=UserResponseSchema,
    summary="Return user information",
)
async def signup(body: UserCreateSchema):
    return await signup_controller.create(body)
