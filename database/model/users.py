from typing import Any
from beanie import Document


class User(Document):
    age: int
    name: str
    last_name: str
    email: str
    role: int
