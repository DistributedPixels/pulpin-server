from fastapi import FastAPI, HTTPException
from src.controller.event_controller import EventController
from src.model.event import Event
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola": "Pulpin 🐙"}

@app.get("/events", response_model=List[Event])
async def get_events():
    return await EventController.get_events()

@app.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int):
    event = EventController.get_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    return event

@app.post("/events", response_model=Event, status_code=201)
def create_event(event: Event):
    return EventController.create_event(event)

@app.put("/events/{event_id}", response_model=Event)
def update_event(event_id: int, event: Event):
    updated_event = EventController.update_event(event_id, event)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    return updated_event

@app.delete("/events/{event_id}", status_code=204)
def delete_event(event_id: int):
    success = EventController.delete_event(event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found.")