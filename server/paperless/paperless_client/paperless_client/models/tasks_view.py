from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_enum import StatusEnum
from ..models.task_name_enum import TaskNameEnum
from ..models.tasks_view_type_enum import TasksViewTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TasksView")


@_attrs_define
class TasksView:
    """
    Attributes:
        id (int):
        task_id (str): Celery ID for the Task that was run
        related_document (None | str):
        task_name (None | TaskNameEnum | Unset): Name of the task that was run

            * `consume_file` - Consume File
            * `train_classifier` - Train Classifier
            * `check_sanity` - Check Sanity
            * `index_optimize` - Index Optimize
        task_file_name (None | str | Unset): Name of the file which the Task was run for
        date_created (datetime.datetime | None | Unset): Datetime field when the task result was created in UTC
        date_done (datetime.datetime | None | Unset): Datetime field when the task was completed in UTC
        type_ (TasksViewTypeEnum | Unset): * `auto_task` - Auto Task
            * `scheduled_task` - Scheduled Task
            * `manual_task` - Manual Task
        status (StatusEnum | Unset): * `FAILURE` - FAILURE
            * `PENDING` - PENDING
            * `RECEIVED` - RECEIVED
            * `RETRY` - RETRY
            * `REVOKED` - REVOKED
            * `STARTED` - STARTED
            * `SUCCESS` - SUCCESS
        result (None | str | Unset): The data returned by the task
        acknowledged (bool | Unset): If the task is acknowledged via the frontend or API
        owner (int | None | Unset):
    """

    id: int
    task_id: str
    related_document: None | str
    task_name: None | TaskNameEnum | Unset = UNSET
    task_file_name: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_done: datetime.datetime | None | Unset = UNSET
    type_: TasksViewTypeEnum | Unset = UNSET
    status: StatusEnum | Unset = UNSET
    result: None | str | Unset = UNSET
    acknowledged: bool | Unset = UNSET
    owner: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        task_id = self.task_id

        related_document: None | str
        related_document = self.related_document

        task_name: None | str | Unset
        if isinstance(self.task_name, Unset):
            task_name = UNSET
        elif isinstance(self.task_name, TaskNameEnum):
            task_name = self.task_name.value
        else:
            task_name = self.task_name

        task_file_name: None | str | Unset
        if isinstance(self.task_file_name, Unset):
            task_file_name = UNSET
        else:
            task_file_name = self.task_file_name

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_done: None | str | Unset
        if isinstance(self.date_done, Unset):
            date_done = UNSET
        elif isinstance(self.date_done, datetime.datetime):
            date_done = self.date_done.isoformat()
        else:
            date_done = self.date_done

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        result: None | str | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        acknowledged = self.acknowledged

        owner: int | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "task_id": task_id,
                "related_document": related_document,
            }
        )
        if task_name is not UNSET:
            field_dict["task_name"] = task_name
        if task_file_name is not UNSET:
            field_dict["task_file_name"] = task_file_name
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_done is not UNSET:
            field_dict["date_done"] = date_done
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result
        if acknowledged is not UNSET:
            field_dict["acknowledged"] = acknowledged
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        task_id = d.pop("task_id")

        def _parse_related_document(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        related_document = _parse_related_document(d.pop("related_document"))

        def _parse_task_name(data: object) -> None | TaskNameEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_name_type_0 = TaskNameEnum(data)

                return task_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskNameEnum | Unset, data)

        task_name = _parse_task_name(d.pop("task_name", UNSET))

        def _parse_task_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_file_name = _parse_task_file_name(d.pop("task_file_name", UNSET))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = isoparse(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_done(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_done_type_0 = isoparse(data)

                return date_done_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_done = _parse_date_done(d.pop("date_done", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: TasksViewTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TasksViewTypeEnum(_type_)

        _status = d.pop("status", UNSET)
        status: StatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusEnum(_status)

        def _parse_result(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        acknowledged = d.pop("acknowledged", UNSET)

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        tasks_view = cls(
            id=id,
            task_id=task_id,
            related_document=related_document,
            task_name=task_name,
            task_file_name=task_file_name,
            date_created=date_created,
            date_done=date_done,
            type_=type_,
            status=status,
            result=result,
            acknowledged=acknowledged,
            owner=owner,
        )

        tasks_view.additional_properties = d
        return tasks_view

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
