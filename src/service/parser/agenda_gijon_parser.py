import re
from datetime import datetime

from src.model.event import Event
from src.service.parser.event_parser import EventParser


class AgendaGijonParser(EventParser):
    date_re = re.compile(r"(\d{4}-\d{2}-\d{2})")
    base_external_url = "https://www.gijon.es/es/eventos"
    base_image_url = "https://www.gijon.es"

    def parse(self, raw_event: dict):
        dates = self.date_re.findall(raw_event["fechas"])
        start_date = datetime.strptime(dates[0], "%Y-%m-%d")
        end_date = start_date
        if len(dates) > 1:
            end_date = datetime.strptime(dates[1], "%Y-%m-%d")
        return Event(title=raw_event["titulo"],
                     location="Gijón",
                     start_date=start_date,
                     end_date=end_date,
                     provider="Agenda Gijón",
                     external_url=f"{self.base_external_url}{raw_event['alias']}",
                     image_url=f"{self.base_image_url}{raw_event['imagen']}")
