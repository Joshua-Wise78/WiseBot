from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assign_correspondent_from_enum import AssignCorrespondentFromEnum
from ..models.assign_title_from_enum import AssignTitleFromEnum
from ..models.attachment_type_enum import AttachmentTypeEnum
from ..models.consumption_scope_enum import ConsumptionScopeEnum
from ..models.mail_rule_action_enum import MailRuleActionEnum
from ..models.pdf_layout_enum import PdfLayoutEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MailRule")


@_attrs_define
class MailRule:
    """
    Attributes:
        id (int):
        name (str):
        account (int):
        user_can_change (bool):
        enabled (bool | Unset):
        folder (str | Unset): Subfolders must be separated by a delimiter, often a dot ('.') or slash ('/'), but it
            varies by mail server.
        filter_from (None | str | Unset):
        filter_to (None | str | Unset):
        filter_subject (None | str | Unset):
        filter_body (None | str | Unset):
        filter_attachment_filename_include (None | str | Unset): Only consume documents which entirely match this
            filename if specified. Wildcards such as *.pdf or *invoice* are allowed. Case insensitive.
        filter_attachment_filename_exclude (None | str | Unset): Do not consume documents which entirely match this
            filename if specified. Wildcards such as *.pdf or *invoice* are allowed. Case insensitive.
        maximum_age (int | Unset): Specified in days.
        action (MailRuleActionEnum | Unset): * `1` - Delete
            * `2` - Move to specified folder
            * `3` - Mark as read, don't process read mails
            * `4` - Flag the mail, don't process flagged mails
            * `5` - Tag the mail with specified tag, don't process tagged mails
        action_parameter (None | str | Unset):  Default: ''.
        assign_title_from (AssignTitleFromEnum | Unset): * `1` - Use subject as title
            * `2` - Use attachment filename as title
            * `3` - Do not assign title from rule
        assign_tags (list[int | None] | Unset):
        assign_correspondent_from (AssignCorrespondentFromEnum | Unset): * `1` - Do not assign a correspondent
            * `2` - Use mail address
            * `3` - Use name (or mail address if not available)
            * `4` - Use correspondent selected below
        assign_correspondent (int | None | Unset):
        assign_document_type (int | None | Unset):
        assign_owner_from_rule (bool | Unset):
        order (int | Unset):
        attachment_type (AttachmentTypeEnum | Unset): * `1` - Only process attachments.
            * `2` - Process all files, including 'inline' attachments.
        consumption_scope (ConsumptionScopeEnum | Unset): * `1` - Only process attachments.
            * `2` - Process full Mail (with embedded attachments in file) as .eml
            * `3` - Process full Mail (with embedded attachments in file) as .eml + process attachments as separate
            documents
        pdf_layout (PdfLayoutEnum | Unset): * `0` - System default
            * `1` - Text, then HTML
            * `2` - HTML, then text
            * `3` - HTML only
            * `4` - Text only
        owner (int | None | Unset):
    """

    id: int
    name: str
    account: int
    user_can_change: bool
    enabled: bool | Unset = UNSET
    folder: str | Unset = UNSET
    filter_from: None | str | Unset = UNSET
    filter_to: None | str | Unset = UNSET
    filter_subject: None | str | Unset = UNSET
    filter_body: None | str | Unset = UNSET
    filter_attachment_filename_include: None | str | Unset = UNSET
    filter_attachment_filename_exclude: None | str | Unset = UNSET
    maximum_age: int | Unset = UNSET
    action: MailRuleActionEnum | Unset = UNSET
    action_parameter: None | str | Unset = ""
    assign_title_from: AssignTitleFromEnum | Unset = UNSET
    assign_tags: list[int | None] | Unset = UNSET
    assign_correspondent_from: AssignCorrespondentFromEnum | Unset = UNSET
    assign_correspondent: int | None | Unset = UNSET
    assign_document_type: int | None | Unset = UNSET
    assign_owner_from_rule: bool | Unset = UNSET
    order: int | Unset = UNSET
    attachment_type: AttachmentTypeEnum | Unset = UNSET
    consumption_scope: ConsumptionScopeEnum | Unset = UNSET
    pdf_layout: PdfLayoutEnum | Unset = UNSET
    owner: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        account = self.account

        user_can_change = self.user_can_change

        enabled = self.enabled

        folder = self.folder

        filter_from: None | str | Unset
        if isinstance(self.filter_from, Unset):
            filter_from = UNSET
        else:
            filter_from = self.filter_from

        filter_to: None | str | Unset
        if isinstance(self.filter_to, Unset):
            filter_to = UNSET
        else:
            filter_to = self.filter_to

        filter_subject: None | str | Unset
        if isinstance(self.filter_subject, Unset):
            filter_subject = UNSET
        else:
            filter_subject = self.filter_subject

        filter_body: None | str | Unset
        if isinstance(self.filter_body, Unset):
            filter_body = UNSET
        else:
            filter_body = self.filter_body

        filter_attachment_filename_include: None | str | Unset
        if isinstance(self.filter_attachment_filename_include, Unset):
            filter_attachment_filename_include = UNSET
        else:
            filter_attachment_filename_include = self.filter_attachment_filename_include

        filter_attachment_filename_exclude: None | str | Unset
        if isinstance(self.filter_attachment_filename_exclude, Unset):
            filter_attachment_filename_exclude = UNSET
        else:
            filter_attachment_filename_exclude = self.filter_attachment_filename_exclude

        maximum_age = self.maximum_age

        action: int | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        action_parameter: None | str | Unset
        if isinstance(self.action_parameter, Unset):
            action_parameter = UNSET
        else:
            action_parameter = self.action_parameter

        assign_title_from: int | Unset = UNSET
        if not isinstance(self.assign_title_from, Unset):
            assign_title_from = self.assign_title_from.value

        assign_tags: list[int | None] | Unset = UNSET
        if not isinstance(self.assign_tags, Unset):
            assign_tags = []
            for assign_tags_item_data in self.assign_tags:
                assign_tags_item: int | None
                assign_tags_item = assign_tags_item_data
                assign_tags.append(assign_tags_item)

        assign_correspondent_from: int | Unset = UNSET
        if not isinstance(self.assign_correspondent_from, Unset):
            assign_correspondent_from = self.assign_correspondent_from.value

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

        assign_owner_from_rule = self.assign_owner_from_rule

        order = self.order

        attachment_type: int | Unset = UNSET
        if not isinstance(self.attachment_type, Unset):
            attachment_type = self.attachment_type.value

        consumption_scope: int | Unset = UNSET
        if not isinstance(self.consumption_scope, Unset):
            consumption_scope = self.consumption_scope.value

        pdf_layout: int | Unset = UNSET
        if not isinstance(self.pdf_layout, Unset):
            pdf_layout = self.pdf_layout.value

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
                "name": name,
                "account": account,
                "user_can_change": user_can_change,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if folder is not UNSET:
            field_dict["folder"] = folder
        if filter_from is not UNSET:
            field_dict["filter_from"] = filter_from
        if filter_to is not UNSET:
            field_dict["filter_to"] = filter_to
        if filter_subject is not UNSET:
            field_dict["filter_subject"] = filter_subject
        if filter_body is not UNSET:
            field_dict["filter_body"] = filter_body
        if filter_attachment_filename_include is not UNSET:
            field_dict["filter_attachment_filename_include"] = filter_attachment_filename_include
        if filter_attachment_filename_exclude is not UNSET:
            field_dict["filter_attachment_filename_exclude"] = filter_attachment_filename_exclude
        if maximum_age is not UNSET:
            field_dict["maximum_age"] = maximum_age
        if action is not UNSET:
            field_dict["action"] = action
        if action_parameter is not UNSET:
            field_dict["action_parameter"] = action_parameter
        if assign_title_from is not UNSET:
            field_dict["assign_title_from"] = assign_title_from
        if assign_tags is not UNSET:
            field_dict["assign_tags"] = assign_tags
        if assign_correspondent_from is not UNSET:
            field_dict["assign_correspondent_from"] = assign_correspondent_from
        if assign_correspondent is not UNSET:
            field_dict["assign_correspondent"] = assign_correspondent
        if assign_document_type is not UNSET:
            field_dict["assign_document_type"] = assign_document_type
        if assign_owner_from_rule is not UNSET:
            field_dict["assign_owner_from_rule"] = assign_owner_from_rule
        if order is not UNSET:
            field_dict["order"] = order
        if attachment_type is not UNSET:
            field_dict["attachment_type"] = attachment_type
        if consumption_scope is not UNSET:
            field_dict["consumption_scope"] = consumption_scope
        if pdf_layout is not UNSET:
            field_dict["pdf_layout"] = pdf_layout
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        account = d.pop("account")

        user_can_change = d.pop("user_can_change")

        enabled = d.pop("enabled", UNSET)

        folder = d.pop("folder", UNSET)

        def _parse_filter_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_from = _parse_filter_from(d.pop("filter_from", UNSET))

        def _parse_filter_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_to = _parse_filter_to(d.pop("filter_to", UNSET))

        def _parse_filter_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_subject = _parse_filter_subject(d.pop("filter_subject", UNSET))

        def _parse_filter_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_body = _parse_filter_body(d.pop("filter_body", UNSET))

        def _parse_filter_attachment_filename_include(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_attachment_filename_include = _parse_filter_attachment_filename_include(
            d.pop("filter_attachment_filename_include", UNSET)
        )

        def _parse_filter_attachment_filename_exclude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_attachment_filename_exclude = _parse_filter_attachment_filename_exclude(
            d.pop("filter_attachment_filename_exclude", UNSET)
        )

        maximum_age = d.pop("maximum_age", UNSET)

        _action = d.pop("action", UNSET)
        action: MailRuleActionEnum | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = MailRuleActionEnum(_action)

        def _parse_action_parameter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_parameter = _parse_action_parameter(d.pop("action_parameter", UNSET))

        _assign_title_from = d.pop("assign_title_from", UNSET)
        assign_title_from: AssignTitleFromEnum | Unset
        if isinstance(_assign_title_from, Unset):
            assign_title_from = UNSET
        else:
            assign_title_from = AssignTitleFromEnum(_assign_title_from)

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

        _assign_correspondent_from = d.pop("assign_correspondent_from", UNSET)
        assign_correspondent_from: AssignCorrespondentFromEnum | Unset
        if isinstance(_assign_correspondent_from, Unset):
            assign_correspondent_from = UNSET
        else:
            assign_correspondent_from = AssignCorrespondentFromEnum(_assign_correspondent_from)

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

        assign_owner_from_rule = d.pop("assign_owner_from_rule", UNSET)

        order = d.pop("order", UNSET)

        _attachment_type = d.pop("attachment_type", UNSET)
        attachment_type: AttachmentTypeEnum | Unset
        if isinstance(_attachment_type, Unset):
            attachment_type = UNSET
        else:
            attachment_type = AttachmentTypeEnum(_attachment_type)

        _consumption_scope = d.pop("consumption_scope", UNSET)
        consumption_scope: ConsumptionScopeEnum | Unset
        if isinstance(_consumption_scope, Unset):
            consumption_scope = UNSET
        else:
            consumption_scope = ConsumptionScopeEnum(_consumption_scope)

        _pdf_layout = d.pop("pdf_layout", UNSET)
        pdf_layout: PdfLayoutEnum | Unset
        if isinstance(_pdf_layout, Unset):
            pdf_layout = UNSET
        else:
            pdf_layout = PdfLayoutEnum(_pdf_layout)

        def _parse_owner(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        mail_rule = cls(
            id=id,
            name=name,
            account=account,
            user_can_change=user_can_change,
            enabled=enabled,
            folder=folder,
            filter_from=filter_from,
            filter_to=filter_to,
            filter_subject=filter_subject,
            filter_body=filter_body,
            filter_attachment_filename_include=filter_attachment_filename_include,
            filter_attachment_filename_exclude=filter_attachment_filename_exclude,
            maximum_age=maximum_age,
            action=action,
            action_parameter=action_parameter,
            assign_title_from=assign_title_from,
            assign_tags=assign_tags,
            assign_correspondent_from=assign_correspondent_from,
            assign_correspondent=assign_correspondent,
            assign_document_type=assign_document_type,
            assign_owner_from_rule=assign_owner_from_rule,
            order=order,
            attachment_type=attachment_type,
            consumption_scope=consumption_scope,
            pdf_layout=pdf_layout,
            owner=owner,
        )

        mail_rule.additional_properties = d
        return mail_rule

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
