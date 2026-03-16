from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_instance import CustomFieldInstance
    from ..models.document_permissions import DocumentPermissions
    from ..models.notes import Notes


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """Adds update nested feature

    Attributes:
        id (int):
        correspondent (int | None):
        document_type (int | None):
        storage_path (int | None):
        tags (list[int]):
        modified (datetime.datetime):
        added (datetime.datetime):
        original_file_name (None | str):
        archived_file_name (None | str):
        permissions (DocumentPermissions):
        user_can_change (bool):
        is_shared_by_requester (bool):
        notes (list[Notes]):
        page_count (int | None):
        mime_type (str):
        title (str | Unset):
        content (str | Unset): The raw, text-only data of the document. This field is primarily used for searching.
        created (datetime.date | Unset):
        created_date (datetime.date | Unset):
        deleted_at (datetime.datetime | None | Unset):
        archive_serial_number (int | None | Unset): The position of this document in your physical document archive.
        owner (int | None | Unset):
        custom_fields (list[CustomFieldInstance] | Unset):
    """

    id: int
    correspondent: int | None
    document_type: int | None
    storage_path: int | None
    tags: list[int]
    modified: datetime.datetime
    added: datetime.datetime
    original_file_name: None | str
    archived_file_name: None | str
    permissions: DocumentPermissions
    user_can_change: bool
    is_shared_by_requester: bool
    notes: list[Notes]
    page_count: int | None
    mime_type: str
    title: str | Unset = UNSET
    content: str | Unset = UNSET
    created: datetime.date | Unset = UNSET
    created_date: datetime.date | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    archive_serial_number: int | None | Unset = UNSET
    owner: int | None | Unset = UNSET
    custom_fields: list[CustomFieldInstance] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        correspondent: int | None
        correspondent = self.correspondent

        document_type: int | None
        document_type = self.document_type

        storage_path: int | None
        storage_path = self.storage_path

        tags = self.tags

        modified = self.modified.isoformat()

        added = self.added.isoformat()

        original_file_name: None | str
        original_file_name = self.original_file_name

        archived_file_name: None | str
        archived_file_name = self.archived_file_name

        permissions = self.permissions.to_dict()

        user_can_change = self.user_can_change

        is_shared_by_requester = self.is_shared_by_requester

        notes = []
        for notes_item_data in self.notes:
            notes_item = notes_item_data.to_dict()
            notes.append(notes_item)

        page_count: int | None
        page_count = self.page_count

        mime_type = self.mime_type

        title = self.title

        content = self.content

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_date: str | Unset = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        archive_serial_number: int | None | Unset
        if isinstance(self.archive_serial_number, Unset):
            archive_serial_number = UNSET
        else:
            archive_serial_number = self.archive_serial_number

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        custom_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "correspondent": correspondent,
                "document_type": document_type,
                "storage_path": storage_path,
                "tags": tags,
                "modified": modified,
                "added": added,
                "original_file_name": original_file_name,
                "archived_file_name": archived_file_name,
                "permissions": permissions,
                "user_can_change": user_can_change,
                "is_shared_by_requester": is_shared_by_requester,
                "notes": notes,
                "page_count": page_count,
                "mime_type": mime_type,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if content is not UNSET:
            field_dict["content"] = content
        if created is not UNSET:
            field_dict["created"] = created
        if created_date is not UNSET:
            field_dict["created_date"] = created_date
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if archive_serial_number is not UNSET:
            field_dict["archive_serial_number"] = archive_serial_number
        if owner is not UNSET:
            field_dict["owner"] = owner
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_instance import CustomFieldInstance
        from ..models.document_permissions import DocumentPermissions
        from ..models.notes import Notes

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_correspondent(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        correspondent = _parse_correspondent(d.pop("correspondent"))

        def _parse_document_type(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        document_type = _parse_document_type(d.pop("document_type"))

        def _parse_storage_path(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        storage_path = _parse_storage_path(d.pop("storage_path"))

        tags = cast(list[int], d.pop("tags"))

        modified = isoparse(d.pop("modified"))

        added = isoparse(d.pop("added"))

        def _parse_original_file_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_file_name = _parse_original_file_name(d.pop("original_file_name"))

        def _parse_archived_file_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        archived_file_name = _parse_archived_file_name(d.pop("archived_file_name"))

        permissions = DocumentPermissions.from_dict(d.pop("permissions"))

        user_can_change = d.pop("user_can_change")

        is_shared_by_requester = d.pop("is_shared_by_requester")

        notes = []
        _notes = d.pop("notes")
        for notes_item_data in _notes:
            notes_item = Notes.from_dict(notes_item_data)

            notes.append(notes_item)

        def _parse_page_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        page_count = _parse_page_count(d.pop("page_count"))

        mime_type = d.pop("mime_type")

        title = d.pop("title", UNSET)

        content = d.pop("content", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.date | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created).date()

        _created_date = d.pop("created_date", UNSET)
        created_date: datetime.date | Unset
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date).date()

        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        def _parse_archive_serial_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_serial_number = _parse_archive_serial_number(d.pop("archive_serial_number", UNSET))

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: list[CustomFieldInstance] | Unset = UNSET
        if _custom_fields is not UNSET:
            custom_fields = []
            for custom_fields_item_data in _custom_fields:
                custom_fields_item = CustomFieldInstance.from_dict(custom_fields_item_data)

                custom_fields.append(custom_fields_item)

        document = cls(
            id=id,
            correspondent=correspondent,
            document_type=document_type,
            storage_path=storage_path,
            tags=tags,
            modified=modified,
            added=added,
            original_file_name=original_file_name,
            archived_file_name=archived_file_name,
            permissions=permissions,
            user_can_change=user_can_change,
            is_shared_by_requester=is_shared_by_requester,
            notes=notes,
            page_count=page_count,
            mime_type=mime_type,
            title=title,
            content=content,
            created=created,
            created_date=created_date,
            deleted_at=deleted_at,
            archive_serial_number=archive_serial_number,
            owner=owner,
            custom_fields=custom_fields,
        )

        document.additional_properties = d
        return document

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
