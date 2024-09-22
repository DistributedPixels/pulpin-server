from enum import Enum

class EventType(str, Enum):
    CONCERT = "Concierto"
    FESTIVAL = "Festival"
    SEMINAR = "Seminario"
    WORKSHOP = "Workshop"
    EXHIBITION = "Exhibición"
    OTHER = "Otro"
