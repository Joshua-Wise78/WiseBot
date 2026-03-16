from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_action_request import WorkflowActionRequest
    from ..models.workflow_trigger_request import WorkflowTriggerRequest


T = TypeVar("T", bound="WorkflowRequest")


@_attrs_define
class WorkflowRequest:
    """
    Attributes:
        name (str):
        triggers (list[WorkflowTriggerRequest]):
        actions (list[WorkflowActionRequest]):
        order (int | Unset):
        enabled (bool | Unset):
    """

    name: str
    triggers: list[WorkflowTriggerRequest]
    actions: list[WorkflowActionRequest]
    order: int | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        triggers = []
        for triggers_item_data in self.triggers:
            triggers_item = triggers_item_data.to_dict()
            triggers.append(triggers_item)

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        order = self.order

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "triggers": triggers,
                "actions": actions,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        for triggers_item_element in self.triggers:
            files.append(("triggers", (None, json.dumps(triggers_item_element.to_dict()).encode(), "application/json")))

        for actions_item_element in self.actions:
            files.append(("actions", (None, json.dumps(actions_item_element.to_dict()).encode(), "application/json")))

        if not isinstance(self.order, Unset):
            files.append(("order", (None, str(self.order).encode(), "text/plain")))

        if not isinstance(self.enabled, Unset):
            files.append(("enabled", (None, str(self.enabled).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_action_request import WorkflowActionRequest
        from ..models.workflow_trigger_request import WorkflowTriggerRequest

        d = dict(src_dict)
        name = d.pop("name")

        triggers = []
        _triggers = d.pop("triggers")
        for triggers_item_data in _triggers:
            triggers_item = WorkflowTriggerRequest.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = WorkflowActionRequest.from_dict(actions_item_data)

            actions.append(actions_item)

        order = d.pop("order", UNSET)

        enabled = d.pop("enabled", UNSET)

        workflow_request = cls(
            name=name,
            triggers=triggers,
            actions=actions,
            order=order,
            enabled=enabled,
        )

        workflow_request.additional_properties = d
        return workflow_request

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
