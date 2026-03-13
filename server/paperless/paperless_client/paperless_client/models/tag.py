from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matching_algorithm import MatchingAlgorithm
from ..types import UNSET, Unset

T = TypeVar("T", bound="Tag")


@_attrs_define
class Tag:
    """
    Attributes:
        id (int):
        slug (str):
        name (str):
        text_color (str):
        document_count (int):
        user_can_change (bool):
        children (list[int]):
        color (str | Unset):
        match (str | Unset):
        matching_algorithm (MatchingAlgorithm | Unset): * `0` - None
            * `1` - Any word
            * `2` - All words
            * `3` - Exact match
            * `4` - Regular expression
            * `5` - Fuzzy word
            * `6` - Automatic
        is_insensitive (bool | Unset):
        is_inbox_tag (bool | Unset): Marks this tag as an inbox tag: All newly consumed documents will be tagged with
            inbox tags.
        owner (int | None | Unset):
        parent (int | None | Unset):
    """

    id: int
    slug: str
    name: str
    text_color: str
    document_count: int
    user_can_change: bool
    children: list[int]
    color: str | Unset = UNSET
    match: str | Unset = UNSET
    matching_algorithm: MatchingAlgorithm | Unset = UNSET
    is_insensitive: bool | Unset = UNSET
    is_inbox_tag: bool | Unset = UNSET
    owner: int | None | Unset = UNSET
    parent: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        name = self.name

        text_color = self.text_color

        document_count = self.document_count

        user_can_change = self.user_can_change

        children = self.children

        color = self.color

        match = self.match

        matching_algorithm: int | Unset = UNSET
        if not isinstance(self.matching_algorithm, Unset):
            matching_algorithm = self.matching_algorithm.value

        is_insensitive = self.is_insensitive

        is_inbox_tag = self.is_inbox_tag

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        parent: int | None | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
                "text_color": text_color,
                "document_count": document_count,
                "user_can_change": user_can_change,
                "children": children,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if match is not UNSET:
            field_dict["match"] = match
        if matching_algorithm is not UNSET:
            field_dict["matching_algorithm"] = matching_algorithm
        if is_insensitive is not UNSET:
            field_dict["is_insensitive"] = is_insensitive
        if is_inbox_tag is not UNSET:
            field_dict["is_inbox_tag"] = is_inbox_tag
        if owner is not UNSET:
            field_dict["owner"] = owner
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        slug = d.pop("slug")

        name = d.pop("name")

        text_color = d.pop("text_color")

        document_count = d.pop("document_count")

        user_can_change = d.pop("user_can_change")

        children = cast(list[int], d.pop("children"))

        color = d.pop("color", UNSET)

        match = d.pop("match", UNSET)

        _matching_algorithm = d.pop("matching_algorithm", UNSET)
        matching_algorithm: MatchingAlgorithm | Unset
        if isinstance(_matching_algorithm, Unset):
            matching_algorithm = UNSET
        else:
            matching_algorithm = MatchingAlgorithm(_matching_algorithm)

        is_insensitive = d.pop("is_insensitive", UNSET)

        is_inbox_tag = d.pop("is_inbox_tag", UNSET)

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_parent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        tag = cls(
            id=id,
            slug=slug,
            name=name,
            text_color=text_color,
            document_count=document_count,
            user_can_change=user_can_change,
            children=children,
            color=color,
            match=match,
            matching_algorithm=matching_algorithm,
            is_insensitive=is_insensitive,
            is_inbox_tag=is_inbox_tag,
            owner=owner,
            parent=parent,
        )

        tag.additional_properties = d
        return tag

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
