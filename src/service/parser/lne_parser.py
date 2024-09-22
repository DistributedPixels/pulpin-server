import xml.etree.ElementTree as ET
from src.service.parser.parser_interface import IParserEvent
from src.model.event import Event


class LNEParserEvent(IParserEvent):
    @staticmethod
    def parse_feed(feed_content: str):
        events = []
        # Parsear el contenido XML del feed
        root = ET.fromstring(feed_content)

        # Definir el namespace para media:content
        namespaces = {'media': 'http://search.yahoo.com/mrss/'}

        # Obtener elementos de la etiqueta item
        for item in root.findall('.//item'):
            # Extraer información de la etiqueta media:content
            media_thumbnail = item.find('media:thumbnail', namespaces)
            url_image = media_thumbnail.attrib['url'] if media_thumbnail is not None else ''

            event = Event(
                title=item.find('title').text,
                location='',
                description=item.find('description').text,
                date='',
                type='',
                provider='La Nueva España',
                url=item.find('link').text or '',
                image=url_image
            )
            events.append(event)

        return events
