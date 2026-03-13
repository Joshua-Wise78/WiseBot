from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailRequest")


@_attrs_define
class EmailRequest:
    """
    Attributes:
        documents (list[int]):
        addresses (str): Comma-separated email addresses
        subject (str):
        message (str):
        use_archive_version (bool | Unset): Use archive version of documents if available Default: True.
    """

    documents: list[int]
    addresses: str
    subject: str
    message: str
    use_archive_version: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        documents = self.documents

        addresses = self.addresses

        subject = self.subject

        message = self.message

        use_archive_version = self.use_archive_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documents": documents,
                "addresses": addresses,
                "subject": subject,
                "message": message,
            }
        )
        if use_archive_version is not UNSET:
            field_dict["use_archive_version"] = use_archive_version

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        for documents_item_element in self.documents:
            files.append(("documents", (None, str(documents_item_element).encode(), "text/plain")))

        files.append(("addresses", (None, str(self.addresses).encode(), "text/plain")))

        files.append(("subject", (None, str(self.subject).encode(), "text/plain")))

        files.append(("message", (None, str(self.message).encode(), "text/plain")))

        if not isinstance(self.use_archive_version, Unset):
            files.append(("use_archive_version", (None, str(self.use_archive_version).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        documents = cast(list[int], d.pop("documents"))

        addresses = d.pop("addresses")

        subject = d.pop("subject")

        message = d.pop("message")

        use_archive_version = d.pop("use_archive_version", UNSET)

        email_request = cls(
            documents=documents,
            addresses=addresses,
            subject=subject,
            message=message,
            use_archive_version=use_archive_version,
        )

        email_request.additional_properties = d
        return email_request

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
