from enum import Enum


class ContentEnum(str, Enum):
    ARCHIVE = "archive"
    BOTH = "both"
    ORIGINALS = "originals"

    def __str__(self) -> str:
        return str(self.value)
