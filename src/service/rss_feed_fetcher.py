import httpx
from typing import Type, List, Dict
from src.service.parser.parser_interface import IParserEvent

class RSSFeedFetcher:
    @staticmethod
    async def _fetch_feed(feed_url: str) -> str: #el _ es para indicar que es privado
        async with httpx.AsyncClient() as client:
            response = await client.get(feed_url)
        return response.text

    @staticmethod
    async def get_events(feed_url: str, parser: Type['IParserEvent']) -> List[Dict[str, str]]:
        """
        Método que recibe la url del RSS y el parser correspondiente y devuelve la lista de eventos

        :param feed_url: URL del feed de RSS
        :param parser: Parser correspondiente
        :return: Lista de eventos obtenidos del feed y parser.
        """
        feed_content = await RSSFeedFetcher._fetch_feed(feed_url)
        events = parser.parse_feed(feed_content)
        return events
