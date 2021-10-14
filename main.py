from fastapi import FastAPI, HTTPException
from models import Todo, TodoIn_Pydantic, Todo_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel

class Message(BaseModel):
    message: str

app = FastAPI()

@app.get('/')
async def read_root():
    return {"Hello": "World"}

