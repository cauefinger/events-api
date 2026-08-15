
from ..database import Base
from sqlalchemy import Column, Integer, String

class Review(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    eventId = Column(Integer, unique=True, index=True)
    userId = Column(Integer, unique=True, index=True)
    rating = Column(Integer, unique=True, index=True)
    comment = Column(String, primary_key=True, index=True)
   


    def __init__(self, id:Integer, eventId: Integer, userId: Integer, rating: Integer, comment: String):
        self.id = id
        self.eventId = eventId
        self.userId = userId
        self.rating = rating
        self.comment = comment    
   
    