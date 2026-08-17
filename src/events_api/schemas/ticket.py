from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class TicketResponde(BaseModel):
    id: UUID
    event_id: UUID
    buyer_id: UUID | None

    class Config:
        from_attributes = True