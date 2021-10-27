from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from db.base_class import Base


class User(Base):
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())
    child_id = Column(Integer, ForeignKey('child.id'))
    Child = relationship("Child")

class Child(Base):
    id = Column(Integer, primary_key=True)




class TodoList(Base):
    id = Column(Integer(), primary_key= True, index=True)
    title = Column(String(50), nullable=False)
    complated = Column(Boolean())

