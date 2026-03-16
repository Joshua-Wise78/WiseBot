from __future__ import annotations

import datetime
from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PostDocumentRequest")


@_attrs_define
class PostDocumentRequest:
    """
    Attributes:
        document (File):
        created (datetime.datetime | None | Unset):
        title (str | Unset):
        correspondent (int | None | Unset):
        document_type (int | None | Unset):
        storage_path (int | None | Unset):
        tags (list[int] | Unset):
        archive_serial_number (int | Unset):
        custom_fields (Any | Unset):
        from_webui (bool | Unset):
    """

    document: File
    created: datetime.datetime | None | Unset = UNSET
    title: str | Unset = UNSET
    correspondent: int | None | Unset = UNSET
    document_type: int | None | Unset = UNSET
    storage_path: int | None | Unset = UNSET
    tags: list[int] | Unset = UNSET
    archive_serial_number: int | Unset = UNSET
    custom_fields: Any | Unset = UNSET
    from_webui: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document = self.document.to_tuple()

        created: None | str | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        title = self.title

        correspondent: int | None | Unset
        if isinstance(self.correspondent, Unset):
            correspondent = UNSET
        else:
            correspondent = self.correspondent

        document_type: int | None | Unset
        if isinstance(self.document_type, Unset):
            document_type = UNSET
        else:
            document_type = self.document_type

        storage_path: int | None | Unset
        if isinstance(self.storage_path, Unset):
            storage_path = UNSET
        else:
            storage_path = self.storage_path

        tags: list[int] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        archive_serial_number = self.archive_serial_number

        custom_fields = self.custom_fields

        from_webui = self.from_webui

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document": document,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if title is not UNSET:
            field_dict["title"] = title
        if correspondent is not UNSET:
            field_dict["correspondent"] = correspondent
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if storage_path is not UNSET:
            field_dict["storage_path"] = storage_path
        if tags is not UNSET:
            field_dict["tags"] = tags
        if archive_serial_number is not UNSET:
            field_dict["archive_serial_number"] = archive_serial_number
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if from_webui is not UNSET:
            field_dict["from_webui"] = from_webui

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("document", self.document.to_tuple()))

        if not isinstance(self.created, Unset):
            if isinstance(self.created, datetime.datetime):
                files.append(("created", (None, self.created.isoformat().encode(), "text/plain")))
            else:
                files.append(("created", (None, str(self.created).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.correspondent, Unset):
            if isinstance(self.correspondent, int):
                files.append(("correspondent", (None, str(self.correspondent).encode(), "text/plain")))
            else:
                files.append(("correspondent", (None, str(self.correspondent).encode(), "text/plain")))

        if not isinstance(self.document_type, Unset):
            if isinstance(self.document_type, int):
                files.append(("document_type", (None, str(self.document_type).encode(), "text/plain")))
            else:
                files.append(("document_type", (None, str(self.document_type).encode(), "text/plain")))

        if not isinstance(self.storage_path, Unset):
            if isinstance(self.storage_path, int):
                files.append(("storage_path", (None, str(self.storage_path).encode(), "text/plain")))
            else:
                files.append(("storage_path", (None, str(self.storage_path).encode(), "text/plain")))

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(("tags", (None, str(tags_item_element).encode(), "text/plain")))

        if not isinstance(self.archive_serial_number, Unset):
            files.append(("archive_serial_number", (None, str(self.archive_serial_number).encode(), "text/plain")))

        if not isinstance(self.custom_fields, Unset):
            files.append(("custom_fields", (None, str(self.custom_fields).encode(), "text/plain")))

        if not isinstance(self.from_webui, Unset):
            files.append(("from_webui", (None, str(self.from_webui).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document = File(payload=BytesIO(d.pop("document")))

        def _parse_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        title = d.pop("title", UNSET)

        def _parse_correspondent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        correspondent = _parse_correspondent(d.pop("correspondent", UNSET))

        def _parse_document_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        document_type = _parse_document_type(d.pop("document_type", UNSET))

        def _parse_storage_path(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_path = _parse_storage_path(d.pop("storage_path", UNSET))

        tags = cast(list[int], d.pop("tags", UNSET))

        archive_serial_number = d.pop("archive_serial_number", UNSET)

        custom_fields = d.pop("custom_fields", UNSET)

        from_webui = d.pop("from_webui", UNSET)

        post_document_request = cls(
            document=document,
            created=created,
            title=title,
            correspondent=correspondent,
            document_type=document_type,
            storage_path=storage_path,
            tags=tags,
            archive_serial_number=archive_serial_number,
            custom_fields=custom_fields,
            from_webui=from_webui,
        )

        post_document_request.additional_properties = d
        return post_document_request

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
