from fastapi import FastAPI
from src.controller.event_controller import EventController
from src.model.event import Event
from typing import List

app = FastAPI()
favicon_path = 'favicon.ico'
controller = EventController()


@app.get("/")
def read_root():
    return {"Hola": "Pulpin 🐙"}


@app.get("/events", response_model=List[Event])
async def get_events():
    return await controller.get_events()
