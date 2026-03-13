from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.data_type_enum import DataTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldRequest")


@_attrs_define
class CustomFieldRequest:
    """
    Attributes:
        name (str):
        data_type (DataTypeEnum): * `string` - string
            * `url` - url
            * `date` - date
            * `boolean` - boolean
            * `integer` - integer
            * `float` - float
            * `monetary` - monetary
            * `documentlink` - documentlink
            * `select` - select
            * `longtext` - longtext
        extra_data (Any | Unset): Extra data for the custom field, such as select options
    """

    name: str
    data_type: DataTypeEnum
    extra_data: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        data_type = self.data_type.value

        extra_data = self.extra_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "data_type": data_type,
            }
        )
        if extra_data is not UNSET:
            field_dict["extra_data"] = extra_data

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("data_type", (None, str(self.data_type.value).encode(), "text/plain")))

        if not isinstance(self.extra_data, Unset):
            files.append(("extra_data", (None, str(self.extra_data).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        data_type = DataTypeEnum(d.pop("data_type"))

        extra_data = d.pop("extra_data", UNSET)

        custom_field_request = cls(
            name=name,
            data_type=data_type,
            extra_data=extra_data,
        )

        custom_field_request.additional_properties = d
        return custom_field_request

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
