from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_instance_value_type_3 import CustomFieldInstanceValueType3


T = TypeVar("T", bound="CustomFieldInstance")


@_attrs_define
class CustomFieldInstance:
    """
    Attributes:
        value (CustomFieldInstanceValueType3 | float | int | None | str): Given the *incoming* primitive data, return
            the value for this field
            that should be validated and transformed to a native value.
        field (int):
    """

    value: CustomFieldInstanceValueType3 | float | int | None | str
    field: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_field_instance_value_type_3 import CustomFieldInstanceValueType3

        value: dict[str, Any] | float | int | None | str
        if isinstance(self.value, CustomFieldInstanceValueType3):
            value = self.value.to_dict()
        else:
            value = self.value

        field = self.field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "field": field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_instance_value_type_3 import CustomFieldInstanceValueType3

        d = dict(src_dict)

        def _parse_value(data: object) -> CustomFieldInstanceValueType3 | float | int | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_3 = CustomFieldInstanceValueType3.from_dict(data)

                return value_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomFieldInstanceValueType3 | float | int | None | str, data)

        value = _parse_value(d.pop("value"))

        field = d.pop("field")

        custom_field_instance = cls(
            value=value,
            field=field,
        )

        custom_field_instance.additional_properties = d
        return custom_field_instance

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
