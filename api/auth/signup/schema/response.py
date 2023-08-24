from pydantic import BaseModel, ConfigDict


class UserResponseSchema(BaseModel):
    age: int
    name: str
    last_name: str
    email: str
    model_config = ConfigDict()
