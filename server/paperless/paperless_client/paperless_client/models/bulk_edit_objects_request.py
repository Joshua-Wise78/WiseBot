from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.object_type_enum import ObjectTypeEnum
from ..models.operation_enum import OperationEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_edit_objects_request_set_permissions import BulkEditObjectsRequestSetPermissions


T = TypeVar("T", bound="BulkEditObjectsRequest")


@_attrs_define
class BulkEditObjectsRequest:
    """
    Attributes:
        objects (list[int]):
        object_type (ObjectTypeEnum): * `tags` - tags
            * `correspondents` - correspondents
            * `document_types` - document_types
            * `storage_paths` - storage_paths
        operation (OperationEnum): * `set_permissions` - set_permissions
            * `delete` - delete
        owner (int | None | Unset):
        permissions (BulkEditObjectsRequestSetPermissions | Unset):
        merge (bool | Unset):  Default: False.
    """

    objects: list[int]
    object_type: ObjectTypeEnum
    operation: OperationEnum
    owner: int | None | Unset = UNSET
    permissions: BulkEditObjectsRequestSetPermissions | Unset = UNSET
    merge: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objects = self.objects

        object_type = self.object_type.value

        operation = self.operation.value

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        merge = self.merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "objects": objects,
                "object_type": object_type,
                "operation": operation,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if merge is not UNSET:
            field_dict["merge"] = merge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_edit_objects_request_set_permissions import BulkEditObjectsRequestSetPermissions

        d = dict(src_dict)
        objects = cast(list[int], d.pop("objects"))

        object_type = ObjectTypeEnum(d.pop("object_type"))

        operation = OperationEnum(d.pop("operation"))

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        _permissions = d.pop("permissions", UNSET)
        permissions: BulkEditObjectsRequestSetPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = BulkEditObjectsRequestSetPermissions.from_dict(_permissions)

        merge = d.pop("merge", UNSET)

        bulk_edit_objects_request = cls(
            objects=objects,
            object_type=object_type,
            operation=operation,
            owner=owner,
            permissions=permissions,
            merge=merge,
        )

        bulk_edit_objects_request.additional_properties = d
        return bulk_edit_objects_request

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
