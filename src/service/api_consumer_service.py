from typing import List

import requests

from src.model.event import Event
from src.service.parser import EventParser


class ApiConsumerService:
    @staticmethod
    def consume(url: str, parser: EventParser) -> List[Event]:
        response = requests.get(url)
        events: List[Event] = list(map(lambda raw_event: parser.parse(raw_event), response.json()))
        return events
