from enum import Enum


class TasksViewTypeEnum(str, Enum):
    AUTO_TASK = "auto_task"
    MANUAL_TASK = "manual_task"
    SCHEDULED_TASK = "scheduled_task"

    def __str__(self) -> str:
        return str(self.value)
