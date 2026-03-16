from enum import Enum


class MethodEnum(str, Enum):
    ADD_TAG = "add_tag"
    DELETE = "delete"
    DELETE_PAGES = "delete_pages"
    EDIT_PDF = "edit_pdf"
    MERGE = "merge"
    MODIFY_CUSTOM_FIELDS = "modify_custom_fields"
    MODIFY_TAGS = "modify_tags"
    REMOVE_TAG = "remove_tag"
    REPROCESS = "reprocess"
    ROTATE = "rotate"
    SET_CORRESPONDENT = "set_correspondent"
    SET_DOCUMENT_TYPE = "set_document_type"
    SET_PERMISSIONS = "set_permissions"
    SET_STORAGE_PATH = "set_storage_path"
    SPLIT = "split"

    def __str__(self) -> str:
        return str(self.value)
