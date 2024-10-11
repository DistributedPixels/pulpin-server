from .connection import Connection
from .model import EventDB, Base

class EventRepository:
    def __init__(self):
        self.connection = Connection()

    async def create_tables(self):
        """Create all tables in the database."""
        await Base.metadata.create_all(self.connection._engine)

    async def add_event(self, event: EventDB):
        session = self.connection.get_session()
        try:
            await session.add(event)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    async def get_all_events(self):
        session = self.connection.get_session()
        try:
            events = await session.query(EventDB).all()
            return events
        except Exception as e:
            raise e
        finally:
            session.close()
