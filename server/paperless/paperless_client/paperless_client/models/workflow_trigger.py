from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_date_field_enum import ScheduleDateFieldEnum
from ..models.sources_enum import SourcesEnum
from ..models.workflow_trigger_matching_algorithm_enum import WorkflowTriggerMatchingAlgorithmEnum
from ..models.workflow_trigger_type_enum import WorkflowTriggerTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowTrigger")


@_attrs_define
class WorkflowTrigger:
    """
    Attributes:
        type_ (WorkflowTriggerTypeEnum): * `1` - Consumption Started
            * `2` - Document Added
            * `3` - Document Updated
            * `4` - Scheduled
        id (int | None | Unset):
        sources (list[SourcesEnum] | Unset):
        filter_path (None | str | Unset): Only consume documents with a path that matches this if specified. Wildcards
            specified as * are allowed. Case insensitive.
        filter_filename (None | str | Unset): Only consume documents which entirely match this filename if specified.
            Wildcards such as *.pdf or *invoice* are allowed. Case insensitive.
        filter_mailrule (int | None | Unset):
        matching_algorithm (WorkflowTriggerMatchingAlgorithmEnum | Unset): * `0` - None
            * `1` - Any word
            * `2` - All words
            * `3` - Exact match
            * `4` - Regular expression
            * `5` - Fuzzy word
        match (str | Unset):
        is_insensitive (bool | Unset):
        filter_has_tags (list[int] | Unset):
        filter_has_all_tags (list[int] | Unset):
        filter_has_not_tags (list[int] | Unset):
        filter_custom_field_query (None | str | Unset): JSON-encoded custom field query expression.
        filter_has_not_correspondents (list[int] | Unset):
        filter_has_not_document_types (list[int] | Unset):
        filter_has_not_storage_paths (list[int] | Unset):
        filter_has_correspondent (int | None | Unset):
        filter_has_document_type (int | None | Unset):
        filter_has_storage_path (int | None | Unset):
        schedule_offset_days (int | Unset): The number of days to offset the schedule trigger by.
        schedule_is_recurring (bool | Unset): If the schedule should be recurring.
        schedule_recurring_interval_days (int | Unset): The number of days between recurring schedule triggers.
        schedule_date_field (ScheduleDateFieldEnum | Unset): * `added` - Added
            * `created` - Created
            * `modified` - Modified
            * `custom_field` - Custom Field
        schedule_date_custom_field (int | None | Unset):
    """

    type_: WorkflowTriggerTypeEnum
    id: int | None | Unset = UNSET
    sources: list[SourcesEnum] | Unset = UNSET
    filter_path: None | str | Unset = UNSET
    filter_filename: None | str | Unset = UNSET
    filter_mailrule: int | None | Unset = UNSET
    matching_algorithm: WorkflowTriggerMatchingAlgorithmEnum | Unset = UNSET
    match: str | Unset = UNSET
    is_insensitive: bool | Unset = UNSET
    filter_has_tags: list[int] | Unset = UNSET
    filter_has_all_tags: list[int] | Unset = UNSET
    filter_has_not_tags: list[int] | Unset = UNSET
    filter_custom_field_query: None | str | Unset = UNSET
    filter_has_not_correspondents: list[int] | Unset = UNSET
    filter_has_not_document_types: list[int] | Unset = UNSET
    filter_has_not_storage_paths: list[int] | Unset = UNSET
    filter_has_correspondent: int | None | Unset = UNSET
    filter_has_document_type: int | None | Unset = UNSET
    filter_has_storage_path: int | None | Unset = UNSET
    schedule_offset_days: int | Unset = UNSET
    schedule_is_recurring: bool | Unset = UNSET
    schedule_recurring_interval_days: int | Unset = UNSET
    schedule_date_field: ScheduleDateFieldEnum | Unset = UNSET
    schedule_date_custom_field: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        sources: list[int] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.value
                sources.append(sources_item)

        filter_path: None | str | Unset
        if isinstance(self.filter_path, Unset):
            filter_path = UNSET
        else:
            filter_path = self.filter_path

        filter_filename: None | str | Unset
        if isinstance(self.filter_filename, Unset):
            filter_filename = UNSET
        else:
            filter_filename = self.filter_filename

        filter_mailrule: int | None | Unset
        if isinstance(self.filter_mailrule, Unset):
            filter_mailrule = UNSET
        else:
            filter_mailrule = self.filter_mailrule

        matching_algorithm: int | Unset = UNSET
        if not isinstance(self.matching_algorithm, Unset):
            matching_algorithm = self.matching_algorithm.value

        match = self.match

        is_insensitive = self.is_insensitive

        filter_has_tags: list[int] | Unset = UNSET
        if not isinstance(self.filter_has_tags, Unset):
            filter_has_tags = self.filter_has_tags

        filter_has_all_tags: list[int] | Unset = UNSET
        if not isinstance(self.filter_has_all_tags, Unset):
            filter_has_all_tags = self.filter_has_all_tags

        filter_has_not_tags: list[int] | Unset = UNSET
        if not isinstance(self.filter_has_not_tags, Unset):
            filter_has_not_tags = self.filter_has_not_tags

        filter_custom_field_query: None | str | Unset
        if isinstance(self.filter_custom_field_query, Unset):
            filter_custom_field_query = UNSET
        else:
            filter_custom_field_query = self.filter_custom_field_query

        filter_has_not_correspondents: list[int] | Unset = UNSET
        if not isinstance(self.filter_has_not_correspondents, Unset):
            filter_has_not_correspondents = self.filter_has_not_correspondents

        filter_has_not_document_types: list[int] | Unset = UNSET
        if not isinstance(self.filter_has_not_document_types, Unset):
            filter_has_not_document_types = self.filter_has_not_document_types

        filter_has_not_storage_paths: list[int] | Unset = UNSET
        if not isinstance(self.filter_has_not_storage_paths, Unset):
            filter_has_not_storage_paths = self.filter_has_not_storage_paths

        filter_has_correspondent: int | None | Unset
        if isinstance(self.filter_has_correspondent, Unset):
            filter_has_correspondent = UNSET
        else:
            filter_has_correspondent = self.filter_has_correspondent

        filter_has_document_type: int | None | Unset
        if isinstance(self.filter_has_document_type, Unset):
            filter_has_document_type = UNSET
        else:
            filter_has_document_type = self.filter_has_document_type

        filter_has_storage_path: int | None | Unset
        if isinstance(self.filter_has_storage_path, Unset):
            filter_has_storage_path = UNSET
        else:
            filter_has_storage_path = self.filter_has_storage_path

        schedule_offset_days = self.schedule_offset_days

        schedule_is_recurring = self.schedule_is_recurring

        schedule_recurring_interval_days = self.schedule_recurring_interval_days

        schedule_date_field: str | Unset = UNSET
        if not isinstance(self.schedule_date_field, Unset):
            schedule_date_field = self.schedule_date_field.value

        schedule_date_custom_field: int | None | Unset
        if isinstance(self.schedule_date_custom_field, Unset):
            schedule_date_custom_field = UNSET
        else:
            schedule_date_custom_field = self.schedule_date_custom_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if sources is not UNSET:
            field_dict["sources"] = sources
        if filter_path is not UNSET:
            field_dict["filter_path"] = filter_path
        if filter_filename is not UNSET:
            field_dict["filter_filename"] = filter_filename
        if filter_mailrule is not UNSET:
            field_dict["filter_mailrule"] = filter_mailrule
        if matching_algorithm is not UNSET:
            field_dict["matching_algorithm"] = matching_algorithm
        if match is not UNSET:
            field_dict["match"] = match
        if is_insensitive is not UNSET:
            field_dict["is_insensitive"] = is_insensitive
        if filter_has_tags is not UNSET:
            field_dict["filter_has_tags"] = filter_has_tags
        if filter_has_all_tags is not UNSET:
            field_dict["filter_has_all_tags"] = filter_has_all_tags
        if filter_has_not_tags is not UNSET:
            field_dict["filter_has_not_tags"] = filter_has_not_tags
        if filter_custom_field_query is not UNSET:
            field_dict["filter_custom_field_query"] = filter_custom_field_query
        if filter_has_not_correspondents is not UNSET:
            field_dict["filter_has_not_correspondents"] = filter_has_not_correspondents
        if filter_has_not_document_types is not UNSET:
            field_dict["filter_has_not_document_types"] = filter_has_not_document_types
        if filter_has_not_storage_paths is not UNSET:
            field_dict["filter_has_not_storage_paths"] = filter_has_not_storage_paths
        if filter_has_correspondent is not UNSET:
            field_dict["filter_has_correspondent"] = filter_has_correspondent
        if filter_has_document_type is not UNSET:
            field_dict["filter_has_document_type"] = filter_has_document_type
        if filter_has_storage_path is not UNSET:
            field_dict["filter_has_storage_path"] = filter_has_storage_path
        if schedule_offset_days is not UNSET:
            field_dict["schedule_offset_days"] = schedule_offset_days
        if schedule_is_recurring is not UNSET:
            field_dict["schedule_is_recurring"] = schedule_is_recurring
        if schedule_recurring_interval_days is not UNSET:
            field_dict["schedule_recurring_interval_days"] = schedule_recurring_interval_days
        if schedule_date_field is not UNSET:
            field_dict["schedule_date_field"] = schedule_date_field
        if schedule_date_custom_field is not UNSET:
            field_dict["schedule_date_custom_field"] = schedule_date_custom_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = WorkflowTriggerTypeEnum(d.pop("type"))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _sources = d.pop("sources", UNSET)
        sources: list[SourcesEnum] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = SourcesEnum(sources_item_data)

                sources.append(sources_item)

        def _parse_filter_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_path = _parse_filter_path(d.pop("filter_path", UNSET))

        def _parse_filter_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_filename = _parse_filter_filename(d.pop("filter_filename", UNSET))

        def _parse_filter_mailrule(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_mailrule = _parse_filter_mailrule(d.pop("filter_mailrule", UNSET))

        _matching_algorithm = d.pop("matching_algorithm", UNSET)
        matching_algorithm: WorkflowTriggerMatchingAlgorithmEnum | Unset
        if isinstance(_matching_algorithm, Unset):
            matching_algorithm = UNSET
        else:
            matching_algorithm = WorkflowTriggerMatchingAlgorithmEnum(_matching_algorithm)

        match = d.pop("match", UNSET)

        is_insensitive = d.pop("is_insensitive", UNSET)

        filter_has_tags = cast(list[int], d.pop("filter_has_tags", UNSET))

        filter_has_all_tags = cast(list[int], d.pop("filter_has_all_tags", UNSET))

        filter_has_not_tags = cast(list[int], d.pop("filter_has_not_tags", UNSET))

        def _parse_filter_custom_field_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_custom_field_query = _parse_filter_custom_field_query(d.pop("filter_custom_field_query", UNSET))

        filter_has_not_correspondents = cast(list[int], d.pop("filter_has_not_correspondents", UNSET))

        filter_has_not_document_types = cast(list[int], d.pop("filter_has_not_document_types", UNSET))

        filter_has_not_storage_paths = cast(list[int], d.pop("filter_has_not_storage_paths", UNSET))

        def _parse_filter_has_correspondent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_has_correspondent = _parse_filter_has_correspondent(d.pop("filter_has_correspondent", UNSET))

        def _parse_filter_has_document_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_has_document_type = _parse_filter_has_document_type(d.pop("filter_has_document_type", UNSET))

        def _parse_filter_has_storage_path(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        filter_has_storage_path = _parse_filter_has_storage_path(d.pop("filter_has_storage_path", UNSET))

        schedule_offset_days = d.pop("schedule_offset_days", UNSET)

        schedule_is_recurring = d.pop("schedule_is_recurring", UNSET)

        schedule_recurring_interval_days = d.pop("schedule_recurring_interval_days", UNSET)

        _schedule_date_field = d.pop("schedule_date_field", UNSET)
        schedule_date_field: ScheduleDateFieldEnum | Unset
        if isinstance(_schedule_date_field, Unset):
            schedule_date_field = UNSET
        else:
            schedule_date_field = ScheduleDateFieldEnum(_schedule_date_field)

        def _parse_schedule_date_custom_field(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schedule_date_custom_field = _parse_schedule_date_custom_field(d.pop("schedule_date_custom_field", UNSET))

        workflow_trigger = cls(
            type_=type_,
            id=id,
            sources=sources,
            filter_path=filter_path,
            filter_filename=filter_filename,
            filter_mailrule=filter_mailrule,
            matching_algorithm=matching_algorithm,
            match=match,
            is_insensitive=is_insensitive,
            filter_has_tags=filter_has_tags,
            filter_has_all_tags=filter_has_all_tags,
            filter_has_not_tags=filter_has_not_tags,
            filter_custom_field_query=filter_custom_field_query,
            filter_has_not_correspondents=filter_has_not_correspondents,
            filter_has_not_document_types=filter_has_not_document_types,
            filter_has_not_storage_paths=filter_has_not_storage_paths,
            filter_has_correspondent=filter_has_correspondent,
            filter_has_document_type=filter_has_document_type,
            filter_has_storage_path=filter_has_storage_path,
            schedule_offset_days=schedule_offset_days,
            schedule_is_recurring=schedule_is_recurring,
            schedule_recurring_interval_days=schedule_recurring_interval_days,
            schedule_date_field=schedule_date_field,
            schedule_date_custom_field=schedule_date_custom_field,
        )

        workflow_trigger.additional_properties = d
        return workflow_trigger

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
