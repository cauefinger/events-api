import uuid
from ..database import Base
from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from ..enums.status_ticket import Status_Ticket
from sqlalchemy.dialects.postgresql import UUID



class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    eventId = Column(UUID(as_uuid=True),ForeignKey("event.id"), index=True)
    userId = Column(UUID(as_uuid=True),ForeignKey("user.id"), index=True)
    type = Column(String, index=True)
    price = Column(Integer, index=True)
    status = Column(Enum(Status_Ticket), default=Status_Ticket.PENDING)

