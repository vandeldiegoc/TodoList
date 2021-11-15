from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())




class TodoList(Base):
    id = Column(Integer(), primary_key= True, index=True)
    title = Column(String(50), nullable=False)
    complated = Column(Boolean())

