from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessedMail")


@_attrs_define
class ProcessedMail:
    """
    Attributes:
        id (int):
        rule (int):
        folder (str):
        uid (str):
        subject (str):
        received (datetime.datetime):
        processed (datetime.datetime):
        status (str):
        error (None | str):
        owner (int | None | Unset):
    """

    id: int
    rule: int
    folder: str
    uid: str
    subject: str
    received: datetime.datetime
    processed: datetime.datetime
    status: str
    error: None | str
    owner: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rule = self.rule

        folder = self.folder

        uid = self.uid

        subject = self.subject

        received = self.received.isoformat()

        processed = self.processed.isoformat()

        status = self.status

        error: None | str
        error = self.error

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rule": rule,
                "folder": folder,
                "uid": uid,
                "subject": subject,
                "received": received,
                "processed": processed,
                "status": status,
                "error": error,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        rule = d.pop("rule")

        folder = d.pop("folder")

        uid = d.pop("uid")

        subject = d.pop("subject")

        received = isoparse(d.pop("received"))

        processed = isoparse(d.pop("processed"))

        status = d.pop("status")

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        processed_mail = cls(
            id=id,
            rule=rule,
            folder=folder,
            uid=uid,
            subject=subject,
            received=received,
            processed=processed,
            status=status,
            error=error,
            owner=owner,
        )

        processed_mail.additional_properties = d
        return processed_mail

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
