# session = Session()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base


SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:vda@localhost/Todo'


engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    #connect_args={"check_same_thread": False},
)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
