from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.correspondent import Correspondent
    from ..models.custom_field import CustomField
    from ..models.document import Document
    from ..models.document_type import DocumentType
    from ..models.group import Group
    from ..models.mail_account import MailAccount
    from ..models.mail_rule import MailRule
    from ..models.saved_view import SavedView
    from ..models.storage_path import StoragePath
    from ..models.tag import Tag
    from ..models.user import User
    from ..models.workflow import Workflow


T = TypeVar("T", bound="SearchResult")


@_attrs_define
class SearchResult:
    """
    Attributes:
        total (int):
        documents (list[Document]):
        saved_views (list[SavedView]):
        tags (list[Tag]):
        correspondents (list[Correspondent]):
        document_types (list[DocumentType]):
        storage_paths (list[StoragePath]):
        users (list[User]):
        groups (list[Group]):
        mail_rules (list[MailRule]):
        mail_accounts (list[MailAccount]):
        workflows (list[Workflow]):
        custom_fields (list[CustomField]):
    """

    total: int
    documents: list[Document]
    saved_views: list[SavedView]
    tags: list[Tag]
    correspondents: list[Correspondent]
    document_types: list[DocumentType]
    storage_paths: list[StoragePath]
    users: list[User]
    groups: list[Group]
    mail_rules: list[MailRule]
    mail_accounts: list[MailAccount]
    workflows: list[Workflow]
    custom_fields: list[CustomField]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        saved_views = []
        for saved_views_item_data in self.saved_views:
            saved_views_item = saved_views_item_data.to_dict()
            saved_views.append(saved_views_item)

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        correspondents = []
        for correspondents_item_data in self.correspondents:
            correspondents_item = correspondents_item_data.to_dict()
            correspondents.append(correspondents_item)

        document_types = []
        for document_types_item_data in self.document_types:
            document_types_item = document_types_item_data.to_dict()
            document_types.append(document_types_item)

        storage_paths = []
        for storage_paths_item_data in self.storage_paths:
            storage_paths_item = storage_paths_item_data.to_dict()
            storage_paths.append(storage_paths_item)

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        mail_rules = []
        for mail_rules_item_data in self.mail_rules:
            mail_rules_item = mail_rules_item_data.to_dict()
            mail_rules.append(mail_rules_item)

        mail_accounts = []
        for mail_accounts_item_data in self.mail_accounts:
            mail_accounts_item = mail_accounts_item_data.to_dict()
            mail_accounts.append(mail_accounts_item)

        workflows = []
        for workflows_item_data in self.workflows:
            workflows_item = workflows_item_data.to_dict()
            workflows.append(workflows_item)

        custom_fields = []
        for custom_fields_item_data in self.custom_fields:
            custom_fields_item = custom_fields_item_data.to_dict()
            custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "documents": documents,
                "saved_views": saved_views,
                "tags": tags,
                "correspondents": correspondents,
                "document_types": document_types,
                "storage_paths": storage_paths,
                "users": users,
                "groups": groups,
                "mail_rules": mail_rules,
                "mail_accounts": mail_accounts,
                "workflows": workflows,
                "custom_fields": custom_fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.correspondent import Correspondent
        from ..models.custom_field import CustomField
        from ..models.document import Document
        from ..models.document_type import DocumentType
        from ..models.group import Group
        from ..models.mail_account import MailAccount
        from ..models.mail_rule import MailRule
        from ..models.saved_view import SavedView
        from ..models.storage_path import StoragePath
        from ..models.tag import Tag
        from ..models.user import User
        from ..models.workflow import Workflow

        d = dict(src_dict)
        total = d.pop("total")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        saved_views = []
        _saved_views = d.pop("saved_views")
        for saved_views_item_data in _saved_views:
            saved_views_item = SavedView.from_dict(saved_views_item_data)

            saved_views.append(saved_views_item)

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        correspondents = []
        _correspondents = d.pop("correspondents")
        for correspondents_item_data in _correspondents:
            correspondents_item = Correspondent.from_dict(correspondents_item_data)

            correspondents.append(correspondents_item)

        document_types = []
        _document_types = d.pop("document_types")
        for document_types_item_data in _document_types:
            document_types_item = DocumentType.from_dict(document_types_item_data)

            document_types.append(document_types_item)

        storage_paths = []
        _storage_paths = d.pop("storage_paths")
        for storage_paths_item_data in _storage_paths:
            storage_paths_item = StoragePath.from_dict(storage_paths_item_data)

            storage_paths.append(storage_paths_item)

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = Group.from_dict(groups_item_data)

            groups.append(groups_item)

        mail_rules = []
        _mail_rules = d.pop("mail_rules")
        for mail_rules_item_data in _mail_rules:
            mail_rules_item = MailRule.from_dict(mail_rules_item_data)

            mail_rules.append(mail_rules_item)

        mail_accounts = []
        _mail_accounts = d.pop("mail_accounts")
        for mail_accounts_item_data in _mail_accounts:
            mail_accounts_item = MailAccount.from_dict(mail_accounts_item_data)

            mail_accounts.append(mail_accounts_item)

        workflows = []
        _workflows = d.pop("workflows")
        for workflows_item_data in _workflows:
            workflows_item = Workflow.from_dict(workflows_item_data)

            workflows.append(workflows_item)

        custom_fields = []
        _custom_fields = d.pop("custom_fields")
        for custom_fields_item_data in _custom_fields:
            custom_fields_item = CustomField.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        search_result = cls(
            total=total,
            documents=documents,
            saved_views=saved_views,
            tags=tags,
            correspondents=correspondents,
            document_types=document_types,
            storage_paths=storage_paths,
            users=users,
            groups=groups,
            mail_rules=mail_rules,
            mail_accounts=mail_accounts,
            workflows=workflows,
            custom_fields=custom_fields,
        )

        search_result.additional_properties = d
        return search_result

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
