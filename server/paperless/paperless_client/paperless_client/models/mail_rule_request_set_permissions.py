from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mail_rule_request_set_permissions_change import MailRuleRequestSetPermissionsChange
    from ..models.mail_rule_request_set_permissions_view import MailRuleRequestSetPermissionsView


T = TypeVar("T", bound="MailRuleRequestSetPermissions")


@_attrs_define
class MailRuleRequestSetPermissions:
    """
    Attributes:
        view (MailRuleRequestSetPermissionsView | Unset):
        change (MailRuleRequestSetPermissionsChange | Unset):
    """

    view: MailRuleRequestSetPermissionsView | Unset = UNSET
    change: MailRuleRequestSetPermissionsChange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        view: dict[str, Any] | Unset = UNSET
        if not isinstance(self.view, Unset):
            view = self.view.to_dict()

        change: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change, Unset):
            change = self.change.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if view is not UNSET:
            field_dict["view"] = view
        if change is not UNSET:
            field_dict["change"] = change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mail_rule_request_set_permissions_change import MailRuleRequestSetPermissionsChange
        from ..models.mail_rule_request_set_permissions_view import MailRuleRequestSetPermissionsView

        d = dict(src_dict)
        _view = d.pop("view", UNSET)
        view: MailRuleRequestSetPermissionsView | Unset
        if isinstance(_view, Unset):
            view = UNSET
        else:
            view = MailRuleRequestSetPermissionsView.from_dict(_view)

        _change = d.pop("change", UNSET)
        change: MailRuleRequestSetPermissionsChange | Unset
        if isinstance(_change, Unset):
            change = UNSET
        else:
            change = MailRuleRequestSetPermissionsChange.from_dict(_change)

        mail_rule_request_set_permissions = cls(
            view=view,
            change=change,
        )

        mail_rule_request_set_permissions.additional_properties = d
        return mail_rule_request_set_permissions

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
