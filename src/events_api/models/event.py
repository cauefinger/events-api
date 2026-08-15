
from ..database import Base
from sqlalchemy import Column, Integer, String, SQLAlchemyEnum
from enum import Enum

class StatusEvent(Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CANCELED = "CANCELED"


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, unique=True, index=True)
    location = Column(String, unique=True, index=True)
    date = Column(Integer, primary_key=True, index=True)
    capacity = Column(Integer, unique=True, index=True)
    status = Column(
        SQLAlchemyEnum(StatusEvent),
          default=StatusEvent.PENDING
          )


    def __init__(self, id:Integer, title: String, description: String, location: String, date: Integer, capacity:Integer, status: StatusEvent):
        self.id = id
        self.title = title
        self.description = description
        self.location = location
        self.date = date    
        self.capacity = capacity
        self.status = StatusEvent
    