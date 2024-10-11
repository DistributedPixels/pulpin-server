from typing import List

from src.model.event import Event
from src.service.event_service import EventService


class EventController:
    def __init__(self):
        self.service = EventService()

    async def get_events(self) -> List[Event]:
        return await self.service.get_events()
