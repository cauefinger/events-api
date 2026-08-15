
from ..database import Base
from sqlalchemy import Column, Integer, String, Float, SQLAlchemyEnum
from ..enums.status_ticket import Status_Ticket

class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, index=True)
    eventId = Column(String, unique=True, index=True)
    userId = Column(String, unique=True, index=True)
    type = Column(String, unique=True, index=True)
    price = Column(Integer, primary_key=True, index=True)
    status = Column(
        SQLAlchemyEnum(Status_Ticket),
          default=Status_Ticket.PENDING
          )


    def __init__(self, id:Integer, eventId: Integer, userId: Integer, type: String, price: Float, status: Status_Ticket):
        self.id = id
        self.eventId = eventId
        self.userId = userId
        self.type = type
        self.price = price
        self.status = Status_Ticket
        