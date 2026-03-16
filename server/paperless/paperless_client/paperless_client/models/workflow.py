from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_action import WorkflowAction
    from ..models.workflow_trigger import WorkflowTrigger


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """
    Attributes:
        id (int):
        name (str):
        triggers (list[WorkflowTrigger]):
        actions (list[WorkflowAction]):
        order (int | Unset):
        enabled (bool | Unset):
    """

    id: int
    name: str
    triggers: list[WorkflowTrigger]
    actions: list[WorkflowAction]
    order: int | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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
                "id": id,
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_action import WorkflowAction
        from ..models.workflow_trigger import WorkflowTrigger

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        triggers = []
        _triggers = d.pop("triggers")
        for triggers_item_data in _triggers:
            triggers_item = WorkflowTrigger.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = WorkflowAction.from_dict(actions_item_data)

            actions.append(actions_item)

        order = d.pop("order", UNSET)

        enabled = d.pop("enabled", UNSET)

        workflow = cls(
            id=id,
            name=name,
            triggers=triggers,
            actions=actions,
            order=order,
            enabled=enabled,
        )

        workflow.additional_properties = d
        return workflow

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
