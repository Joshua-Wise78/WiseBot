from enum import Enum


class OperationEnum(str, Enum):
    DELETE = "delete"
    SET_PERMISSIONS = "set_permissions"

    def __str__(self) -> str:
        return str(self.value)
