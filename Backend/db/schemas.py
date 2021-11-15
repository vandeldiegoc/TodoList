from datetime import datetime
from pydantic import BaseModel
from typing import Optional



class Users(BaseModel):
    id = int
    username = str
    email = str
    created_at = datetime
    child_id = int
    Child = int
    


class Todo(BaseModel):
    id : int
    title: str
    complated: bool = False


class Tod(BaseModel):
    title: str
    complated: bool = False

class TodoUpdate(BaseModel):
    title: Optional[str]
    complated: Optional[bool] = False
    

""" class Update """