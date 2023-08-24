from pydantic import (
    BaseModel,
    ConfigDict,
    constr,
    EmailStr,
    root_validator,
    field_validator,
    validator,
)
from fastapi.exceptions import ValidationException


class UserSignupRequestSchema(BaseModel):
    age: int
    name: constr(min_length=3, max_length=255)
    last_name: constr(min_length=3, max_length=255)
    email: EmailStr
    password1: constr(min_length=8)
    password2: constr(min_length=8)
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "age": 24,
                "name": "amir",
                "last_name": "espahbodi",
                "email": "ah.espahbodi@gmail.com",
                "password1": "secret-12",
                "password2": "secret-12",
            }
        }
    )

    @validator("password1", "password2")
    @classmethod
    def password_checker(cls, value: str) -> str:
        contain_numbers = False
        contain_lower = False
        contain_upper = False
        other = False
        for char in value:
            if char.isdigit():
                contain_numbers = True
            elif char.isalpha():
                if char.isupper():
                    contain_upper = True
                else:
                    contain_lower = True
            else:
                other = True
        if not (contain_lower and contain_upper and other and contain_numbers):
            raise ValueError(
                [
                    "password must contain lower and upper case character and number and one ore more other"
                ]
            )

        return value

    @root_validator(pre=True)
    def check_password_equal(cls, values):
        if values["password1"] != values["password2"]:
            raise ValueError(["two password must be equal"])
        return values
