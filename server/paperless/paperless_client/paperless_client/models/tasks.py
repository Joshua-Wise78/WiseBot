from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Tasks")


@_attrs_define
class Tasks:
    """
    Attributes:
        redis_url (str):
        redis_status (str):
        redis_error (str):
        celery_status (str):
    """

    redis_url: str
    redis_status: str
    redis_error: str
    celery_status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        redis_url = self.redis_url

        redis_status = self.redis_status

        redis_error = self.redis_error

        celery_status = self.celery_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "redis_url": redis_url,
                "redis_status": redis_status,
                "redis_error": redis_error,
                "celery_status": celery_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        redis_url = d.pop("redis_url")

        redis_status = d.pop("redis_status")

        redis_error = d.pop("redis_error")

        celery_status = d.pop("celery_status")

        tasks = cls(
            redis_url=redis_url,
            redis_status=redis_status,
            redis_error=redis_error,
            celery_status=celery_status,
        )

        tasks.additional_properties = d
        return tasks

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
