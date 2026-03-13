from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_settings_view_request_settings_type_0 import UiSettingsViewRequestSettingsType0


T = TypeVar("T", bound="UiSettingsViewRequest")


@_attrs_define
class UiSettingsViewRequest:
    """
    Attributes:
        settings (None | UiSettingsViewRequestSettingsType0 | Unset):
    """

    settings: None | UiSettingsViewRequestSettingsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ui_settings_view_request_settings_type_0 import UiSettingsViewRequestSettingsType0

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, UiSettingsViewRequestSettingsType0):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.ui_settings_view_request_settings_type_0 import UiSettingsViewRequestSettingsType0

        files: types.RequestFiles = []

        if not isinstance(self.settings, Unset):
            if isinstance(self.settings, UiSettingsViewRequestSettingsType0):
                files.append(("settings", (None, json.dumps(self.settings.to_dict()).encode(), "application/json")))
            else:
                files.append(("settings", (None, str(self.settings).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_settings_view_request_settings_type_0 import UiSettingsViewRequestSettingsType0

        d = dict(src_dict)

        def _parse_settings(data: object) -> None | UiSettingsViewRequestSettingsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = UiSettingsViewRequestSettingsType0.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UiSettingsViewRequestSettingsType0 | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        ui_settings_view_request = cls(
            settings=settings,
        )

        ui_settings_view_request.additional_properties = d
        return ui_settings_view_request

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
