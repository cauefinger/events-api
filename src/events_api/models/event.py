


from ..database import Base
from sqlalchemy import Column, Integer, String

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)
    location = Column(String, unique=True, index=True)
    date = Column(Integer, primary_key=True, index=True)
    capacity = Column(Integer, unique=True, index=True)
    status = Column(String, unique=True, index=True)


    def __init__(self, id:Integer, title: String, description: String, location: String, date: Integer, capacity:Integer, status: String):
        self.id = id
        self.title = title
        self.description = description
        self.location = location
        self.date = date
        self.capacity = capacity
        self.status = status
    