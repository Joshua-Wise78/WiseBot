from enum import Enum


class ModeEnum(str, Enum):
    FORCE = "force"
    REDO = "redo"
    SKIP = "skip"
    SKIP_NOARCHIVE = "skip_noarchive"

    def __str__(self) -> str:
        return str(self.value)
