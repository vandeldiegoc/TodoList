from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import PrimaryKeyConstraint

Base = declarative_base()

engine = create_engine('postgresql://postgres@localhost/Todo')
class Use(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

Session = sessionmaker(engine)
session = Session()

Base.metadata.create_all(engine)