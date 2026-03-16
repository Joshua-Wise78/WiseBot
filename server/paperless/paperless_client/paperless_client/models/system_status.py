from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.classifier import Classifier
    from ..models.database import Database
    from ..models.index import Index
    from ..models.sanity_check import SanityCheck
    from ..models.storage import Storage
    from ..models.tasks import Tasks


T = TypeVar("T", bound="SystemStatus")


@_attrs_define
class SystemStatus:
    """
    Attributes:
        pngx_version (str):
        server_os (str):
        install_type (str):
        storage (Storage):
        database (Database):
        tasks (Tasks):
        index (Index):
        classifier (Classifier):
        sanity_check (SanityCheck):
    """

    pngx_version: str
    server_os: str
    install_type: str
    storage: Storage
    database: Database
    tasks: Tasks
    index: Index
    classifier: Classifier
    sanity_check: SanityCheck
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pngx_version = self.pngx_version

        server_os = self.server_os

        install_type = self.install_type

        storage = self.storage.to_dict()

        database = self.database.to_dict()

        tasks = self.tasks.to_dict()

        index = self.index.to_dict()

        classifier = self.classifier.to_dict()

        sanity_check = self.sanity_check.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pngx_version": pngx_version,
                "server_os": server_os,
                "install_type": install_type,
                "storage": storage,
                "database": database,
                "tasks": tasks,
                "index": index,
                "classifier": classifier,
                "sanity_check": sanity_check,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.classifier import Classifier
        from ..models.database import Database
        from ..models.index import Index
        from ..models.sanity_check import SanityCheck
        from ..models.storage import Storage
        from ..models.tasks import Tasks

        d = dict(src_dict)
        pngx_version = d.pop("pngx_version")

        server_os = d.pop("server_os")

        install_type = d.pop("install_type")

        storage = Storage.from_dict(d.pop("storage"))

        database = Database.from_dict(d.pop("database"))

        tasks = Tasks.from_dict(d.pop("tasks"))

        index = Index.from_dict(d.pop("index"))

        classifier = Classifier.from_dict(d.pop("classifier"))

        sanity_check = SanityCheck.from_dict(d.pop("sanity_check"))

        system_status = cls(
            pngx_version=pngx_version,
            server_os=server_os,
            install_type=install_type,
            storage=storage,
            database=database,
            tasks=tasks,
            index=index,
            classifier=classifier,
            sanity_check=sanity_check,
        )

        system_status.additional_properties = d
        return system_status

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
