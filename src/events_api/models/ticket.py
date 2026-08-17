import uuid
from ..database import Base
from sqlalchemy import Column, Integer, String, Float, Enum
from ..enums.status_ticket import Status_Ticket
from sqlalchemy.dialects.postgresql import UUID

# TODO: usar foreignkey no user id, event id


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    eventId = Column(UUID(as_uuid=True),index=True)
    userId = Column(UUID(as_uuid=True), index=True)
    type = Column(String, index=True)
    price = Column(Integer, index=True)
    status = Column(
        Enum(Status_Ticket),
          default=Status_Ticket.PENDING
          )

