from enum import Enum

class StatusEvent(Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CANCELED = "CANCELED"
