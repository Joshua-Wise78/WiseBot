from enum import Enum


class SkipArchiveFileEnum(str, Enum):
    ALWAYS = "always"
    NEVER = "never"
    WITH_TEXT = "with_text"

    def __str__(self) -> str:
        return str(self.value)
