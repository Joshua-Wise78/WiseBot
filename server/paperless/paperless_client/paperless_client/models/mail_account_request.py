from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..models.account_type_enum import AccountTypeEnum
from ..models.imap_security_enum import ImapSecurityEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mail_account_request_set_permissions import MailAccountRequestSetPermissions


T = TypeVar("T", bound="MailAccountRequest")


@_attrs_define
class MailAccountRequest:
    """
    Attributes:
        name (str):
        imap_server (str):
        username (str):
        password (str):
        imap_port (int | None | Unset): This is usually 143 for unencrypted and STARTTLS connections, and 993 for SSL
            connections.
        imap_security (ImapSecurityEnum | Unset): * `1` - No encryption
            * `2` - Use SSL
            * `3` - Use STARTTLS
        character_set (str | Unset): The character set to use when communicating with the mail server, such as 'UTF-8'
            or 'US-ASCII'.
        is_token (bool | Unset):
        owner (int | None | Unset):
        set_permissions (MailAccountRequestSetPermissions | Unset):
        account_type (AccountTypeEnum | Unset): * `1` - IMAP
            * `2` - Gmail OAuth
            * `3` - Outlook OAuth
        expiration (datetime.datetime | None | Unset): The expiration date of the refresh token.
    """

    name: str
    imap_server: str
    username: str
    password: str
    imap_port: int | None | Unset = UNSET
    imap_security: ImapSecurityEnum | Unset = UNSET
    character_set: str | Unset = UNSET
    is_token: bool | Unset = UNSET
    owner: int | None | Unset = UNSET
    set_permissions: MailAccountRequestSetPermissions | Unset = UNSET
    account_type: AccountTypeEnum | Unset = UNSET
    expiration: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        imap_server = self.imap_server

        username = self.username

        password = self.password

        imap_port: int | None | Unset
        if isinstance(self.imap_port, Unset):
            imap_port = UNSET
        else:
            imap_port = self.imap_port

        imap_security: int | Unset = UNSET
        if not isinstance(self.imap_security, Unset):
            imap_security = self.imap_security.value

        character_set = self.character_set

        is_token = self.is_token

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        set_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_permissions, Unset):
            set_permissions = self.set_permissions.to_dict()

        account_type: int | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        expiration: None | str | Unset
        if isinstance(self.expiration, Unset):
            expiration = UNSET
        elif isinstance(self.expiration, datetime.datetime):
            expiration = self.expiration.isoformat()
        else:
            expiration = self.expiration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "imap_server": imap_server,
                "username": username,
                "password": password,
            }
        )
        if imap_port is not UNSET:
            field_dict["imap_port"] = imap_port
        if imap_security is not UNSET:
            field_dict["imap_security"] = imap_security
        if character_set is not UNSET:
            field_dict["character_set"] = character_set
        if is_token is not UNSET:
            field_dict["is_token"] = is_token
        if owner is not UNSET:
            field_dict["owner"] = owner
        if set_permissions is not UNSET:
            field_dict["set_permissions"] = set_permissions
        if account_type is not UNSET:
            field_dict["account_type"] = account_type
        if expiration is not UNSET:
            field_dict["expiration"] = expiration

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("imap_server", (None, str(self.imap_server).encode(), "text/plain")))

        files.append(("username", (None, str(self.username).encode(), "text/plain")))

        files.append(("password", (None, str(self.password).encode(), "text/plain")))

        if not isinstance(self.imap_port, Unset):
            if isinstance(self.imap_port, int):
                files.append(("imap_port", (None, str(self.imap_port).encode(), "text/plain")))
            else:
                files.append(("imap_port", (None, str(self.imap_port).encode(), "text/plain")))

        if not isinstance(self.imap_security, Unset):
            files.append(("imap_security", (None, str(self.imap_security.value).encode(), "text/plain")))

        if not isinstance(self.character_set, Unset):
            files.append(("character_set", (None, str(self.character_set).encode(), "text/plain")))

        if not isinstance(self.is_token, Unset):
            files.append(("is_token", (None, str(self.is_token).encode(), "text/plain")))

        if not isinstance(self.owner, Unset):
            if isinstance(self.owner, int):
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))
            else:
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))

        if not isinstance(self.set_permissions, Unset):
            files.append(
                ("set_permissions", (None, json.dumps(self.set_permissions.to_dict()).encode(), "application/json"))
            )

        if not isinstance(self.account_type, Unset):
            files.append(("account_type", (None, str(self.account_type.value).encode(), "text/plain")))

        if not isinstance(self.expiration, Unset):
            if isinstance(self.expiration, datetime.datetime):
                files.append(("expiration", (None, self.expiration.isoformat().encode(), "text/plain")))
            else:
                files.append(("expiration", (None, str(self.expiration).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mail_account_request_set_permissions import MailAccountRequestSetPermissions

        d = dict(src_dict)
        name = d.pop("name")

        imap_server = d.pop("imap_server")

        username = d.pop("username")

        password = d.pop("password")

        def _parse_imap_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        imap_port = _parse_imap_port(d.pop("imap_port", UNSET))

        _imap_security = d.pop("imap_security", UNSET)
        imap_security: ImapSecurityEnum | Unset
        if isinstance(_imap_security, Unset):
            imap_security = UNSET
        else:
            imap_security = ImapSecurityEnum(_imap_security)

        character_set = d.pop("character_set", UNSET)

        is_token = d.pop("is_token", UNSET)

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        _set_permissions = d.pop("set_permissions", UNSET)
        set_permissions: MailAccountRequestSetPermissions | Unset
        if isinstance(_set_permissions, Unset):
            set_permissions = UNSET
        else:
            set_permissions = MailAccountRequestSetPermissions.from_dict(_set_permissions)

        _account_type = d.pop("account_type", UNSET)
        account_type: AccountTypeEnum | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AccountTypeEnum(_account_type)

        def _parse_expiration(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_type_0 = isoparse(data)

                return expiration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiration = _parse_expiration(d.pop("expiration", UNSET))

        mail_account_request = cls(
            name=name,
            imap_server=imap_server,
            username=username,
            password=password,
            imap_port=imap_port,
            imap_security=imap_security,
            character_set=character_set,
            is_token=is_token,
            owner=owner,
            set_permissions=set_permissions,
            account_type=account_type,
            expiration=expiration,
        )

        mail_account_request.additional_properties = d
        return mail_account_request

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
