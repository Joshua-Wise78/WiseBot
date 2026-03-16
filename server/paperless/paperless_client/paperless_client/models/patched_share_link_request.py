from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..models.file_version_enum import FileVersionEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedShareLinkRequest")


@_attrs_define
class PatchedShareLinkRequest:
    """
    Attributes:
        expiration (datetime.datetime | None | Unset):
        document (int | Unset):
        file_version (FileVersionEnum | Unset): * `archive` - Archive
            * `original` - Original
    """

    expiration: datetime.datetime | None | Unset = UNSET
    document: int | Unset = UNSET
    file_version: FileVersionEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiration: None | str | Unset
        if isinstance(self.expiration, Unset):
            expiration = UNSET
        elif isinstance(self.expiration, datetime.datetime):
            expiration = self.expiration.isoformat()
        else:
            expiration = self.expiration

        document = self.document

        file_version: str | Unset = UNSET
        if not isinstance(self.file_version, Unset):
            file_version = self.file_version.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if document is not UNSET:
            field_dict["document"] = document
        if file_version is not UNSET:
            field_dict["file_version"] = file_version

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.expiration, Unset):
            if isinstance(self.expiration, datetime.datetime):
                files.append(("expiration", (None, self.expiration.isoformat().encode(), "text/plain")))
            else:
                files.append(("expiration", (None, str(self.expiration).encode(), "text/plain")))

        if not isinstance(self.document, Unset):
            files.append(("document", (None, str(self.document).encode(), "text/plain")))

        if not isinstance(self.file_version, Unset):
            files.append(("file_version", (None, str(self.file_version.value).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expiration(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_type_0 = isoparse(data)

                return expiration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration = _parse_expiration(d.pop("expiration", UNSET))

        document = d.pop("document", UNSET)

        _file_version = d.pop("file_version", UNSET)
        file_version: FileVersionEnum | Unset
        if isinstance(_file_version, Unset):
            file_version = UNSET
        else:
            file_version = FileVersionEnum(_file_version)

        patched_share_link_request = cls(
            expiration=expiration,
            document=document,
            file_version=file_version,
        )

        patched_share_link_request.additional_properties = d
        return patched_share_link_request

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
