from enum import Enum


class TrashActionEnum(str, Enum):
    EMPTY = "empty"
    RESTORE = "restore"

    def __str__(self) -> str:
        return str(self.value)
