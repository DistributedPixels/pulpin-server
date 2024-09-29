from typing import List, Optional
from src.model.event import Event
from src.db.db_temporal import db_temporal, get_lne_rss_events

class EventController:
    @staticmethod
    async def get_events() -> List[Event]:
        return await get_lne_rss_events()

    @staticmethod
    def get_event(event_id: int) -> Optional[Event]:
        return db_temporal.get(event_id)

    @staticmethod
    def create_event(event: Event) -> Event:
        event_id = len(db_temporal) + 1
        db_temporal[event_id] = event
        return event

    @staticmethod
    def update_event(event_id: int, updated_event: Event) -> Optional[Event]:
        if event_id in db_temporal:
            db_temporal[event_id] = updated_event
            return updated_event
        return None

    @staticmethod
    def delete_event(event_id: int) -> bool:
        if event_id in db_temporal:
            del db_temporal[event_id]
            return True
        return False
