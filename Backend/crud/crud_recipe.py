from crud.base import CRUDBase
from db.schemas import Todo, Child
from db.models import TodoList


class CRUDRecipe(CRUDBase[TodoList, Todo, Todo]):
    ...


recipe = CRUDRecipe(TodoList)