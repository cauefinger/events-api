
from ..database import Base
from sqlalchemy import Column, Integer, String, Float, Enum
from ..enums.status_ticket import Status_Ticket

class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, index=True)
    eventId = Column(String, unique=True, index=True)
    userId = Column(String, unique=True, index=True)
    type = Column(String, unique=True, index=True)
    price = Column(Integer, primary_key=True, index=True)
    status = Column(
        Enum(Status_Ticket),
          default=Status_Ticket.PENDING
          )

