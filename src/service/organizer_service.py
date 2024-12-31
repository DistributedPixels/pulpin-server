from typing import List

from src.db.organizer_repository import OrganizerRepository
from src.model.organizer import Organizer, OrganizerCreate, OrganizerUpdate


class OrganizerService:
    def __init__(self):
        self.repository = OrganizerRepository()

    def add_organizer(self, organizer_data: OrganizerCreate) -> Organizer:
        return self.repository.add_organizer(organizer_data)

    def get_organizers(self) -> List[Organizer]:
        return self.repository.get_all_organizers()

    def edit_organizer(self, organizer_id: int, organizer_data: OrganizerUpdate) -> Organizer:
        return self.repository.edit_organizer(organizer_id, organizer_data)

    def delete_organizer(self, organizer_id: int) -> Organizer:
        return self.repository.delete_organizer(organizer_id)
