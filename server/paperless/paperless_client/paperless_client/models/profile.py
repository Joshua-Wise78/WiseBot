from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_account import SocialAccount


T = TypeVar("T", bound="Profile")


@_attrs_define
class Profile:
    """
    Attributes:
        auth_token (str):
        social_accounts (list[SocialAccount]):
        has_usable_password (bool):
        is_mfa_enabled (bool):
        email (str | Unset):
        password (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
    """

    auth_token: str
    social_accounts: list[SocialAccount]
    has_usable_password: bool
    is_mfa_enabled: bool
    email: str | Unset = UNSET
    password: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_token = self.auth_token

        social_accounts = []
        for social_accounts_item_data in self.social_accounts:
            social_accounts_item = social_accounts_item_data.to_dict()
            social_accounts.append(social_accounts_item)

        has_usable_password = self.has_usable_password

        is_mfa_enabled = self.is_mfa_enabled

        email = self.email

        password = self.password

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_token": auth_token,
                "social_accounts": social_accounts,
                "has_usable_password": has_usable_password,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_account import SocialAccount

        d = dict(src_dict)
        auth_token = d.pop("auth_token")

        social_accounts = []
        _social_accounts = d.pop("social_accounts")
        for social_accounts_item_data in _social_accounts:
            social_accounts_item = SocialAccount.from_dict(social_accounts_item_data)

            social_accounts.append(social_accounts_item)

        has_usable_password = d.pop("has_usable_password")

        is_mfa_enabled = d.pop("is_mfa_enabled")

        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        profile = cls(
            auth_token=auth_token,
            social_accounts=social_accounts,
            has_usable_password=has_usable_password,
            is_mfa_enabled=is_mfa_enabled,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        profile.additional_properties = d
        return profile

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
