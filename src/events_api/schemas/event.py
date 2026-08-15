from pydantic import BaseModel
from datetime import datetime

class CreateEvent(BaseModel):
    title: str
    description: str
    date_time: datetime
    location: str
    capacity: int
    