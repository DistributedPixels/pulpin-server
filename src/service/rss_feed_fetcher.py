import feedparser
import httpx

class RSSFeedFetcher:

    def __init__(self, feed_url: str):
        self.feed_url = feed_url

    async def fetch_feed(self):
        """
        Hace una solicitud HTTP para obtener el contenido del feed RSS.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(self.feed_url)
        return response.text

    def parse_feed(self, feed_content: str):
        """
        Analiza el contenido del feed RSS y extrae los eventos.
        """
        feed = feedparser.parse(feed_content)
        events = []

        for entry in feed.entries:
            event = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "description": entry.description,
            }
            events.append(event)
            # Mostrar el evento en consola
            print(f"Título: {entry.title}")
            print(f"Link: {entry.link}")
            print(f"Publicado: {entry.published}")
            print(f"Descripción: {entry.description}")
            print("-" * 40)

        return events

    async def get_events(self):
        """
        Método público que obtiene los eventos del feed RSS.
        """
        feed_content = await self.fetch_feed()
        events = self.parse_feed(feed_content)
        return events