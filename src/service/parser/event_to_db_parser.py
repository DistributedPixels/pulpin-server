from src.db.model import EventDB
from src.model.event import Event

class EventToDBParser:
    @staticmethod
    def parse(event: Event) -> EventDB:
        """Convert Event (Pydantic) to EventDB (SQLAlchemy)."""
        return EventDB(
            title=event.title,
            description=event.description,
            location=event.location,
            start_date=event.start_date,
            end_date=event.end_date,
            type=event.type,
            provider=event.provider,
            external_url=str(event.external_url),
            image_url=str(event.image_url) if event.image_url else None
        )
