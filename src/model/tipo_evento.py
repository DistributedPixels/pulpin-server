from enum import Enum

class TipoEvento(str, Enum):
    CONCIERTO = "Concierto"
    FESTIVAL = "Festival"
    SEMINARIO = "Seminario"
    WORKSHOP = "Workshop"
    EXHIBICION = "Exhibición"
    OTRO = "Otro"
