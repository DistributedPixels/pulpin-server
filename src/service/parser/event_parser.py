from abc import ABC, abstractmethod


class EventParser(ABC):
    @abstractmethod
    def parse(self, raw_event: dict):
        raise NotImplementedError()
