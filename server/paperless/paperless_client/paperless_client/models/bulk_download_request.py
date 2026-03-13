from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compression_enum import CompressionEnum
from ..models.content_enum import ContentEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkDownloadRequest")


@_attrs_define
class BulkDownloadRequest:
    """
    Attributes:
        documents (list[int]):
        content (ContentEnum | Unset): * `archive` - archive
            * `originals` - originals
            * `both` - both Default: ContentEnum.ARCHIVE.
        compression (CompressionEnum | Unset): * `none` - none
            * `deflated` - deflated
            * `bzip2` - bzip2
            * `lzma` - lzma Default: CompressionEnum.NONE.
        follow_formatting (bool | Unset):  Default: False.
    """

    documents: list[int]
    content: ContentEnum | Unset = ContentEnum.ARCHIVE
    compression: CompressionEnum | Unset = CompressionEnum.NONE
    follow_formatting: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        documents = self.documents

        content: str | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.value

        compression: str | Unset = UNSET
        if not isinstance(self.compression, Unset):
            compression = self.compression.value

        follow_formatting = self.follow_formatting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documents": documents,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if compression is not UNSET:
            field_dict["compression"] = compression
        if follow_formatting is not UNSET:
            field_dict["follow_formatting"] = follow_formatting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        documents = cast(list[int], d.pop("documents"))

        _content = d.pop("content", UNSET)
        content: ContentEnum | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ContentEnum(_content)

        _compression = d.pop("compression", UNSET)
        compression: CompressionEnum | Unset
        if isinstance(_compression, Unset):
            compression = UNSET
        else:
            compression = CompressionEnum(_compression)

        follow_formatting = d.pop("follow_formatting", UNSET)

        bulk_download_request = cls(
            documents=documents,
            content=content,
            compression=compression,
            follow_formatting=follow_formatting,
        )

        bulk_download_request.additional_properties = d
        return bulk_download_request

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
