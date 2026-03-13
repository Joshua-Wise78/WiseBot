from enum import Enum


class CompressionEnum(str, Enum):
    BZIP2 = "bzip2"
    DEFLATED = "deflated"
    LZMA = "lzma"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
