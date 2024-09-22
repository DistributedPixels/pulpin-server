import xml.etree.ElementTree as ET
from src.service.parser.parser_interface import IParserEvento
from src.model.evento import Evento


class LNEParserEvento(IParserEvento):
    @staticmethod
    def parse_feed(feed_content: str):
        eventos = []
        # Parsear el contenido XML del feed
        root = ET.fromstring(feed_content)

        # Definir el namespace para media:content
        namespaces = {'media': 'http://search.yahoo.com/mrss/'}

        # Obtener elementos de la etiqueta item
        for item in root.findall('.//item'):
            # Extraer información de la etiqueta media:content
            media_thumbnail = item.find('media:thumbnail', namespaces)
            imagen_url = media_thumbnail.attrib['url'] if media_thumbnail is not None else ''

            evento = Evento(
                titulo=item.find('title').text,
                ubicacion='',
                descripcion=item.find('description').text,
                fecha='',
                tipo='',
                proveedor='La Nueva España',
                urlPublicacion=item.find('link').text or '',
                imagen=imagen_url
            )
            eventos.append(evento)

        return eventos
