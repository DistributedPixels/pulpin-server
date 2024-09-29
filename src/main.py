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
