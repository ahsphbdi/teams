from pydantic import BaseModel, ConfigDict, Field
from core.schema.py_objectid import PyObjectId


class TeamResponseSchema(BaseModel):
    id: str = Field(
        validation_alias="_id"
    )  # = Field(default_factory=PyObjectId, alias="_id")
    title: str
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
