from pydantic import BaseModel


class OrganizerCreate(BaseModel):
    name: str


class OrganizerUpdate(BaseModel):
    name: str


class Organizer(BaseModel):
    id: int
    name: str
