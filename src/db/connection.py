import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    _instance = None
    _engine = None
    _Session = None

    def __new__(cls):
        if cls._instance is None:
            url = os.getenv("TURSO_DATABASE_URL")
            auth_token = os.getenv("TURSO_AUTH_TOKEN")
            connection_string = f"{url}?auth_token={auth_token}"

            cls._instance = super(Connection, cls).__new__(cls)
            cls._engine = create_engine(connection_string)
            cls._Session = sessionmaker(bind=cls._engine)
        return cls._instance

    def get_session(self):
        """Returns a new session to interact with data base"""
        return self._Session()

    def __del__(self):
        self.close()

