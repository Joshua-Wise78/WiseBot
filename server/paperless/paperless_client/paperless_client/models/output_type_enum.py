from enum import Enum


class OutputTypeEnum(str, Enum):
    PDF = "pdf"
    PDFA = "pdfa"
    PDFA_1 = "pdfa-1"
    PDFA_2 = "pdfa-2"
    PDFA_3 = "pdfa-3"

    def __str__(self) -> str:
        return str(self.value)
