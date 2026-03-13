from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rule_type_enum import RuleTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SavedViewFilterRuleRequest")


@_attrs_define
class SavedViewFilterRuleRequest:
    """
    Attributes:
        rule_type (RuleTypeEnum): * `0` - title contains
            * `1` - content contains
            * `2` - ASN is
            * `3` - correspondent is
            * `4` - document type is
            * `5` - is in inbox
            * `6` - has tag
            * `7` - has any tag
            * `8` - created before
            * `9` - created after
            * `10` - created year is
            * `11` - created month is
            * `12` - created day is
            * `13` - added before
            * `14` - added after
            * `15` - modified before
            * `16` - modified after
            * `17` - does not have tag
            * `18` - does not have ASN
            * `19` - title or content contains
            * `20` - fulltext query
            * `21` - more like this
            * `22` - has tags in
            * `23` - ASN greater than
            * `24` - ASN less than
            * `25` - storage path is
            * `26` - has correspondent in
            * `27` - does not have correspondent in
            * `28` - has document type in
            * `29` - does not have document type in
            * `30` - has storage path in
            * `31` - does not have storage path in
            * `32` - owner is
            * `33` - has owner in
            * `34` - does not have owner
            * `35` - does not have owner in
            * `36` - has custom field value
            * `37` - is shared by me
            * `38` - has custom fields
            * `39` - has custom field in
            * `40` - does not have custom field in
            * `41` - does not have custom field
            * `42` - custom fields query
            * `43` - created to
            * `44` - created from
            * `45` - added to
            * `46` - added from
            * `47` - mime type is
        value (None | str | Unset):
    """

    rule_type: RuleTypeEnum
    value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type = self.rule_type.value

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = RuleTypeEnum(d.pop("rule_type"))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        saved_view_filter_rule_request = cls(
            rule_type=rule_type,
            value=value,
        )

        saved_view_filter_rule_request.additional_properties = d
        return saved_view_filter_rule_request

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
