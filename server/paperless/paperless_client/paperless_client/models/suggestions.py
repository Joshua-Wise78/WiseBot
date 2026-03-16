from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Suggestions")


@_attrs_define
class Suggestions:
    """
    Attributes:
        correspondents (list[int]):
        tags (list[int]):
        document_types (list[int]):
        storage_paths (list[int]):
        dates (list[str]):
    """

    correspondents: list[int]
    tags: list[int]
    document_types: list[int]
    storage_paths: list[int]
    dates: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        correspondents = self.correspondents

        tags = self.tags

        document_types = self.document_types

        storage_paths = self.storage_paths

        dates = self.dates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "correspondents": correspondents,
                "tags": tags,
                "document_types": document_types,
                "storage_paths": storage_paths,
                "dates": dates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        correspondents = cast(list[int], d.pop("correspondents"))

        tags = cast(list[int], d.pop("tags"))

        document_types = cast(list[int], d.pop("document_types"))

        storage_paths = cast(list[int], d.pop("storage_paths"))

        dates = cast(list[str], d.pop("dates"))

        suggestions = cls(
            correspondents=correspondents,
            tags=tags,
            document_types=document_types,
            storage_paths=storage_paths,
            dates=dates,
        )

        suggestions.additional_properties = d
        return suggestions

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
