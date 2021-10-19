from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from db.schemas import Todo, TodoUpdate
from sqlalchemy.orm import Session, session
from db.deps import get_db
from crud.crud_recipe import recipe

class Message(BaseModel):
    message: str

app = FastAPI()

@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.get('/task/{id}')
def task(
    db: session = Depends(get_db), id = id):
    task = recipe.getTask(db, id)
    return task


@app.post('/create', status_code=201, response_model=Todo)
def creaate_todo(
    *, todo_S:Todo, db: Session = Depends(get_db)
    ):
    todo = recipe.create(db=db, obj_in=todo_S)
    return todo

@app.put('/create', status_code=201, response_model=TodoUpdate)
def update_todo(id: int, todo_u: TodoUpdate, db: session = Depends(get_db)
    ):
    todo  = recipe.update(db=db, obj_in=todo_u, id=id)
    return todo


@app.delete("/delete")
async def delete(
    id: int,
    session = Depends(get_db)
    ):
    """resive id task and delete task in databases"""
    recipe.delete_task(id, session)
    return ('Done')


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")