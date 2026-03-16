from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowActionEmail")


@_attrs_define
class WorkflowActionEmail:
    """
    Attributes:
        subject (str): The subject of the email, can include some placeholders, see documentation.
        body (str): The body (message) of the email, can include some placeholders, see documentation.
        to (str): The destination email addresses, comma separated.
        id (int | None | Unset):
        include_document (bool | Unset):
    """

    subject: str
    body: str
    to: str
    id: int | None | Unset = UNSET
    include_document: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        body = self.body

        to = self.to

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        include_document = self.include_document

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "body": body,
                "to": to,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if include_document is not UNSET:
            field_dict["include_document"] = include_document

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject = d.pop("subject")

        body = d.pop("body")

        to = d.pop("to")

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        include_document = d.pop("include_document", UNSET)

        workflow_action_email = cls(
            subject=subject,
            body=body,
            to=to,
            id=id,
            include_document=include_document,
        )

        workflow_action_email.additional_properties = d
        return workflow_action_email

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
