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
    from ..models.patched_document_type_request_set_permissions import PatchedDocumentTypeRequestSetPermissions


T = TypeVar("T", bound="PatchedDocumentTypeRequest")


@_attrs_define
class PatchedDocumentTypeRequest:
    """
    Attributes:
        name (str | Unset):
        match (str | Unset):
        matching_algorithm (MatchingAlgorithm | Unset): * `0` - None
            * `1` - Any word
            * `2` - All words
            * `3` - Exact match
            * `4` - Regular expression
            * `5` - Fuzzy word
            * `6` - Automatic
        is_insensitive (bool | Unset):
        owner (int | None | Unset):
        set_permissions (PatchedDocumentTypeRequestSetPermissions | Unset):
    """

    name: str | Unset = UNSET
    match: str | Unset = UNSET
    matching_algorithm: MatchingAlgorithm | Unset = UNSET
    is_insensitive: bool | Unset = UNSET
    owner: int | None | Unset = UNSET
    set_permissions: PatchedDocumentTypeRequestSetPermissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        match = self.match

        matching_algorithm: int | Unset = UNSET
        if not isinstance(self.matching_algorithm, Unset):
            matching_algorithm = self.matching_algorithm.value

        is_insensitive = self.is_insensitive

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        set_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_permissions, Unset):
            set_permissions = self.set_permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if match is not UNSET:
            field_dict["match"] = match
        if matching_algorithm is not UNSET:
            field_dict["matching_algorithm"] = matching_algorithm
        if is_insensitive is not UNSET:
            field_dict["is_insensitive"] = is_insensitive
        if owner is not UNSET:
            field_dict["owner"] = owner
        if set_permissions is not UNSET:
            field_dict["set_permissions"] = set_permissions

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.match, Unset):
            files.append(("match", (None, str(self.match).encode(), "text/plain")))

        if not isinstance(self.matching_algorithm, Unset):
            files.append(("matching_algorithm", (None, str(self.matching_algorithm.value).encode(), "text/plain")))

        if not isinstance(self.is_insensitive, Unset):
            files.append(("is_insensitive", (None, str(self.is_insensitive).encode(), "text/plain")))

        if not isinstance(self.owner, Unset):
            if isinstance(self.owner, int):
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))
            else:
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))

        if not isinstance(self.set_permissions, Unset):
            files.append(
                ("set_permissions", (None, json.dumps(self.set_permissions.to_dict()).encode(), "application/json"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_document_type_request_set_permissions import PatchedDocumentTypeRequestSetPermissions

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        match = d.pop("match", UNSET)

        _matching_algorithm = d.pop("matching_algorithm", UNSET)
        matching_algorithm: MatchingAlgorithm | Unset
        if isinstance(_matching_algorithm, Unset):
            matching_algorithm = UNSET
        else:
            matching_algorithm = MatchingAlgorithm(_matching_algorithm)

        is_insensitive = d.pop("is_insensitive", UNSET)

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        _set_permissions = d.pop("set_permissions", UNSET)
        set_permissions: PatchedDocumentTypeRequestSetPermissions | Unset
        if isinstance(_set_permissions, Unset):
            set_permissions = UNSET
        else:
            set_permissions = PatchedDocumentTypeRequestSetPermissions.from_dict(_set_permissions)

        patched_document_type_request = cls(
            name=name,
            match=match,
            matching_algorithm=matching_algorithm,
            is_insensitive=is_insensitive,
            owner=owner,
            set_permissions=set_permissions,
        )

        patched_document_type_request.additional_properties = d
        return patched_document_type_request

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
