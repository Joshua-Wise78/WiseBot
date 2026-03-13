from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.matching_algorithm import MatchingAlgorithm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.correspondent_permissions import CorrespondentPermissions


T = TypeVar("T", bound="Correspondent")


@_attrs_define
class Correspondent:
    """
    Attributes:
        id (int):
        slug (str):
        name (str):
        document_count (int):
        last_correspondence (datetime.date):
        permissions (CorrespondentPermissions):
        user_can_change (bool):
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
    """

    id: int
    slug: str
    name: str
    document_count: int
    last_correspondence: datetime.date
    permissions: CorrespondentPermissions
    user_can_change: bool
    match: str | Unset = UNSET
    matching_algorithm: MatchingAlgorithm | Unset = UNSET
    is_insensitive: bool | Unset = UNSET
    owner: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        name = self.name

        document_count = self.document_count

        last_correspondence = self.last_correspondence.isoformat()

        permissions = self.permissions.to_dict()

        user_can_change = self.user_can_change

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
                "document_count": document_count,
                "last_correspondence": last_correspondence,
                "permissions": permissions,
                "user_can_change": user_can_change,
            }
        )
        if match is not UNSET:
            field_dict["match"] = match
        if matching_algorithm is not UNSET:
            field_dict["matching_algorithm"] = matching_algorithm
        if is_insensitive is not UNSET:
            field_dict["is_insensitive"] = is_insensitive
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.correspondent_permissions import CorrespondentPermissions

        d = dict(src_dict)
        id = d.pop("id")

        slug = d.pop("slug")

        name = d.pop("name")

        document_count = d.pop("document_count")

        last_correspondence = isoparse(d.pop("last_correspondence")).date()

        permissions = CorrespondentPermissions.from_dict(d.pop("permissions"))

        user_can_change = d.pop("user_can_change")

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

        correspondent = cls(
            id=id,
            slug=slug,
            name=name,
            document_count=document_count,
            last_correspondence=last_correspondence,
            permissions=permissions,
            user_can_change=user_can_change,
            match=match,
            matching_algorithm=matching_algorithm,
            is_insensitive=is_insensitive,
            owner=owner,
        )

        correspondent.additional_properties = d
        return correspondent

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
