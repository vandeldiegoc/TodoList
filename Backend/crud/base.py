from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import session
from sqlalchemy.orm.exc import NoResultFound
from db.base_class import Base
from db.sess import SessionLocal as Session
from sqlalchemy.exc import IntegrityError

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
updateSchemaType = TypeVar("updateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, updateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model


    def getTask(self, db:Session, id: any) -> ModelType:
        try:
            task = db.query(self.model).filter(self.model.id == id).one()   
        except NoResultFound:
            raise HTTPException(status_code=406,
                                detail='id task dont found')
        return task       

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        try:
            db.add(db_obj)
            db.commit()
            return obj_in
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=405, 
                                detail="error to try insert new to do for parameter")


    def update(self, db: Session, *, obj_in: CreateSchemaType, id) -> ModelType:
        db_obj = obj_in.dict(exclude_unset=True)
        try:
            task = db.query(self.model).filter(self.model.id == id).\
            update(db_obj)
            db.commit()
            return db_obj
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=405, 
                                detail="error to try update new to do for parameter")
        


    def delete_task(self, id: int, db: Session) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
        

       