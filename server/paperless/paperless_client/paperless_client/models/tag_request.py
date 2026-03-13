from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.matching_algorithm import MatchingAlgorithm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_request_set_permissions import TagRequestSetPermissions


T = TypeVar("T", bound="TagRequest")


@_attrs_define
class TagRequest:
    """
    Attributes:
        name (str):
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
        set_permissions (TagRequestSetPermissions | Unset):
        parent (int | None | Unset):
    """

    name: str
    color: str | Unset = UNSET
    match: str | Unset = UNSET
    matching_algorithm: MatchingAlgorithm | Unset = UNSET
    is_insensitive: bool | Unset = UNSET
    is_inbox_tag: bool | Unset = UNSET
    owner: int | None | Unset = UNSET
    set_permissions: TagRequestSetPermissions | Unset = UNSET
    parent: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        set_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_permissions, Unset):
            set_permissions = self.set_permissions.to_dict()

        parent: int | None | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
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
        if set_permissions is not UNSET:
            field_dict["set_permissions"] = set_permissions
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.color, Unset):
            files.append(("color", (None, str(self.color).encode(), "text/plain")))

        if not isinstance(self.match, Unset):
            files.append(("match", (None, str(self.match).encode(), "text/plain")))

        if not isinstance(self.matching_algorithm, Unset):
            files.append(("matching_algorithm", (None, str(self.matching_algorithm.value).encode(), "text/plain")))

        if not isinstance(self.is_insensitive, Unset):
            files.append(("is_insensitive", (None, str(self.is_insensitive).encode(), "text/plain")))

        if not isinstance(self.is_inbox_tag, Unset):
            files.append(("is_inbox_tag", (None, str(self.is_inbox_tag).encode(), "text/plain")))

        if not isinstance(self.owner, Unset):
            if isinstance(self.owner, int):
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))
            else:
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))

        if not isinstance(self.set_permissions, Unset):
            files.append(
                ("set_permissions", (None, json.dumps(self.set_permissions.to_dict()).encode(), "application/json"))
            )

        if not isinstance(self.parent, Unset):
            if isinstance(self.parent, int):
                files.append(("parent", (None, str(self.parent).encode(), "text/plain")))
            else:
                files.append(("parent", (None, str(self.parent).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag_request_set_permissions import TagRequestSetPermissions

        d = dict(src_dict)
        name = d.pop("name")

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

        _set_permissions = d.pop("set_permissions", UNSET)
        set_permissions: TagRequestSetPermissions | Unset
        if isinstance(_set_permissions, Unset):
            set_permissions = UNSET
        else:
            set_permissions = TagRequestSetPermissions.from_dict(_set_permissions)

        def _parse_parent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        tag_request = cls(
            name=name,
            color=color,
            match=match,
            matching_algorithm=matching_algorithm,
            is_insensitive=is_insensitive,
            is_inbox_tag=is_inbox_tag,
            owner=owner,
            set_permissions=set_permissions,
            parent=parent,
        )

        tag_request.additional_properties = d
        return tag_request

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
