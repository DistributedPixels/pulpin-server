from typing import List

from src.model.organizer import Organizer, OrganizerCreate, OrganizerUpdate
from src.service.organizer_service import OrganizerService


class OrganizerController:

    def __init__(self):
        self.service = OrganizerService()

    def get_organizers(self) -> List[Organizer]:
        return self.service.get_organizers()

    def add_organizer(self, organizer_data: OrganizerCreate) -> Organizer:
        return self.service.add_organizer(organizer_data)

    def edit_organizer(self, organizer_id: int, organizer_data: OrganizerUpdate) -> Organizer:
        return self.service.edit_organizer(organizer_id, organizer_data)

    def delete_organizer(self, organizer_id: int) -> Organizer:
        return self.service.delete_organizer(organizer_id)
