from ..service.rss_feed_fetcher import RSSFeedFetcher
from typing import List, Dict, Union
from datetime import datetime

# Initialize the RSS feed fetcher instance
RSS_FEED_URL = "https://www.lne.es/rss/section/2014085"
rss_fetcher = RSSFeedFetcher(RSS_FEED_URL)

db_temporal = {}

def get_lne_rss_eventos() -> List[Dict[str, Union[str, datetime]]]: #para probar, hay que hacer un flow para que esto llegue a bbdd
    events = rss_fetcher.get_events()
    return events