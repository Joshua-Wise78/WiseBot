from enum import Enum


class StatusEnum(str, Enum):
    FAILURE = "FAILURE"
    PENDING = "PENDING"
    RECEIVED = "RECEIVED"
    RETRY = "RETRY"
    REVOKED = "REVOKED"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
