from fastapi import APIRouter, status
from .schema import UserResponseSchema, UserCreateSchema
from .controller import SignUpController
from database.model import User

signup_controller = SignUpController(User)
router = APIRouter(tags=["Signup"])


@router.post(
    "/signup/",
    status_code=status.HTTP_200_OK,
    response_model=UserResponseSchema,
    summary="Return user information",
)
async def signup(body: UserCreateSchema):
    return await signup_controller.create(body)
