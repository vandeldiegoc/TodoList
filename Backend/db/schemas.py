from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from db.models import Child


class Users(BaseModel):
    id = int
    username = str
    email = str
    created_at = datetime
    child_id = int
    Child = int
    

class Child(BaseModel):
    id = int

class Todo(BaseModel):
    id : int
    title: str
    complated: bool = False


class TodoUpdate(BaseModel):
    title: Optional[str]
    complated: Optional[bool] = False
    

""" class Update """