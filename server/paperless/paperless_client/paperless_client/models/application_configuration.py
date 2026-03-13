from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.color_conversion_strategy_enum import ColorConversionStrategyEnum
from ..models.mode_enum import ModeEnum
from ..models.output_type_enum import OutputTypeEnum
from ..models.skip_archive_file_enum import SkipArchiveFileEnum
from ..models.unpaper_clean_enum import UnpaperCleanEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationConfiguration")


@_attrs_define
class ApplicationConfiguration:
    """
    Attributes:
        id (int):
        user_args (Any):
        barcode_tag_mapping (Any):
        output_type (BlankEnum | None | OutputTypeEnum | Unset):
        pages (int | None | Unset):
        language (None | str | Unset):
        mode (BlankEnum | ModeEnum | None | Unset):
        skip_archive_file (BlankEnum | None | SkipArchiveFileEnum | Unset):
        image_dpi (int | None | Unset):
        unpaper_clean (BlankEnum | None | UnpaperCleanEnum | Unset):
        deskew (bool | None | Unset):
        rotate_pages (bool | None | Unset):
        rotate_pages_threshold (float | None | Unset):
        max_image_pixels (float | None | Unset):
        color_conversion_strategy (BlankEnum | ColorConversionStrategyEnum | None | Unset):
        app_title (None | str | Unset):
        app_logo (None | str | Unset):
        barcodes_enabled (bool | None | Unset):
        barcode_enable_tiff_support (bool | None | Unset):
        barcode_string (None | str | Unset):
        barcode_retain_split_pages (bool | None | Unset):
        barcode_enable_asn (bool | None | Unset):
        barcode_asn_prefix (None | str | Unset):
        barcode_upscale (float | None | Unset):
        barcode_dpi (int | None | Unset):
        barcode_max_pages (int | None | Unset):
        barcode_enable_tag (bool | None | Unset):
    """

    id: int
    user_args: Any
    barcode_tag_mapping: Any
    output_type: BlankEnum | None | OutputTypeEnum | Unset = UNSET
    pages: int | None | Unset = UNSET
    language: None | str | Unset = UNSET
    mode: BlankEnum | ModeEnum | None | Unset = UNSET
    skip_archive_file: BlankEnum | None | SkipArchiveFileEnum | Unset = UNSET
    image_dpi: int | None | Unset = UNSET
    unpaper_clean: BlankEnum | None | UnpaperCleanEnum | Unset = UNSET
    deskew: bool | None | Unset = UNSET
    rotate_pages: bool | None | Unset = UNSET
    rotate_pages_threshold: float | None | Unset = UNSET
    max_image_pixels: float | None | Unset = UNSET
    color_conversion_strategy: BlankEnum | ColorConversionStrategyEnum | None | Unset = UNSET
    app_title: None | str | Unset = UNSET
    app_logo: None | str | Unset = UNSET
    barcodes_enabled: bool | None | Unset = UNSET
    barcode_enable_tiff_support: bool | None | Unset = UNSET
    barcode_string: None | str | Unset = UNSET
    barcode_retain_split_pages: bool | None | Unset = UNSET
    barcode_enable_asn: bool | None | Unset = UNSET
    barcode_asn_prefix: None | str | Unset = UNSET
    barcode_upscale: float | None | Unset = UNSET
    barcode_dpi: int | None | Unset = UNSET
    barcode_max_pages: int | None | Unset = UNSET
    barcode_enable_tag: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_args = self.user_args

        barcode_tag_mapping = self.barcode_tag_mapping

        output_type: None | str | Unset
        if isinstance(self.output_type, Unset):
            output_type = UNSET
        elif isinstance(self.output_type, OutputTypeEnum):
            output_type = self.output_type.value
        elif isinstance(self.output_type, BlankEnum):
            output_type = self.output_type.value
        else:
            output_type = self.output_type

        pages: int | None | Unset
        if isinstance(self.pages, Unset):
            pages = UNSET
        else:
            pages = self.pages

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, ModeEnum):
            mode = self.mode.value
        elif isinstance(self.mode, BlankEnum):
            mode = self.mode.value
        else:
            mode = self.mode

        skip_archive_file: None | str | Unset
        if isinstance(self.skip_archive_file, Unset):
            skip_archive_file = UNSET
        elif isinstance(self.skip_archive_file, SkipArchiveFileEnum):
            skip_archive_file = self.skip_archive_file.value
        elif isinstance(self.skip_archive_file, BlankEnum):
            skip_archive_file = self.skip_archive_file.value
        else:
            skip_archive_file = self.skip_archive_file

        image_dpi: int | None | Unset
        if isinstance(self.image_dpi, Unset):
            image_dpi = UNSET
        else:
            image_dpi = self.image_dpi

        unpaper_clean: None | str | Unset
        if isinstance(self.unpaper_clean, Unset):
            unpaper_clean = UNSET
        elif isinstance(self.unpaper_clean, UnpaperCleanEnum):
            unpaper_clean = self.unpaper_clean.value
        elif isinstance(self.unpaper_clean, BlankEnum):
            unpaper_clean = self.unpaper_clean.value
        else:
            unpaper_clean = self.unpaper_clean

        deskew: bool | None | Unset
        if isinstance(self.deskew, Unset):
            deskew = UNSET
        else:
            deskew = self.deskew

        rotate_pages: bool | None | Unset
        if isinstance(self.rotate_pages, Unset):
            rotate_pages = UNSET
        else:
            rotate_pages = self.rotate_pages

        rotate_pages_threshold: float | None | Unset
        if isinstance(self.rotate_pages_threshold, Unset):
            rotate_pages_threshold = UNSET
        else:
            rotate_pages_threshold = self.rotate_pages_threshold

        max_image_pixels: float | None | Unset
        if isinstance(self.max_image_pixels, Unset):
            max_image_pixels = UNSET
        else:
            max_image_pixels = self.max_image_pixels

        color_conversion_strategy: None | str | Unset
        if isinstance(self.color_conversion_strategy, Unset):
            color_conversion_strategy = UNSET
        elif isinstance(self.color_conversion_strategy, ColorConversionStrategyEnum):
            color_conversion_strategy = self.color_conversion_strategy.value
        elif isinstance(self.color_conversion_strategy, BlankEnum):
            color_conversion_strategy = self.color_conversion_strategy.value
        else:
            color_conversion_strategy = self.color_conversion_strategy

        app_title: None | str | Unset
        if isinstance(self.app_title, Unset):
            app_title = UNSET
        else:
            app_title = self.app_title

        app_logo: None | str | Unset
        if isinstance(self.app_logo, Unset):
            app_logo = UNSET
        else:
            app_logo = self.app_logo

        barcodes_enabled: bool | None | Unset
        if isinstance(self.barcodes_enabled, Unset):
            barcodes_enabled = UNSET
        else:
            barcodes_enabled = self.barcodes_enabled

        barcode_enable_tiff_support: bool | None | Unset
        if isinstance(self.barcode_enable_tiff_support, Unset):
            barcode_enable_tiff_support = UNSET
        else:
            barcode_enable_tiff_support = self.barcode_enable_tiff_support

        barcode_string: None | str | Unset
        if isinstance(self.barcode_string, Unset):
            barcode_string = UNSET
        else:
            barcode_string = self.barcode_string

        barcode_retain_split_pages: bool | None | Unset
        if isinstance(self.barcode_retain_split_pages, Unset):
            barcode_retain_split_pages = UNSET
        else:
            barcode_retain_split_pages = self.barcode_retain_split_pages

        barcode_enable_asn: bool | None | Unset
        if isinstance(self.barcode_enable_asn, Unset):
            barcode_enable_asn = UNSET
        else:
            barcode_enable_asn = self.barcode_enable_asn

        barcode_asn_prefix: None | str | Unset
        if isinstance(self.barcode_asn_prefix, Unset):
            barcode_asn_prefix = UNSET
        else:
            barcode_asn_prefix = self.barcode_asn_prefix

        barcode_upscale: float | None | Unset
        if isinstance(self.barcode_upscale, Unset):
            barcode_upscale = UNSET
        else:
            barcode_upscale = self.barcode_upscale

        barcode_dpi: int | None | Unset
        if isinstance(self.barcode_dpi, Unset):
            barcode_dpi = UNSET
        else:
            barcode_dpi = self.barcode_dpi

        barcode_max_pages: int | None | Unset
        if isinstance(self.barcode_max_pages, Unset):
            barcode_max_pages = UNSET
        else:
            barcode_max_pages = self.barcode_max_pages

        barcode_enable_tag: bool | None | Unset
        if isinstance(self.barcode_enable_tag, Unset):
            barcode_enable_tag = UNSET
        else:
            barcode_enable_tag = self.barcode_enable_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_args": user_args,
                "barcode_tag_mapping": barcode_tag_mapping,
            }
        )
        if output_type is not UNSET:
            field_dict["output_type"] = output_type
        if pages is not UNSET:
            field_dict["pages"] = pages
        if language is not UNSET:
            field_dict["language"] = language
        if mode is not UNSET:
            field_dict["mode"] = mode
        if skip_archive_file is not UNSET:
            field_dict["skip_archive_file"] = skip_archive_file
        if image_dpi is not UNSET:
            field_dict["image_dpi"] = image_dpi
        if unpaper_clean is not UNSET:
            field_dict["unpaper_clean"] = unpaper_clean
        if deskew is not UNSET:
            field_dict["deskew"] = deskew
        if rotate_pages is not UNSET:
            field_dict["rotate_pages"] = rotate_pages
        if rotate_pages_threshold is not UNSET:
            field_dict["rotate_pages_threshold"] = rotate_pages_threshold
        if max_image_pixels is not UNSET:
            field_dict["max_image_pixels"] = max_image_pixels
        if color_conversion_strategy is not UNSET:
            field_dict["color_conversion_strategy"] = color_conversion_strategy
        if app_title is not UNSET:
            field_dict["app_title"] = app_title
        if app_logo is not UNSET:
            field_dict["app_logo"] = app_logo
        if barcodes_enabled is not UNSET:
            field_dict["barcodes_enabled"] = barcodes_enabled
        if barcode_enable_tiff_support is not UNSET:
            field_dict["barcode_enable_tiff_support"] = barcode_enable_tiff_support
        if barcode_string is not UNSET:
            field_dict["barcode_string"] = barcode_string
        if barcode_retain_split_pages is not UNSET:
            field_dict["barcode_retain_split_pages"] = barcode_retain_split_pages
        if barcode_enable_asn is not UNSET:
            field_dict["barcode_enable_asn"] = barcode_enable_asn
        if barcode_asn_prefix is not UNSET:
            field_dict["barcode_asn_prefix"] = barcode_asn_prefix
        if barcode_upscale is not UNSET:
            field_dict["barcode_upscale"] = barcode_upscale
        if barcode_dpi is not UNSET:
            field_dict["barcode_dpi"] = barcode_dpi
        if barcode_max_pages is not UNSET:
            field_dict["barcode_max_pages"] = barcode_max_pages
        if barcode_enable_tag is not UNSET:
            field_dict["barcode_enable_tag"] = barcode_enable_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_args = d.pop("user_args")

        barcode_tag_mapping = d.pop("barcode_tag_mapping")

        def _parse_output_type(data: object) -> BlankEnum | None | OutputTypeEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                output_type_type_0 = OutputTypeEnum(data)

                return output_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                output_type_type_1 = BlankEnum(data)

                return output_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | OutputTypeEnum | Unset, data)

        output_type = _parse_output_type(d.pop("output_type", UNSET))

        def _parse_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pages = _parse_pages(d.pop("pages", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_mode(data: object) -> BlankEnum | ModeEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = ModeEnum(data)

                return mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = BlankEnum(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | ModeEnum | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_skip_archive_file(data: object) -> BlankEnum | None | SkipArchiveFileEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                skip_archive_file_type_0 = SkipArchiveFileEnum(data)

                return skip_archive_file_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                skip_archive_file_type_1 = BlankEnum(data)

                return skip_archive_file_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | SkipArchiveFileEnum | Unset, data)

        skip_archive_file = _parse_skip_archive_file(d.pop("skip_archive_file", UNSET))

        def _parse_image_dpi(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_dpi = _parse_image_dpi(d.pop("image_dpi", UNSET))

        def _parse_unpaper_clean(data: object) -> BlankEnum | None | UnpaperCleanEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unpaper_clean_type_0 = UnpaperCleanEnum(data)

                return unpaper_clean_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unpaper_clean_type_1 = BlankEnum(data)

                return unpaper_clean_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | UnpaperCleanEnum | Unset, data)

        unpaper_clean = _parse_unpaper_clean(d.pop("unpaper_clean", UNSET))

        def _parse_deskew(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deskew = _parse_deskew(d.pop("deskew", UNSET))

        def _parse_rotate_pages(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        rotate_pages = _parse_rotate_pages(d.pop("rotate_pages", UNSET))

        def _parse_rotate_pages_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotate_pages_threshold = _parse_rotate_pages_threshold(d.pop("rotate_pages_threshold", UNSET))

        def _parse_max_image_pixels(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_image_pixels = _parse_max_image_pixels(d.pop("max_image_pixels", UNSET))

        def _parse_color_conversion_strategy(data: object) -> BlankEnum | ColorConversionStrategyEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                color_conversion_strategy_type_0 = ColorConversionStrategyEnum(data)

                return color_conversion_strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                color_conversion_strategy_type_1 = BlankEnum(data)

                return color_conversion_strategy_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | ColorConversionStrategyEnum | None | Unset, data)

        color_conversion_strategy = _parse_color_conversion_strategy(d.pop("color_conversion_strategy", UNSET))

        def _parse_app_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_title = _parse_app_title(d.pop("app_title", UNSET))

        def _parse_app_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_logo = _parse_app_logo(d.pop("app_logo", UNSET))

        def _parse_barcodes_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        barcodes_enabled = _parse_barcodes_enabled(d.pop("barcodes_enabled", UNSET))

        def _parse_barcode_enable_tiff_support(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        barcode_enable_tiff_support = _parse_barcode_enable_tiff_support(d.pop("barcode_enable_tiff_support", UNSET))

        def _parse_barcode_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode_string = _parse_barcode_string(d.pop("barcode_string", UNSET))

        def _parse_barcode_retain_split_pages(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        barcode_retain_split_pages = _parse_barcode_retain_split_pages(d.pop("barcode_retain_split_pages", UNSET))

        def _parse_barcode_enable_asn(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        barcode_enable_asn = _parse_barcode_enable_asn(d.pop("barcode_enable_asn", UNSET))

        def _parse_barcode_asn_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode_asn_prefix = _parse_barcode_asn_prefix(d.pop("barcode_asn_prefix", UNSET))

        def _parse_barcode_upscale(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        barcode_upscale = _parse_barcode_upscale(d.pop("barcode_upscale", UNSET))

        def _parse_barcode_dpi(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        barcode_dpi = _parse_barcode_dpi(d.pop("barcode_dpi", UNSET))

        def _parse_barcode_max_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        barcode_max_pages = _parse_barcode_max_pages(d.pop("barcode_max_pages", UNSET))

        def _parse_barcode_enable_tag(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        barcode_enable_tag = _parse_barcode_enable_tag(d.pop("barcode_enable_tag", UNSET))

        application_configuration = cls(
            id=id,
            user_args=user_args,
            barcode_tag_mapping=barcode_tag_mapping,
            output_type=output_type,
            pages=pages,
            language=language,
            mode=mode,
            skip_archive_file=skip_archive_file,
            image_dpi=image_dpi,
            unpaper_clean=unpaper_clean,
            deskew=deskew,
            rotate_pages=rotate_pages,
            rotate_pages_threshold=rotate_pages_threshold,
            max_image_pixels=max_image_pixels,
            color_conversion_strategy=color_conversion_strategy,
            app_title=app_title,
            app_logo=app_logo,
            barcodes_enabled=barcodes_enabled,
            barcode_enable_tiff_support=barcode_enable_tiff_support,
            barcode_string=barcode_string,
            barcode_retain_split_pages=barcode_retain_split_pages,
            barcode_enable_asn=barcode_enable_asn,
            barcode_asn_prefix=barcode_asn_prefix,
            barcode_upscale=barcode_upscale,
            barcode_dpi=barcode_dpi,
            barcode_max_pages=barcode_max_pages,
            barcode_enable_tag=barcode_enable_tag,
        )

        application_configuration.additional_properties = d
        return application_configuration

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
