from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, session
from events_api.dependencies.get_session import get_session
from events_api.models.ticket import Ticket

async def buy_tickets(ticket_id: int, session: Session = Depends(get_session)):

    ticket = session.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()




    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found."
        )

    if ticket.buyer_id is not None:
        raise HTTPException(
            status_code=400,
            detail = ("Ticket unavailable.")
        )


session.commit()