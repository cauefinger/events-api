from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from events_api.dependencies.get_session import get_session
from events_api.models.ticket import Ticket

ticket_router = APIRouter(prefix="/tickets")

@ticket_router.get("/")
async def visualizar_tickets(session: Session = Depends(get_session)):
    quantidade = session.query(Ticket).filter(Ticket.buyer_id.is_(None)).count()
    return {"tickets_disponiveis": quantidade}


@ticket_router.post("/comprar/{ticket_id}")
async def comprar_tickets(ticket_id: int, session: Session = Depends(get_session)):

    ticket = session.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if ticket.buyer_id is not None:
        raise HTTPException(
            status_code=400,
            detail = ("Ticket indisponível.")
        )