from pydantic import BaseModel, ConfigDict, Field
from core.schema.py_objectid import PyObjectId


class TeamCreateSchema(BaseModel):
    title: str
    model_config = ConfigDict(
        json_schema_extra={"example": {"title": "back-end"}},
    )


class TeamUpdateScema(TeamCreateSchema):
    pass
