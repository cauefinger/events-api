from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    location = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=False)
    capacity = Column(Integer, nullable=False)
    status = Column(String, nullable=False, index=True)