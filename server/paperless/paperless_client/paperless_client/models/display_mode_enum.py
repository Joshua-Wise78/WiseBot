from enum import Enum


class DisplayModeEnum(str, Enum):
    LARGECARDS = "largeCards"
    SMALLCARDS = "smallCards"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
