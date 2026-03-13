from enum import Enum


class FileVersionEnum(str, Enum):
    ARCHIVE = "archive"
    ORIGINAL = "original"

    def __str__(self) -> str:
        return str(self.value)
