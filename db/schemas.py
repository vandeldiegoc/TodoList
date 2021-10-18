from datetime import datetime
from pydantic import BaseModel
from typing import Sequence

class Users(BaseModel):
    id = int
    username = str
    email = str
    created_at = datetime


class Todo(BaseModel):
    id : int
    title: str
    complated: bool


""" class Update """