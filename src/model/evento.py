from pydantic import BaseModel, model_validator, AnyUrl
from typing import Union, Tuple, Optional
from datetime import datetime
from src.model.tipo_evento import TipoEvento

class Evento(BaseModel):
    titulo: str
    ubicacion: Optional[str] = None
    descripcion: str
    fecha: str # Permite una fecha única o un rango de fechas: Union[datetime, Tuple[datetime, datetime]]
    tipo:  str #Un enumerado nuestro: Optional[TipoEvento] = None
    proveedor: str
    urlPublicacion: AnyUrl #para validar que es una url correcta
    imagen: Optional[str] = None

    @model_validator(mode="before")
    def check_date_range(cls, values):
        fecha = values.get('fecha')
        if isinstance(fecha, tuple):
            if len(fecha) != 2:
                raise ValueError(
                    'El formato del rango de fechas es incorrecto. Asegúrese de que ambas fechas son correctas.')
            start_date, end_date = fecha
            if start_date >= end_date:
                raise ValueError('La fecha de comienzo debe ser anterior a la fecha de finalización.')
        return values
