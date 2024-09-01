from typing import Union

from fastapi import FastAPI

# URL del feed RSS de La Nueva España
from service.rss_feed_fetcher import RSSFeedFetcher

RSS_FEED_URL = "https://www.lne.es/rss/section/2014085"

app = FastAPI()

rss_fetcher = RSSFeedFetcher(RSS_FEED_URL)


@app.get("/")
def read_root():
    return {"Hola": "Pulpin 🐙"}

@app.get("/rss-events")
async def get_rss_events():
    events = await rss_fetcher.get_events()
    return {"events": events}