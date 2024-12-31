from typing import Optional

from pydantic import BaseModel


class Event(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: str
    end_date: str
    type: Optional[str] = None
    provider: str
    external_url: str  # para validar que es una url correcta
    image_url: Optional[str] = None
