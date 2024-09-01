from typing import List, Optional
from src.model.evento import Evento
from src.db.db_temporal import db_temporal, get_lne_rss_eventos

class ControladorEvento:
    @staticmethod
    async def get_eventos() -> List[Evento]:
        return await get_lne_rss_eventos()

    @staticmethod
    def get_evento(id_evento: int) -> Optional[Evento]:
        return db_temporal.get(id_evento)

    @staticmethod
    def crea_evento(evento: Evento) -> Evento:
        id_evento = len(db_temporal) + 1
        db_temporal[id_evento] = evento
        return evento

    @staticmethod
    def actualiza_evento(id_evento: int, evento_actualizado: Evento) -> Optional[Evento]:
        if id_evento in db_temporal:
            db_temporal[id_evento] = evento_actualizado
            return evento_actualizado
        return None

    @staticmethod
    def elimina_evento(id_evento: int) -> bool:
        if id_evento in db_temporal:
            del db_temporal[id_evento]
            return True
        return False
