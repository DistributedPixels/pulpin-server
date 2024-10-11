from .connection import Connection
from .model import EventDB, Base

class EventRepository:
    def __init__(self):
        self.connection = Connection()

    def create_tables(self):
        """Create all tables in the database."""
        Base.metadata.create_all(self.connection._engine)

    def add_event(self, event: EventDB):
        session = self.connection.get_session()
        try:
            session.add(event)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_events(self):
        session = self.connection.get_session()
        try:
            events = session.query(EventDB).all()
            return events
        except Exception as e:
            raise e
        finally:
            session.close()
