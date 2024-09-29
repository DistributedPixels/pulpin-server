from pydantic import BaseModel, model_validator, AnyUrl
from typing import Union, Tuple, Optional
from datetime import datetime
from src.model.event_type import EventType

class Event(BaseModel):
    title: str
    location: Optional[str] = None
    description: str
    date: str # Permite una date única o un rango de fechas: Union[datetime, Tuple[datetime, datetime]]
    type:  str #Un enumerado nuestro: Optional[EventType] = None
    provider: str
    url: AnyUrl #para validar que es una url correcta
    image: Optional[str] = None

    @model_validator(mode="before")
    def check_date_range(cls, values):
        fecha = values.get('date')
        if isinstance(fecha, tuple):
            if len(fecha) != 2:
                raise ValueError(
                    'The format of the date range is incorrect. Make sure both dates are correct.')
            start_date, end_date = fecha
            if start_date >= end_date:
                raise ValueError('The start date must be before the end date.')
        return values
