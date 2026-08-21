from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from events_api.dependencies.get_session import get_session
from events_api.models.ticket import Ticket
from events_api.services.ticket_service import ticket, buy_tickets

ticket_router = APIRouter(prefix="/tickets")

@ticket_router.get("/")
async def view_tickets(session: Session = Depends(get_session)):
    amount = session.query(Ticket).filter(Ticket.buyer_id.is_(None)).count()
    return {"available_tickets": amount}


@ticket_router.post("/buy/{ticket_id}")
async def buy_ticket(
    ticket_id: int,
    session: Session = Depends(get_session)
):
    return await buy_tickets