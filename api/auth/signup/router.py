from fastapi import APIRouter, status
from .schema import UserResponseSchema, UserSignupRequestSchema

router = APIRouter(tags=["Register"])


@router.post(
    "/signup/",
    status_code=status.HTTP_200_OK,
    response_model=UserResponseSchema,
    summary="Return user information",
)
async def signup(body: UserSignupRequestSchema):
    return {
        "age": body.age,
        "name": body.name,
        "last_name": body.last_name,
        "email": body.email,
    }
