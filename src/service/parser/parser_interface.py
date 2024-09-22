#En Python no hay interfaces como tal, así que hay que hacer esta trampilla

from abc import ABC, abstractmethod
from typing import List, Dict
from src.model.evento import Evento

class IParserEvento(ABC): #ABC para convertirlo en una clase abstracta
    @abstractmethod
    def parse_feed(feed_content: str) -> List[Evento]:
        """
        Metodo abstracto para parsear un string a una lista de elementos. Debe ser implementado por las subclases.
        """
        pass
