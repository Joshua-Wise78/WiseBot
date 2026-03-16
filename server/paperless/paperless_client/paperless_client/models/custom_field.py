from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_type_enum import DataTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomField")


@_attrs_define
class CustomField:
    """
    Attributes:
        id (int):
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
        document_count (int):
        extra_data (Any | Unset): Extra data for the custom field, such as select options
    """

    id: int
    name: str
    data_type: DataTypeEnum
    document_count: int
    extra_data: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        data_type = self.data_type.value

        document_count = self.document_count

        extra_data = self.extra_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "data_type": data_type,
                "document_count": document_count,
            }
        )
        if extra_data is not UNSET:
            field_dict["extra_data"] = extra_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        data_type = DataTypeEnum(d.pop("data_type"))

        document_count = d.pop("document_count")

        extra_data = d.pop("extra_data", UNSET)

        custom_field = cls(
            id=id,
            name=name,
            data_type=data_type,
            document_count=document_count,
            extra_data=extra_data,
        )

        custom_field.additional_properties = d
        return custom_field

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
