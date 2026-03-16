from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.data_type_enum import DataTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCustomFieldRequest")


@_attrs_define
class PatchedCustomFieldRequest:
    """
    Attributes:
        name (str | Unset):
        data_type (DataTypeEnum | Unset): * `string` - string
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

    name: str | Unset = UNSET
    data_type: DataTypeEnum | Unset = UNSET
    extra_data: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        data_type: str | Unset = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        extra_data = self.extra_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if extra_data is not UNSET:
            field_dict["extra_data"] = extra_data

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.data_type, Unset):
            files.append(("data_type", (None, str(self.data_type.value).encode(), "text/plain")))

        if not isinstance(self.extra_data, Unset):
            files.append(("extra_data", (None, str(self.extra_data).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _data_type = d.pop("data_type", UNSET)
        data_type: DataTypeEnum | Unset
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = DataTypeEnum(_data_type)

        extra_data = d.pop("extra_data", UNSET)

        patched_custom_field_request = cls(
            name=name,
            data_type=data_type,
            extra_data=extra_data,
        )

        patched_custom_field_request.additional_properties = d
        return patched_custom_field_request

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
