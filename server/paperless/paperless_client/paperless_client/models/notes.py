from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.basic_user import BasicUser


T = TypeVar("T", bound="Notes")


@_attrs_define
class Notes:
    """
    Attributes:
        id (int):
        user (BasicUser):
        note (str | Unset): Note for the document
        created (datetime.datetime | Unset):
    """

    id: int
    user: BasicUser
    note: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user = self.user.to_dict()

        note = self.note

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_user import BasicUser

        d = dict(src_dict)
        id = d.pop("id")

        user = BasicUser.from_dict(d.pop("user"))

        note = d.pop("note", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        notes = cls(
            id=id,
            user=user,
            note=note,
            created=created,
        )

        notes.additional_properties = d
        return notes

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
