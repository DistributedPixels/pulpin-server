from pydantic import BaseModel, model_validator, AnyUrl
from typing import Union, Tuple
from datetime import datetime
from tipo_evento import TipoEvento

class Evento(BaseModel):
    titulo: str
    ubicacion: str
    descripcion: str
    fecha: Union[datetime, Tuple[datetime, datetime]]  # Permite una fecha única o un rango de fechas
    tipo: TipoEvento #Un enumerado nuestro
    proveedor: str
    urlPublicacion: AnyUrl #para validar que es una url correcta
    imagen: str

    @model_validator
    def check_date_range(cls, values):
        fecha = values.get('fecha')
        if isinstance(fecha, tuple): # si es un rango
            if len(fecha) != 2: #y no tiene sólo 2 fechas correctas
                raise ValueError(
                    'El formato del rango de fechas es incorrecto. Asegúrese de que ambas fechas son correctas.')
            start_date, end_date = fecha
            if start_date >= end_date: #y el rango no es físicamente posible
                raise ValueError('La fecha de comienzo debe ser anterior a la fecha de finalización.')
        return values
