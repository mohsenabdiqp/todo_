from database import Base
from sqlalchemy.types import Boolean , Integer , String , DateTime
from sqlalchemy import Column


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer , primary_key = True , index = True)
    title = Column(String)
    status = Column(Boolean , default = False)
    created = Column(Integer)
    deadline = Column(Integer)
    time_left = Column(Integer , default = 0)