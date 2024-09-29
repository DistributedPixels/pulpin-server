from src.service.rss_feed_fetcher import RSSFeedFetcher
from src.service.parser.lne_parser import LNEParserEvent
from typing import List
from src.model.event import Event

RSS_FEED_URL = "https://www.lne.es/rss/section/2014085"
rss_fetcher = RSSFeedFetcher()

db_temporal = {}

async def get_lne_rss_events() ->List[Event]: #para probar, hay que hacer un flow para que esto llegue a bbdd
    events = await rss_fetcher.get_events(RSS_FEED_URL, LNEParserEvent)
    return events