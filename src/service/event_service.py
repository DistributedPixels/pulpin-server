from typing import List
from src.model.event import Event
from src.db.event_repository import EventRepository

class EventService:
    def __init__(self):
        self.repository = EventRepository()

    def add_event(self, event_data: Event) -> Event:
        return self.repository.add_event(event_data)

    def get_events(self) -> List[Event]:
        return self.repository.get_all_events()
