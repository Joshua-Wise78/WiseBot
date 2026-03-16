from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.correspondent_counts import CorrespondentCounts
    from ..models.custom_field_counts import CustomFieldCounts
    from ..models.document_type_counts import DocumentTypeCounts
    from ..models.storage_path_counts import StoragePathCounts
    from ..models.tag_counts import TagCounts


T = TypeVar("T", bound="SelectionData")


@_attrs_define
class SelectionData:
    """
    Attributes:
        selected_correspondents (list[CorrespondentCounts]):
        selected_tags (list[TagCounts]):
        selected_document_types (list[DocumentTypeCounts]):
        selected_storage_paths (list[StoragePathCounts]):
        selected_custom_fields (list[CustomFieldCounts]):
    """

    selected_correspondents: list[CorrespondentCounts]
    selected_tags: list[TagCounts]
    selected_document_types: list[DocumentTypeCounts]
    selected_storage_paths: list[StoragePathCounts]
    selected_custom_fields: list[CustomFieldCounts]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selected_correspondents = []
        for selected_correspondents_item_data in self.selected_correspondents:
            selected_correspondents_item = selected_correspondents_item_data.to_dict()
            selected_correspondents.append(selected_correspondents_item)

        selected_tags = []
        for selected_tags_item_data in self.selected_tags:
            selected_tags_item = selected_tags_item_data.to_dict()
            selected_tags.append(selected_tags_item)

        selected_document_types = []
        for selected_document_types_item_data in self.selected_document_types:
            selected_document_types_item = selected_document_types_item_data.to_dict()
            selected_document_types.append(selected_document_types_item)

        selected_storage_paths = []
        for selected_storage_paths_item_data in self.selected_storage_paths:
            selected_storage_paths_item = selected_storage_paths_item_data.to_dict()
            selected_storage_paths.append(selected_storage_paths_item)

        selected_custom_fields = []
        for selected_custom_fields_item_data in self.selected_custom_fields:
            selected_custom_fields_item = selected_custom_fields_item_data.to_dict()
            selected_custom_fields.append(selected_custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selected_correspondents": selected_correspondents,
                "selected_tags": selected_tags,
                "selected_document_types": selected_document_types,
                "selected_storage_paths": selected_storage_paths,
                "selected_custom_fields": selected_custom_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.correspondent_counts import CorrespondentCounts
        from ..models.custom_field_counts import CustomFieldCounts
        from ..models.document_type_counts import DocumentTypeCounts
        from ..models.storage_path_counts import StoragePathCounts
        from ..models.tag_counts import TagCounts

        d = dict(src_dict)
        selected_correspondents = []
        _selected_correspondents = d.pop("selected_correspondents")
        for selected_correspondents_item_data in _selected_correspondents:
            selected_correspondents_item = CorrespondentCounts.from_dict(selected_correspondents_item_data)

            selected_correspondents.append(selected_correspondents_item)

        selected_tags = []
        _selected_tags = d.pop("selected_tags")
        for selected_tags_item_data in _selected_tags:
            selected_tags_item = TagCounts.from_dict(selected_tags_item_data)

            selected_tags.append(selected_tags_item)

        selected_document_types = []
        _selected_document_types = d.pop("selected_document_types")
        for selected_document_types_item_data in _selected_document_types:
            selected_document_types_item = DocumentTypeCounts.from_dict(selected_document_types_item_data)

            selected_document_types.append(selected_document_types_item)

        selected_storage_paths = []
        _selected_storage_paths = d.pop("selected_storage_paths")
        for selected_storage_paths_item_data in _selected_storage_paths:
            selected_storage_paths_item = StoragePathCounts.from_dict(selected_storage_paths_item_data)

            selected_storage_paths.append(selected_storage_paths_item)

        selected_custom_fields = []
        _selected_custom_fields = d.pop("selected_custom_fields")
        for selected_custom_fields_item_data in _selected_custom_fields:
            selected_custom_fields_item = CustomFieldCounts.from_dict(selected_custom_fields_item_data)

            selected_custom_fields.append(selected_custom_fields_item)

        selection_data = cls(
            selected_correspondents=selected_correspondents,
            selected_tags=selected_tags,
            selected_document_types=selected_document_types,
            selected_storage_paths=selected_storage_paths,
            selected_custom_fields=selected_custom_fields,
        )

        selection_data.additional_properties = d
        return selection_data

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
