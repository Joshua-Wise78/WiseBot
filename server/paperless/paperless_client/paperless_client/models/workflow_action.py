from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_action_type_enum import WorkflowActionTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_action_email import WorkflowActionEmail
    from ..models.workflow_action_webhook import WorkflowActionWebhook


T = TypeVar("T", bound="WorkflowAction")


@_attrs_define
class WorkflowAction:
    """
    Attributes:
        id (int | None | Unset):
        type_ (WorkflowActionTypeEnum | Unset): * `1` - Assignment
            * `2` - Removal
            * `3` - Email
            * `4` - Webhook
        assign_title (None | str | Unset): Assign a document title, must  be a Jinja2 template, see documentation.
        assign_tags (list[int | None] | Unset):
        assign_correspondent (int | None | Unset):
        assign_document_type (int | None | Unset):
        assign_storage_path (int | None | Unset):
        assign_owner (int | None | Unset):
        assign_view_users (list[int] | Unset):
        assign_view_groups (list[int] | Unset):
        assign_change_users (list[int] | Unset):
        assign_change_groups (list[int] | Unset):
        assign_custom_fields (list[int] | Unset):
        assign_custom_fields_values (Any | Unset): Optional values to assign to the custom fields.
        remove_all_tags (bool | Unset):
        remove_tags (list[int] | Unset):
        remove_all_correspondents (bool | Unset):
        remove_correspondents (list[int] | Unset):
        remove_all_document_types (bool | Unset):
        remove_document_types (list[int] | Unset):
        remove_all_storage_paths (bool | Unset):
        remove_storage_paths (list[int] | Unset):
        remove_custom_fields (list[int] | Unset):
        remove_all_custom_fields (bool | Unset):
        remove_all_owners (bool | Unset):
        remove_owners (list[int] | Unset):
        remove_all_permissions (bool | Unset):
        remove_view_users (list[int] | Unset):
        remove_view_groups (list[int] | Unset):
        remove_change_users (list[int] | Unset):
        remove_change_groups (list[int] | Unset):
        email (None | Unset | WorkflowActionEmail):
        webhook (None | Unset | WorkflowActionWebhook):
    """

    id: int | None | Unset = UNSET
    type_: WorkflowActionTypeEnum | Unset = UNSET
    assign_title: None | str | Unset = UNSET
    assign_tags: list[int | None] | Unset = UNSET
    assign_correspondent: int | None | Unset = UNSET
    assign_document_type: int | None | Unset = UNSET
    assign_storage_path: int | None | Unset = UNSET
    assign_owner: int | None | Unset = UNSET
    assign_view_users: list[int] | Unset = UNSET
    assign_view_groups: list[int] | Unset = UNSET
    assign_change_users: list[int] | Unset = UNSET
    assign_change_groups: list[int] | Unset = UNSET
    assign_custom_fields: list[int] | Unset = UNSET
    assign_custom_fields_values: Any | Unset = UNSET
    remove_all_tags: bool | Unset = UNSET
    remove_tags: list[int] | Unset = UNSET
    remove_all_correspondents: bool | Unset = UNSET
    remove_correspondents: list[int] | Unset = UNSET
    remove_all_document_types: bool | Unset = UNSET
    remove_document_types: list[int] | Unset = UNSET
    remove_all_storage_paths: bool | Unset = UNSET
    remove_storage_paths: list[int] | Unset = UNSET
    remove_custom_fields: list[int] | Unset = UNSET
    remove_all_custom_fields: bool | Unset = UNSET
    remove_all_owners: bool | Unset = UNSET
    remove_owners: list[int] | Unset = UNSET
    remove_all_permissions: bool | Unset = UNSET
    remove_view_users: list[int] | Unset = UNSET
    remove_view_groups: list[int] | Unset = UNSET
    remove_change_users: list[int] | Unset = UNSET
    remove_change_groups: list[int] | Unset = UNSET
    email: None | Unset | WorkflowActionEmail = UNSET
    webhook: None | Unset | WorkflowActionWebhook = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_action_email import WorkflowActionEmail
        from ..models.workflow_action_webhook import WorkflowActionWebhook

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        assign_title: None | str | Unset
        if isinstance(self.assign_title, Unset):
            assign_title = UNSET
        else:
            assign_title = self.assign_title

        assign_tags: list[int | None] | Unset = UNSET
        if not isinstance(self.assign_tags, Unset):
            assign_tags = []
            for assign_tags_item_data in self.assign_tags:
                assign_tags_item: int | None
                assign_tags_item = assign_tags_item_data
                assign_tags.append(assign_tags_item)

        assign_correspondent: int | None | Unset
        if isinstance(self.assign_correspondent, Unset):
            assign_correspondent = UNSET
        else:
            assign_correspondent = self.assign_correspondent

        assign_document_type: int | None | Unset
        if isinstance(self.assign_document_type, Unset):
            assign_document_type = UNSET
        else:
            assign_document_type = self.assign_document_type

        assign_storage_path: int | None | Unset
        if isinstance(self.assign_storage_path, Unset):
            assign_storage_path = UNSET
        else:
            assign_storage_path = self.assign_storage_path

        assign_owner: int | None | Unset
        if isinstance(self.assign_owner, Unset):
            assign_owner = UNSET
        else:
            assign_owner = self.assign_owner

        assign_view_users: list[int] | Unset = UNSET
        if not isinstance(self.assign_view_users, Unset):
            assign_view_users = self.assign_view_users

        assign_view_groups: list[int] | Unset = UNSET
        if not isinstance(self.assign_view_groups, Unset):
            assign_view_groups = self.assign_view_groups

        assign_change_users: list[int] | Unset = UNSET
        if not isinstance(self.assign_change_users, Unset):
            assign_change_users = self.assign_change_users

        assign_change_groups: list[int] | Unset = UNSET
        if not isinstance(self.assign_change_groups, Unset):
            assign_change_groups = self.assign_change_groups

        assign_custom_fields: list[int] | Unset = UNSET
        if not isinstance(self.assign_custom_fields, Unset):
            assign_custom_fields = self.assign_custom_fields

        assign_custom_fields_values = self.assign_custom_fields_values

        remove_all_tags = self.remove_all_tags

        remove_tags: list[int] | Unset = UNSET
        if not isinstance(self.remove_tags, Unset):
            remove_tags = self.remove_tags

        remove_all_correspondents = self.remove_all_correspondents

        remove_correspondents: list[int] | Unset = UNSET
        if not isinstance(self.remove_correspondents, Unset):
            remove_correspondents = self.remove_correspondents

        remove_all_document_types = self.remove_all_document_types

        remove_document_types: list[int] | Unset = UNSET
        if not isinstance(self.remove_document_types, Unset):
            remove_document_types = self.remove_document_types

        remove_all_storage_paths = self.remove_all_storage_paths

        remove_storage_paths: list[int] | Unset = UNSET
        if not isinstance(self.remove_storage_paths, Unset):
            remove_storage_paths = self.remove_storage_paths

        remove_custom_fields: list[int] | Unset = UNSET
        if not isinstance(self.remove_custom_fields, Unset):
            remove_custom_fields = self.remove_custom_fields

        remove_all_custom_fields = self.remove_all_custom_fields

        remove_all_owners = self.remove_all_owners

        remove_owners: list[int] | Unset = UNSET
        if not isinstance(self.remove_owners, Unset):
            remove_owners = self.remove_owners

        remove_all_permissions = self.remove_all_permissions

        remove_view_users: list[int] | Unset = UNSET
        if not isinstance(self.remove_view_users, Unset):
            remove_view_users = self.remove_view_users

        remove_view_groups: list[int] | Unset = UNSET
        if not isinstance(self.remove_view_groups, Unset):
            remove_view_groups = self.remove_view_groups

        remove_change_users: list[int] | Unset = UNSET
        if not isinstance(self.remove_change_users, Unset):
            remove_change_users = self.remove_change_users

        remove_change_groups: list[int] | Unset = UNSET
        if not isinstance(self.remove_change_groups, Unset):
            remove_change_groups = self.remove_change_groups

        email: dict[str, Any] | None | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        elif isinstance(self.email, WorkflowActionEmail):
            email = self.email.to_dict()
        else:
            email = self.email

        webhook: dict[str, Any] | None | Unset
        if isinstance(self.webhook, Unset):
            webhook = UNSET
        elif isinstance(self.webhook, WorkflowActionWebhook):
            webhook = self.webhook.to_dict()
        else:
            webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if assign_title is not UNSET:
            field_dict["assign_title"] = assign_title
        if assign_tags is not UNSET:
            field_dict["assign_tags"] = assign_tags
        if assign_correspondent is not UNSET:
            field_dict["assign_correspondent"] = assign_correspondent
        if assign_document_type is not UNSET:
            field_dict["assign_document_type"] = assign_document_type
        if assign_storage_path is not UNSET:
            field_dict["assign_storage_path"] = assign_storage_path
        if assign_owner is not UNSET:
            field_dict["assign_owner"] = assign_owner
        if assign_view_users is not UNSET:
            field_dict["assign_view_users"] = assign_view_users
        if assign_view_groups is not UNSET:
            field_dict["assign_view_groups"] = assign_view_groups
        if assign_change_users is not UNSET:
            field_dict["assign_change_users"] = assign_change_users
        if assign_change_groups is not UNSET:
            field_dict["assign_change_groups"] = assign_change_groups
        if assign_custom_fields is not UNSET:
            field_dict["assign_custom_fields"] = assign_custom_fields
        if assign_custom_fields_values is not UNSET:
            field_dict["assign_custom_fields_values"] = assign_custom_fields_values
        if remove_all_tags is not UNSET:
            field_dict["remove_all_tags"] = remove_all_tags
        if remove_tags is not UNSET:
            field_dict["remove_tags"] = remove_tags
        if remove_all_correspondents is not UNSET:
            field_dict["remove_all_correspondents"] = remove_all_correspondents
        if remove_correspondents is not UNSET:
            field_dict["remove_correspondents"] = remove_correspondents
        if remove_all_document_types is not UNSET:
            field_dict["remove_all_document_types"] = remove_all_document_types
        if remove_document_types is not UNSET:
            field_dict["remove_document_types"] = remove_document_types
        if remove_all_storage_paths is not UNSET:
            field_dict["remove_all_storage_paths"] = remove_all_storage_paths
        if remove_storage_paths is not UNSET:
            field_dict["remove_storage_paths"] = remove_storage_paths
        if remove_custom_fields is not UNSET:
            field_dict["remove_custom_fields"] = remove_custom_fields
        if remove_all_custom_fields is not UNSET:
            field_dict["remove_all_custom_fields"] = remove_all_custom_fields
        if remove_all_owners is not UNSET:
            field_dict["remove_all_owners"] = remove_all_owners
        if remove_owners is not UNSET:
            field_dict["remove_owners"] = remove_owners
        if remove_all_permissions is not UNSET:
            field_dict["remove_all_permissions"] = remove_all_permissions
        if remove_view_users is not UNSET:
            field_dict["remove_view_users"] = remove_view_users
        if remove_view_groups is not UNSET:
            field_dict["remove_view_groups"] = remove_view_groups
        if remove_change_users is not UNSET:
            field_dict["remove_change_users"] = remove_change_users
        if remove_change_groups is not UNSET:
            field_dict["remove_change_groups"] = remove_change_groups
        if email is not UNSET:
            field_dict["email"] = email
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_action_email import WorkflowActionEmail
        from ..models.workflow_action_webhook import WorkflowActionWebhook

        d = dict(src_dict)

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: WorkflowActionTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WorkflowActionTypeEnum(_type_)

        def _parse_assign_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_title = _parse_assign_title(d.pop("assign_title", UNSET))

        _assign_tags = d.pop("assign_tags", UNSET)
        assign_tags: list[int | None] | Unset = UNSET
        if _assign_tags is not UNSET:
            assign_tags = []
            for assign_tags_item_data in _assign_tags:

                def _parse_assign_tags_item(data: object) -> int | None:
                    if data is None:
                        return data
                    return cast(int | None, data)

                assign_tags_item = _parse_assign_tags_item(assign_tags_item_data)

                assign_tags.append(assign_tags_item)

        def _parse_assign_correspondent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assign_correspondent = _parse_assign_correspondent(d.pop("assign_correspondent", UNSET))

        def _parse_assign_document_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assign_document_type = _parse_assign_document_type(d.pop("assign_document_type", UNSET))

        def _parse_assign_storage_path(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assign_storage_path = _parse_assign_storage_path(d.pop("assign_storage_path", UNSET))

        def _parse_assign_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assign_owner = _parse_assign_owner(d.pop("assign_owner", UNSET))

        assign_view_users = cast(list[int], d.pop("assign_view_users", UNSET))

        assign_view_groups = cast(list[int], d.pop("assign_view_groups", UNSET))

        assign_change_users = cast(list[int], d.pop("assign_change_users", UNSET))

        assign_change_groups = cast(list[int], d.pop("assign_change_groups", UNSET))

        assign_custom_fields = cast(list[int], d.pop("assign_custom_fields", UNSET))

        assign_custom_fields_values = d.pop("assign_custom_fields_values", UNSET)

        remove_all_tags = d.pop("remove_all_tags", UNSET)

        remove_tags = cast(list[int], d.pop("remove_tags", UNSET))

        remove_all_correspondents = d.pop("remove_all_correspondents", UNSET)

        remove_correspondents = cast(list[int], d.pop("remove_correspondents", UNSET))

        remove_all_document_types = d.pop("remove_all_document_types", UNSET)

        remove_document_types = cast(list[int], d.pop("remove_document_types", UNSET))

        remove_all_storage_paths = d.pop("remove_all_storage_paths", UNSET)

        remove_storage_paths = cast(list[int], d.pop("remove_storage_paths", UNSET))

        remove_custom_fields = cast(list[int], d.pop("remove_custom_fields", UNSET))

        remove_all_custom_fields = d.pop("remove_all_custom_fields", UNSET)

        remove_all_owners = d.pop("remove_all_owners", UNSET)

        remove_owners = cast(list[int], d.pop("remove_owners", UNSET))

        remove_all_permissions = d.pop("remove_all_permissions", UNSET)

        remove_view_users = cast(list[int], d.pop("remove_view_users", UNSET))

        remove_view_groups = cast(list[int], d.pop("remove_view_groups", UNSET))

        remove_change_users = cast(list[int], d.pop("remove_change_users", UNSET))

        remove_change_groups = cast(list[int], d.pop("remove_change_groups", UNSET))

        def _parse_email(data: object) -> None | Unset | WorkflowActionEmail:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                email_type_1 = WorkflowActionEmail.from_dict(data)

                return email_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowActionEmail, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_webhook(data: object) -> None | Unset | WorkflowActionWebhook:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                webhook_type_1 = WorkflowActionWebhook.from_dict(data)

                return webhook_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowActionWebhook, data)

        webhook = _parse_webhook(d.pop("webhook", UNSET))

        workflow_action = cls(
            id=id,
            type_=type_,
            assign_title=assign_title,
            assign_tags=assign_tags,
            assign_correspondent=assign_correspondent,
            assign_document_type=assign_document_type,
            assign_storage_path=assign_storage_path,
            assign_owner=assign_owner,
            assign_view_users=assign_view_users,
            assign_view_groups=assign_view_groups,
            assign_change_users=assign_change_users,
            assign_change_groups=assign_change_groups,
            assign_custom_fields=assign_custom_fields,
            assign_custom_fields_values=assign_custom_fields_values,
            remove_all_tags=remove_all_tags,
            remove_tags=remove_tags,
            remove_all_correspondents=remove_all_correspondents,
            remove_correspondents=remove_correspondents,
            remove_all_document_types=remove_all_document_types,
            remove_document_types=remove_document_types,
            remove_all_storage_paths=remove_all_storage_paths,
            remove_storage_paths=remove_storage_paths,
            remove_custom_fields=remove_custom_fields,
            remove_all_custom_fields=remove_all_custom_fields,
            remove_all_owners=remove_all_owners,
            remove_owners=remove_owners,
            remove_all_permissions=remove_all_permissions,
            remove_view_users=remove_view_users,
            remove_view_groups=remove_view_groups,
            remove_change_users=remove_change_users,
            remove_change_groups=remove_change_groups,
            email=email,
            webhook=webhook,
        )

        workflow_action.additional_properties = d
        return workflow_action

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
