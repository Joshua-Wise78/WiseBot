from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (int):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        inherited_permissions (list[str]):
        is_mfa_enabled (bool):
        email (str | Unset):
        password (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        date_joined (datetime.datetime | Unset):
        is_staff (bool | Unset): Designates whether the user can log into this admin site.
        is_active (bool | Unset): Designates whether this user should be treated as active. Unselect this instead of
            deleting accounts.
        is_superuser (bool | Unset): Designates that this user has all permissions without explicitly assigning them.
        groups (list[int] | Unset): The groups this user belongs to. A user will get all permissions granted to each of
            their groups.
        user_permissions (list[str] | Unset):
    """

    id: int
    username: str
    inherited_permissions: list[str]
    is_mfa_enabled: bool
    email: str | Unset = UNSET
    password: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    date_joined: datetime.datetime | Unset = UNSET
    is_staff: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_superuser: bool | Unset = UNSET
    groups: list[int] | Unset = UNSET
    user_permissions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        inherited_permissions = self.inherited_permissions

        is_mfa_enabled = self.is_mfa_enabled

        email = self.email

        password = self.password

        first_name = self.first_name

        last_name = self.last_name

        date_joined: str | Unset = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        is_staff = self.is_staff

        is_active = self.is_active

        is_superuser = self.is_superuser

        groups: list[int] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        user_permissions: list[str] | Unset = UNSET
        if not isinstance(self.user_permissions, Unset):
            user_permissions = self.user_permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "inherited_permissions": inherited_permissions,
                "is_mfa_enabled": is_mfa_enabled,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if groups is not UNSET:
            field_dict["groups"] = groups
        if user_permissions is not UNSET:
            field_dict["user_permissions"] = user_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        inherited_permissions = cast(list[str], d.pop("inherited_permissions"))

        is_mfa_enabled = d.pop("is_mfa_enabled")

        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: datetime.datetime | Unset
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        is_staff = d.pop("is_staff", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        groups = cast(list[int], d.pop("groups", UNSET))

        user_permissions = cast(list[str], d.pop("user_permissions", UNSET))

        user = cls(
            id=id,
            username=username,
            inherited_permissions=inherited_permissions,
            is_mfa_enabled=is_mfa_enabled,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_joined=date_joined,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            groups=groups,
            user_permissions=user_permissions,
        )

        user.additional_properties = d
        return user

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
