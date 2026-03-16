from enum import Enum


class TaskNameEnum(str, Enum):
    CHECK_SANITY = "check_sanity"
    CONSUME_FILE = "consume_file"
    INDEX_OPTIMIZE = "index_optimize"
    TRAIN_CLASSIFIER = "train_classifier"

    def __str__(self) -> str:
        return str(self.value)
