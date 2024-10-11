from fastapi import FastAPI, HTTPException
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
def get_events():
    try:
        return controller.get_events()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/events", response_model=Event)
def add_event(event: Event):
    try:
        return controller.add_event(event)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
