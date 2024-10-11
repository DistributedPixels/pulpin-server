from typing import List
from src.model.event import Event
from src.db.event_repository import EventRepository
from src.service.parser import DBToEventParser
from src.service.parser import EventToDBParser

class EventService:
    def __init__(self):
        self.repository = EventRepository()

    async def add_event(self, event_data: Event):
        event_db = EventToDBParser.parse(event_data)
        await self.repository.add_event(event_db)

    async def get_events(self) -> List[Event]:
        events_db = await self.repository.get_all_events()
        events = [DBToEventParser.parse(event_db) for event_db in events_db]
        return events
