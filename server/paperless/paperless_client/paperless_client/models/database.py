from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.migration_status import MigrationStatus


T = TypeVar("T", bound="Database")


@_attrs_define
class Database:
    """
    Attributes:
        type_ (str):
        url (str):
        status (str):
        error (str):
        migration_status (MigrationStatus):
    """

    type_: str
    url: str
    status: str
    error: str
    migration_status: MigrationStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        status = self.status

        error = self.error

        migration_status = self.migration_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "url": url,
                "status": status,
                "error": error,
                "migration_status": migration_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_status import MigrationStatus

        d = dict(src_dict)
        type_ = d.pop("type")

        url = d.pop("url")

        status = d.pop("status")

        error = d.pop("error")

        migration_status = MigrationStatus.from_dict(d.pop("migration_status"))

        database = cls(
            type_=type_,
            url=url,
            status=status,
            error=error,
            migration_status=migration_status,
        )

        database.additional_properties = d
        return database

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
