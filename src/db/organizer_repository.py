from typing import List

from src.model.organizer import Organizer, OrganizerCreate, OrganizerUpdate
from .connection import Connection


class OrganizerRepository:
    ORGANIZERS_TABLE = "organizers"

    def __init__(self):
        self.connection = Connection()

    def add_organizer(self, organizer: OrganizerCreate) -> Organizer:
        try:
            organizer_data = self.connection.table(self.ORGANIZERS_TABLE) \
                .insert(organizer.model_dump(exclude_none=True)) \
                .execute()
            return Organizer(**organizer_data.data[0])
        except Exception as e:
            raise e

    def get_all_organizers(self) -> List[Organizer]:
        try:
            organizer_data = self.connection.table(self.ORGANIZERS_TABLE) \
                .select("*") \
                .execute()
            return [Organizer(**organizer) for organizer in organizer_data.data]

        except Exception as e:
            raise e

    def edit_organizer(self, organizer_id: int, organizer: OrganizerUpdate) -> Organizer:
        try:
            organizer_data = self.connection.table(self.ORGANIZERS_TABLE) \
                .update(organizer.model_dump(exclude_none=True)) \
                .eq("id", organizer_id) \
                .execute()
            return Organizer(**organizer_data.data[0])
        except Exception as e:
            raise e

    def delete_organizer(self, organizer_id: int) -> Organizer:
        try:
            organizer_data = self.connection.table(self.ORGANIZERS_TABLE) \
                .delete() \
                .eq("id", organizer_id) \
                .execute()
            return Organizer(**organizer_data.data[0])
        except Exception as e:
            raise e
