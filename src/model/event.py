from datetime import datetime
from typing import Optional

from pydantic import BaseModel, AnyUrl


class Event(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: datetime
    end_date: datetime
    type: Optional[str] = None
    provider: str
    external_url: AnyUrl  # para validar que es una url correcta
    image_url: Optional[AnyUrl] = None
