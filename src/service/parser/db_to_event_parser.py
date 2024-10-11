from src.db.model import EventDB
from src.model.event import Event

class DBToEventParser:
    @staticmethod
    def parse(event_db: EventDB) -> Event:
        """Convert EventDB (SQLAlchemy) to Event (Pydantic)."""
        return Event(
            title=event_db.title,
            description=event_db.description,
            location=event_db.location,
            start_date=event_db.start_date,
            end_date=event_db.end_date,
            type=event_db.type,
            provider=event_db.provider,
            external_url=event_db.external_url,
            image_url=event_db.image_url
        )
