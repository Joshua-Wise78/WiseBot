from enum import Enum


class ScheduleDateFieldEnum(str, Enum):
    ADDED = "added"
    CREATED = "created"
    CUSTOM_FIELD = "custom_field"
    MODIFIED = "modified"

    def __str__(self) -> str:
        return str(self.value)
