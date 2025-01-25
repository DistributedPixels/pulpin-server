from typing import List

from fastapi import APIRouter, HTTPException

from src.controller.event_controller import EventController
from src.model.event import Event

router = APIRouter(prefix="/events", tags=["Events"])
controller = EventController()


@router.get("/", response_model=List[Event])
def get_events():
    try:
        return controller.get_events()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/", response_model=Event)
def add_event(event: Event):
    try:
        return controller.add_event(event)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
