from enum import Enum


class DataTypeEnum(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    DOCUMENTLINK = "documentlink"
    FLOAT = "float"
    INTEGER = "integer"
    LONGTEXT = "longtext"
    MONETARY = "monetary"
    SELECT = "select"
    STRING = "string"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
