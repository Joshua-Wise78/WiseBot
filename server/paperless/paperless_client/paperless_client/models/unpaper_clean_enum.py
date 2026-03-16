from enum import Enum


class UnpaperCleanEnum(str, Enum):
    CLEAN = "clean"
    CLEAN_FINAL = "clean-final"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
