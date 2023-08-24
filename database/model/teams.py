from typing import Any
from beanie import Document, Link

from database.model.users import User


class Team(Document):
    title: str
    members: list[Link[User]]
