from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from events_api.dependencies.get_session import get_session
from events_api.models.ticket import Ticket

ticket_router = APIRouter(prefix="/tickets")

@ticket_router.get("/")
async def visualizar_tickets(session: Session = Depends(get_session)):
    quantidade = session.query(Ticket).filter(Ticket.buyer_id.is_(None)).count()
    return {"tickets_disponiveis": quantidade}

