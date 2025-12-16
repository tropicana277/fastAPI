from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    user_id: str
    name: str
    email: str


class User(UserCreate):
    created_at: datetime
