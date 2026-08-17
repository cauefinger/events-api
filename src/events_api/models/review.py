import uuid
from ..database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey

 
class Review(Base):
    __tablename__ = "review"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    eventId = Column(UUID(as_uuid=True), ForeignKey("event.id"), index=True)
    userId = Column(UUID(as_uuid=True),ForeignKey("user.id"),index=True)
    rating = Column(Integer, index=True)
    comment = Column(String, index=True)
   
