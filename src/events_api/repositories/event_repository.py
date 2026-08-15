from sqlalchemy.orm import Session
from ..models.event import Event


class EventRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self) -> list[Event]:
        return self.db.query(Event).all()

    def find_by_id(self, event_id: int) -> Event | None:
        return self.db.query(Event).filter(Event.id == event_id).first()

    def create(self, event: Event) -> Event:
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event