from enum import Enum

#TODO: Criar status ENDED para quando o evento acabou
class StatusEvent(Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CANCELED = "CANCELED"
