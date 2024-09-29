from typing import Optional

from pydantic import BaseModel, AnyUrl


class Event(BaseModel):
    title: str
    description: str
    location: Optional[str] = None
    start_date: str
    end_date: str
    type: str
    provider: str
    url: AnyUrl  # para validar que es una url correcta
    image: Optional[str] = None
