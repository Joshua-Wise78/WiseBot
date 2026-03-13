from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum
from ..models.display_mode_enum import DisplayModeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.saved_view_filter_rule_request import SavedViewFilterRuleRequest


T = TypeVar("T", bound="SavedViewRequest")


@_attrs_define
class SavedViewRequest:
    """
    Attributes:
        name (str):
        show_on_dashboard (bool):
        show_in_sidebar (bool):
        filter_rules (list[SavedViewFilterRuleRequest]):
        sort_field (None | str | Unset):
        sort_reverse (bool | Unset):
        page_size (int | None | Unset):
        display_mode (BlankEnum | DisplayModeEnum | None | Unset):
        display_fields (Any | Unset):
        owner (int | None | Unset):
    """

    name: str
    show_on_dashboard: bool
    show_in_sidebar: bool
    filter_rules: list[SavedViewFilterRuleRequest]
    sort_field: None | str | Unset = UNSET
    sort_reverse: bool | Unset = UNSET
    page_size: int | None | Unset = UNSET
    display_mode: BlankEnum | DisplayModeEnum | None | Unset = UNSET
    display_fields: Any | Unset = UNSET
    owner: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        show_on_dashboard = self.show_on_dashboard

        show_in_sidebar = self.show_in_sidebar

        filter_rules = []
        for filter_rules_item_data in self.filter_rules:
            filter_rules_item = filter_rules_item_data.to_dict()
            filter_rules.append(filter_rules_item)

        sort_field: None | str | Unset
        if isinstance(self.sort_field, Unset):
            sort_field = UNSET
        else:
            sort_field = self.sort_field

        sort_reverse = self.sort_reverse

        page_size: int | None | Unset
        if isinstance(self.page_size, Unset):
            page_size = UNSET
        else:
            page_size = self.page_size

        display_mode: None | str | Unset
        if isinstance(self.display_mode, Unset):
            display_mode = UNSET
        elif isinstance(self.display_mode, DisplayModeEnum):
            display_mode = self.display_mode.value
        elif isinstance(self.display_mode, BlankEnum):
            display_mode = self.display_mode.value
        else:
            display_mode = self.display_mode

        display_fields = self.display_fields

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "show_on_dashboard": show_on_dashboard,
                "show_in_sidebar": show_in_sidebar,
                "filter_rules": filter_rules,
            }
        )
        if sort_field is not UNSET:
            field_dict["sort_field"] = sort_field
        if sort_reverse is not UNSET:
            field_dict["sort_reverse"] = sort_reverse
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if display_mode is not UNSET:
            field_dict["display_mode"] = display_mode
        if display_fields is not UNSET:
            field_dict["display_fields"] = display_fields
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("show_on_dashboard", (None, str(self.show_on_dashboard).encode(), "text/plain")))

        files.append(("show_in_sidebar", (None, str(self.show_in_sidebar).encode(), "text/plain")))

        for filter_rules_item_element in self.filter_rules:
            files.append(
                ("filter_rules", (None, json.dumps(filter_rules_item_element.to_dict()).encode(), "application/json"))
            )

        if not isinstance(self.sort_field, Unset):
            if isinstance(self.sort_field, str):
                files.append(("sort_field", (None, str(self.sort_field).encode(), "text/plain")))
            else:
                files.append(("sort_field", (None, str(self.sort_field).encode(), "text/plain")))

        if not isinstance(self.sort_reverse, Unset):
            files.append(("sort_reverse", (None, str(self.sort_reverse).encode(), "text/plain")))

        if not isinstance(self.page_size, Unset):
            if isinstance(self.page_size, int):
                files.append(("page_size", (None, str(self.page_size).encode(), "text/plain")))
            else:
                files.append(("page_size", (None, str(self.page_size).encode(), "text/plain")))

        if not isinstance(self.display_mode, Unset):
            if isinstance(self.display_mode, DisplayModeEnum):
                files.append(("display_mode", (None, str(self.display_mode.value).encode(), "text/plain")))
            elif isinstance(self.display_mode, BlankEnum):
                files.append(("display_mode", (None, str(self.display_mode.value).encode(), "text/plain")))
            else:
                files.append(("display_mode", (None, str(self.display_mode).encode(), "text/plain")))

        if not isinstance(self.display_fields, Unset):
            files.append(("display_fields", (None, str(self.display_fields).encode(), "text/plain")))

        if not isinstance(self.owner, Unset):
            if isinstance(self.owner, int):
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))
            else:
                files.append(("owner", (None, str(self.owner).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saved_view_filter_rule_request import SavedViewFilterRuleRequest

        d = dict(src_dict)
        name = d.pop("name")

        show_on_dashboard = d.pop("show_on_dashboard")

        show_in_sidebar = d.pop("show_in_sidebar")

        filter_rules = []
        _filter_rules = d.pop("filter_rules")
        for filter_rules_item_data in _filter_rules:
            filter_rules_item = SavedViewFilterRuleRequest.from_dict(filter_rules_item_data)

            filter_rules.append(filter_rules_item)

        def _parse_sort_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sort_field = _parse_sort_field(d.pop("sort_field", UNSET))

        sort_reverse = d.pop("sort_reverse", UNSET)

        def _parse_page_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_size = _parse_page_size(d.pop("page_size", UNSET))

        def _parse_display_mode(data: object) -> BlankEnum | DisplayModeEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                display_mode_type_0 = DisplayModeEnum(data)

                return display_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                display_mode_type_1 = BlankEnum(data)

                return display_mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | DisplayModeEnum | None | Unset, data)

        display_mode = _parse_display_mode(d.pop("display_mode", UNSET))

        display_fields = d.pop("display_fields", UNSET)

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        saved_view_request = cls(
            name=name,
            show_on_dashboard=show_on_dashboard,
            show_in_sidebar=show_in_sidebar,
            filter_rules=filter_rules,
            sort_field=sort_field,
            sort_reverse=sort_reverse,
            page_size=page_size,
            display_mode=display_mode,
            display_fields=display_fields,
            owner=owner,
        )

        saved_view_request.additional_properties = d
        return saved_view_request

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
