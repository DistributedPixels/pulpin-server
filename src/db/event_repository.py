from .connection import Connection
from src.model.event import Event
from typing import List


class EventRepository:
    EVENTS_TABLE = "events"

    def __init__(self):
        self.connection = Connection()

    def add_event(self, event: Event) -> Event:
        try:
            event_data = self.connection.table(self.EVENTS_TABLE) \
                .insert(event.model_dump(exclude_none=True)) \
                .execute()
            return Event(**event_data.data[0])
        except Exception as e:
            raise e

    def get_all_events(self) -> List[Event]:
        try:
            event_data = self.connection.table(self.EVENTS_TABLE) \
                .select("*") \
                .execute()
            return [Event(**event) for event in event_data.data]

        except Exception as e:
            raise e
