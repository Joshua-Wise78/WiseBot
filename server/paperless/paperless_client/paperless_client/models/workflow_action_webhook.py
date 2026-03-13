from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowActionWebhook")


@_attrs_define
class WorkflowActionWebhook:
    """
    Attributes:
        url (str): The destination URL for the notification.
        id (int | None | Unset):
        use_params (bool | Unset):
        as_json (bool | Unset):
        params (Any | Unset): The parameters to send with the webhook URL if body not used.
        body (None | str | Unset): The body to send with the webhook URL if parameters not used.
        headers (Any | Unset): The headers to send with the webhook URL.
        include_document (bool | Unset):
    """

    url: str
    id: int | None | Unset = UNSET
    use_params: bool | Unset = UNSET
    as_json: bool | Unset = UNSET
    params: Any | Unset = UNSET
    body: None | str | Unset = UNSET
    headers: Any | Unset = UNSET
    include_document: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        use_params = self.use_params

        as_json = self.as_json

        params = self.params

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        headers = self.headers

        include_document = self.include_document

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if use_params is not UNSET:
            field_dict["use_params"] = use_params
        if as_json is not UNSET:
            field_dict["as_json"] = as_json
        if params is not UNSET:
            field_dict["params"] = params
        if body is not UNSET:
            field_dict["body"] = body
        if headers is not UNSET:
            field_dict["headers"] = headers
        if include_document is not UNSET:
            field_dict["include_document"] = include_document

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        use_params = d.pop("use_params", UNSET)

        as_json = d.pop("as_json", UNSET)

        params = d.pop("params", UNSET)

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        headers = d.pop("headers", UNSET)

        include_document = d.pop("include_document", UNSET)

        workflow_action_webhook = cls(
            url=url,
            id=id,
            use_params=use_params,
            as_json=as_json,
            params=params,
            body=body,
            headers=headers,
            include_document=include_document,
        )

        workflow_action_webhook.additional_properties = d
        return workflow_action_webhook

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
