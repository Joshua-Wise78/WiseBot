from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.method_enum import MethodEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_edit_request_parameters import BulkEditRequestParameters


T = TypeVar("T", bound="BulkEditRequest")


@_attrs_define
class BulkEditRequest:
    """
    Attributes:
        documents (list[int]):
        method (MethodEnum): * `set_correspondent` - set_correspondent
            * `set_document_type` - set_document_type
            * `set_storage_path` - set_storage_path
            * `add_tag` - add_tag
            * `remove_tag` - remove_tag
            * `modify_tags` - modify_tags
            * `modify_custom_fields` - modify_custom_fields
            * `delete` - delete
            * `reprocess` - reprocess
            * `set_permissions` - set_permissions
            * `rotate` - rotate
            * `merge` - merge
            * `split` - split
            * `delete_pages` - delete_pages
            * `edit_pdf` - edit_pdf
        parameters (BulkEditRequestParameters | Unset):
    """

    documents: list[int]
    method: MethodEnum
    parameters: BulkEditRequestParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        documents = self.documents

        method = self.method.value

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documents": documents,
                "method": method,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_edit_request_parameters import BulkEditRequestParameters

        d = dict(src_dict)
        documents = cast(list[int], d.pop("documents"))

        method = MethodEnum(d.pop("method"))

        _parameters = d.pop("parameters", UNSET)
        parameters: BulkEditRequestParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = BulkEditRequestParameters.from_dict(_parameters)

        bulk_edit_request = cls(
            documents=documents,
            method=method,
            parameters=parameters,
        )

        bulk_edit_request.additional_properties = d
        return bulk_edit_request

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
