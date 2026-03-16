from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_archive_metadata import MetadataArchiveMetadata
    from ..models.metadata_original_metadata import MetadataOriginalMetadata


T = TypeVar("T", bound="Metadata")


@_attrs_define
class Metadata:
    """
    Attributes:
        original_checksum (str):
        original_size (int):
        original_mime_type (str):
        media_filename (str):
        has_archive_version (bool):
        original_metadata (MetadataOriginalMetadata):
        archive_checksum (str):
        archive_media_filename (str):
        original_filename (str):
        archive_size (int):
        archive_metadata (MetadataArchiveMetadata):
        lang (str):
    """

    original_checksum: str
    original_size: int
    original_mime_type: str
    media_filename: str
    has_archive_version: bool
    original_metadata: MetadataOriginalMetadata
    archive_checksum: str
    archive_media_filename: str
    original_filename: str
    archive_size: int
    archive_metadata: MetadataArchiveMetadata
    lang: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_checksum = self.original_checksum

        original_size = self.original_size

        original_mime_type = self.original_mime_type

        media_filename = self.media_filename

        has_archive_version = self.has_archive_version

        original_metadata = self.original_metadata.to_dict()

        archive_checksum = self.archive_checksum

        archive_media_filename = self.archive_media_filename

        original_filename = self.original_filename

        archive_size = self.archive_size

        archive_metadata = self.archive_metadata.to_dict()

        lang = self.lang

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "original_checksum": original_checksum,
                "original_size": original_size,
                "original_mime_type": original_mime_type,
                "media_filename": media_filename,
                "has_archive_version": has_archive_version,
                "original_metadata": original_metadata,
                "archive_checksum": archive_checksum,
                "archive_media_filename": archive_media_filename,
                "original_filename": original_filename,
                "archive_size": archive_size,
                "archive_metadata": archive_metadata,
                "lang": lang,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_archive_metadata import MetadataArchiveMetadata
        from ..models.metadata_original_metadata import MetadataOriginalMetadata

        d = dict(src_dict)
        original_checksum = d.pop("original_checksum")

        original_size = d.pop("original_size")

        original_mime_type = d.pop("original_mime_type")

        media_filename = d.pop("media_filename")

        has_archive_version = d.pop("has_archive_version")

        original_metadata = MetadataOriginalMetadata.from_dict(d.pop("original_metadata"))

        archive_checksum = d.pop("archive_checksum")

        archive_media_filename = d.pop("archive_media_filename")

        original_filename = d.pop("original_filename")

        archive_size = d.pop("archive_size")

        archive_metadata = MetadataArchiveMetadata.from_dict(d.pop("archive_metadata"))

        lang = d.pop("lang")

        metadata = cls(
            original_checksum=original_checksum,
            original_size=original_size,
            original_mime_type=original_mime_type,
            media_filename=media_filename,
            has_archive_version=has_archive_version,
            original_metadata=original_metadata,
            archive_checksum=archive_checksum,
            archive_media_filename=archive_media_filename,
            original_filename=original_filename,
            archive_size=archive_size,
            archive_metadata=archive_metadata,
            lang=lang,
        )

        metadata.additional_properties = d
        return metadata

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
