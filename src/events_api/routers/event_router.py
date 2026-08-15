from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..services.event_service import EventService
from ..schemas.event import CreateEvent

event_router = APIRouter(prefix="/events")

def get_event_service(db: Session = Depends(get_db)) -> EventService:
    return EventService(db)

@event_router.get("/")
async def find_all(event_service: EventService = Depends(get_event_service)):
    return event_service.find_all()

@event_router.get("/{event_id}")
async def find_by_id(event_id: int, event_service: EventService = Depends(get_event_service)):
    return event_service.find_by_id(event_id)

@event_router.post("/")
async def create_event(event: CreateEvent, event_service: EventService = Depends(get_event_service)):
    return event_service.create(event)