from pydantic import BaseModel, ConfigDict, Field
from bson import ObjectId


class TeamResponseSchema(BaseModel):
    id: ObjectId = Field(validation_alias="_id")
    title: str
    members: list[ObjectId]
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )


class TeamListResponseSchema(BaseModel):
    id: ObjectId = Field(validation_alias="_id")
    title: str
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )


class Member(BaseModel):
    name: str
    age: int


class TaskTeamResponseSchema(BaseModel):
    title: str
    members: list[Member] | Member
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        json_encoders={ObjectId: str},
    )
