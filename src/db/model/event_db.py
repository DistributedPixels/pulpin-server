from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Base class for SQLAlchemy models
Base = declarative_base()

class EventDB(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    type = Column(String, nullable=True)
    provider = Column(String, nullable=False)
    external_url = Column(String, nullable=False)
    image_url = Column(String, nullable=True)