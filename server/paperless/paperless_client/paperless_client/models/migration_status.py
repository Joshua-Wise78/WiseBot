from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MigrationStatus")


@_attrs_define
class MigrationStatus:
    """
    Attributes:
        latest_migration (str):
        unapplied_migrations (list[str]):
    """

    latest_migration: str
    unapplied_migrations: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_migration = self.latest_migration

        unapplied_migrations = self.unapplied_migrations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latest_migration": latest_migration,
                "unapplied_migrations": unapplied_migrations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latest_migration = d.pop("latest_migration")

        unapplied_migrations = cast(list[str], d.pop("unapplied_migrations"))

        migration_status = cls(
            latest_migration=latest_migration,
            unapplied_migrations=unapplied_migrations,
        )

        migration_status.additional_properties = d
        return migration_status

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
