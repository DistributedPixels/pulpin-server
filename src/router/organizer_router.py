from typing import List

from fastapi import APIRouter, HTTPException

from src.controller.organizer_controller import OrganizerController
from src.model.organizer import Organizer, OrganizerCreate, OrganizerUpdate

router = APIRouter(prefix="/organizers", tags=["Organizers"])
controller = OrganizerController()


@router.post("/", response_model=Organizer)
def add_organizer(organizer: OrganizerCreate):
    try:
        return controller.add_organizer(organizer)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[Organizer])
def get_organizers():
    try:
        return controller.get_organizers()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{organizer_id}", response_model=Organizer)
def update_organizer(organizer_id: int, organizer: OrganizerUpdate):
    try:
        return controller.edit_organizer(organizer_id, organizer)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{organizer_id}", response_model=Organizer)
def delete_organizer(organizer_id: int):
    try:
        return controller.delete_organizer(organizer_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
