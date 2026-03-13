from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_instance_request import CustomFieldInstanceRequest
    from ..models.document_request_set_permissions import DocumentRequestSetPermissions


T = TypeVar("T", bound="DocumentRequest")


@_attrs_define
class DocumentRequest:
    """Adds update nested feature

    Attributes:
        correspondent (int | None):
        document_type (int | None):
        storage_path (int | None):
        tags (list[int]):
        title (str | Unset):
        content (str | Unset): The raw, text-only data of the document. This field is primarily used for searching.
        created (datetime.date | Unset):
        created_date (datetime.date | Unset):
        deleted_at (datetime.datetime | None | Unset):
        archive_serial_number (int | None | Unset): The position of this document in your physical document archive.
        owner (int | None | Unset):
        set_permissions (DocumentRequestSetPermissions | Unset):
        custom_fields (list[CustomFieldInstanceRequest] | Unset):
        remove_inbox_tags (bool | None | Unset):  Default: False.
    """

    correspondent: int | None
    document_type: int | None
    storage_path: int | None
    tags: list[int]
    title: str | Unset = UNSET
    content: str | Unset = UNSET
    created: datetime.date | Unset = UNSET
    created_date: datetime.date | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    archive_serial_number: int | None | Unset = UNSET
    owner: int | None | Unset = UNSET
    set_permissions: DocumentRequestSetPermissions | Unset = UNSET
    custom_fields: list[CustomFieldInstanceRequest] | Unset = UNSET
    remove_inbox_tags: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        correspondent: int | None
        correspondent = self.correspondent

        document_type: int | None
        document_type = self.document_type

        storage_path: int | None
        storage_path = self.storage_path

        tags = self.tags

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

        set_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_permissions, Unset):
            set_permissions = self.set_permissions.to_dict()

        custom_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        remove_inbox_tags: bool | None | Unset
        if isinstance(self.remove_inbox_tags, Unset):
            remove_inbox_tags = UNSET
        else:
            remove_inbox_tags = self.remove_inbox_tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "correspondent": correspondent,
                "document_type": document_type,
                "storage_path": storage_path,
                "tags": tags,
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
        if set_permissions is not UNSET:
            field_dict["set_permissions"] = set_permissions
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if remove_inbox_tags is not UNSET:
            field_dict["remove_inbox_tags"] = remove_inbox_tags

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if isinstance(self.correspondent, int):
            files.append(("correspondent", (None, str(self.correspondent).encode(), "text/plain")))
        else:
            files.append(("correspondent", (None, str(self.correspondent).encode(), "text/plain")))

        if isinstance(self.document_type, int):
            files.append(("document_type", (None, str(self.document_type).encode(), "text/plain")))
        else:
            files.append(("document_type", (None, str(self.document_type).encode(), "text/plain")))

        if isinstance(self.storage_path, int):
            files.append(("storage_path", (None, str(self.storage_path).encode(), "text/plain")))
        else:
            files.append(("storage_path", (None, str(self.storage_path).encode(), "text/plain")))

        for tags_item_element in self.tags:
            files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.content, Unset):
            files.append(("content", (None, str(self.content).encode(), "text/plain")))

        if not isinstance(self.created, Unset):
            files.append(("created", (None, self.created.isoformat().encode(), "text/plain")))

        if not isinstance(self.created_date, Unset):
            files.append(("created_date", (None, self.created_date.isoformat().encode(), "text/plain")))

        if not isinstance(self.deleted_at, Unset):
            if isinstance(self.deleted_at, datetime.datetime):
                files.append(("deleted_at", (None, self.deleted_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("deleted_at", (None, str(self.deleted_at).encode(), "text/plain")))

        if not isinstance(self.archive_serial_number, Unset):
            if isinstance(self.archive_serial_number, int):
                files.append(("archive_serial_number", (None, str(self.archive_serial_number).encode(), "text/plain")))
            else:
                files.append(("archive_serial_number", (None, str(self.archive_serial_number).encode(), "text/plain")))

        if not isinstance(self.owner, Unset):
            if isinstance(self.owner, int):
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))
            else:
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))

        if not isinstance(self.set_permissions, Unset):
            files.append(
                ("set_permissions", (None, json.dumps(self.set_permissions.to_dict()).encode(), "application/json"))
            )

        if not isinstance(self.custom_fields, Unset):
            for custom_fields_item_element in self.custom_fields:
                files.append(
                    (
                        "custom_fields",
                        (None, json.dumps(custom_fields_item_element.to_dict()).encode(), "application/json"),
                    )
                )

        if not isinstance(self.remove_inbox_tags, Unset):
            if isinstance(self.remove_inbox_tags, bool):
                files.append(("remove_inbox_tags", (None, str(self.remove_inbox_tags).encode(), "text/plain")))
            else:
                files.append(("remove_inbox_tags", (None, str(self.remove_inbox_tags).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_instance_request import CustomFieldInstanceRequest
        from ..models.document_request_set_permissions import DocumentRequestSetPermissions

        d = dict(src_dict)

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

        _set_permissions = d.pop("set_permissions", UNSET)
        set_permissions: DocumentRequestSetPermissions | Unset
        if isinstance(_set_permissions, Unset):
            set_permissions = UNSET
        else:
            set_permissions = DocumentRequestSetPermissions.from_dict(_set_permissions)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: list[CustomFieldInstanceRequest] | Unset = UNSET
        if _custom_fields is not UNSET:
            custom_fields = []
            for custom_fields_item_data in _custom_fields:
                custom_fields_item = CustomFieldInstanceRequest.from_dict(custom_fields_item_data)

                custom_fields.append(custom_fields_item)

        def _parse_remove_inbox_tags(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        remove_inbox_tags = _parse_remove_inbox_tags(d.pop("remove_inbox_tags", UNSET))

        document_request = cls(
            correspondent=correspondent,
            document_type=document_type,
            storage_path=storage_path,
            tags=tags,
            title=title,
            content=content,
            created=created,
            created_date=created_date,
            deleted_at=deleted_at,
            archive_serial_number=archive_serial_number,
            owner=owner,
            set_permissions=set_permissions,
            custom_fields=custom_fields,
            remove_inbox_tags=remove_inbox_tags,
        )

        document_request.additional_properties = d
        return document_request

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
