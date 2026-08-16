
from sqlalchemy.orm import Session
from ..models.event import Event
from ..schemas.event import CreateEvent
from enum import Enum

from ..repositories.event_repository import EventRepository


class EventService:
    def __init__(self, db: Session):
        self.repository = EventRepository(db)

    def find_all(self) -> list:
        return self.repository.find_all()

    def create(self, create_event: CreateEvent) -> Event:
        event = Event(
            title=create_event.title,
            description=create_event.description,
            date_time=create_event.date_time,
            location=create_event.location,
            capacity=create_event.capacity,
            status="PENDENT" #TODO: criar um enum para status do evento
        )

        return self.repository.create(event)