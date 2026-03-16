from enum import Enum


class ObjectTypeEnum(str, Enum):
    CORRESPONDENTS = "correspondents"
    DOCUMENT_TYPES = "document_types"
    STORAGE_PATHS = "storage_paths"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
