from typing import List

from src.model.event import Event
from src.service.event_service import EventService


class EventController:
    def __init__(self):
        self.service = EventService()

    def get_events(self) -> List[Event]:
        return self.service.get_events()

    def add_event(self, event_data: Event) -> Event:
        return self.service.add_event(event_data)
