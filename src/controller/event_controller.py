from typing import List

from src.model.event import Event
from src.service.api_consumer_service import ApiConsumerService
from src.service.parser import AgendaGijonParser


class EventController:
    @staticmethod
    async def get_events() -> List[Event]:
        url = "https://drupal.gijon.es/es/listado_eventos_tes3/?_format=json"
        return ApiConsumerService.consume(url, AgendaGijonParser())
