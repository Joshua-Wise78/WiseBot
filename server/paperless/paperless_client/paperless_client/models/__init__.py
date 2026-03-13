"""Contains all the data models used in inputs/outputs"""

from .account_type_enum import AccountTypeEnum
from .acknowledge_tasks import AcknowledgeTasks
from .acknowledge_tasks_body import AcknowledgeTasksBody
from .actor import Actor
from .application_configuration import ApplicationConfiguration
from .application_configuration_request import ApplicationConfigurationRequest
from .assign_correspondent_from_enum import AssignCorrespondentFromEnum
from .assign_title_from_enum import AssignTitleFromEnum
from .attachment_type_enum import AttachmentTypeEnum
from .basic_user import BasicUser
from .basic_user_request import BasicUserRequest
from .blank_enum import BlankEnum
from .bulk_download import BulkDownload
from .bulk_download_request import BulkDownloadRequest
from .bulk_edit_documents_result import BulkEditDocumentsResult
from .bulk_edit_objects_request import BulkEditObjectsRequest
from .bulk_edit_objects_request_set_permissions import BulkEditObjectsRequestSetPermissions
from .bulk_edit_request import BulkEditRequest
from .bulk_edit_request_parameters import BulkEditRequestParameters
from .bulk_edit_result import BulkEditResult
from .classifier import Classifier
from .color_conversion_strategy_enum import ColorConversionStrategyEnum
from .compression_enum import CompressionEnum
from .consumption_scope_enum import ConsumptionScopeEnum
from .content_enum import ContentEnum
from .correspondent import Correspondent
from .correspondent_counts import CorrespondentCounts
from .correspondent_permissions import CorrespondentPermissions
from .correspondent_permissions_change import CorrespondentPermissionsChange
from .correspondent_permissions_view import CorrespondentPermissionsView
from .correspondent_request import CorrespondentRequest
from .correspondent_request_set_permissions import CorrespondentRequestSetPermissions
from .correspondent_request_set_permissions_change import CorrespondentRequestSetPermissionsChange
from .correspondent_request_set_permissions_view import CorrespondentRequestSetPermissionsView
from .custom_field import CustomField
from .custom_field_counts import CustomFieldCounts
from .custom_field_instance import CustomFieldInstance
from .custom_field_instance_request import CustomFieldInstanceRequest
from .custom_field_instance_request_value_type_3 import CustomFieldInstanceRequestValueType3
from .custom_field_instance_value_type_3 import CustomFieldInstanceValueType3
from .custom_field_request import CustomFieldRequest
from .data_type_enum import DataTypeEnum
from .database import Database
from .display_mode_enum import DisplayModeEnum
from .document import Document
from .document_list_request import DocumentListRequest
from .document_permissions import DocumentPermissions
from .document_permissions_change import DocumentPermissionsChange
from .document_permissions_view import DocumentPermissionsView
from .document_request import DocumentRequest
from .document_request_set_permissions import DocumentRequestSetPermissions
from .document_request_set_permissions_change import DocumentRequestSetPermissionsChange
from .document_request_set_permissions_view import DocumentRequestSetPermissionsView
from .document_share_links_response_200_item import DocumentShareLinksResponse200Item
from .document_type import DocumentType
from .document_type_counts import DocumentTypeCounts
from .document_type_permissions import DocumentTypePermissions
from .document_type_permissions_change import DocumentTypePermissionsChange
from .document_type_permissions_view import DocumentTypePermissionsView
from .document_type_request import DocumentTypeRequest
from .document_type_request_set_permissions import DocumentTypeRequestSetPermissions
from .document_type_request_set_permissions_change import DocumentTypeRequestSetPermissionsChange
from .document_type_request_set_permissions_view import DocumentTypeRequestSetPermissionsView
from .email_document_request_request import EmailDocumentRequestRequest
from .email_document_response import EmailDocumentResponse
from .email_documents_response import EmailDocumentsResponse
from .email_request import EmailRequest
from .file_version_enum import FileVersionEnum
from .group import Group
from .group_request import GroupRequest
from .imap_security_enum import ImapSecurityEnum
from .index import Index
from .log_entry import LogEntry
from .log_entry_changes import LogEntryChanges
from .mail_account import MailAccount
from .mail_account_process_response import MailAccountProcessResponse
from .mail_account_request import MailAccountRequest
from .mail_account_request_set_permissions import MailAccountRequestSetPermissions
from .mail_account_request_set_permissions_change import MailAccountRequestSetPermissionsChange
from .mail_account_request_set_permissions_view import MailAccountRequestSetPermissionsView
from .mail_account_test_response import MailAccountTestResponse
from .mail_rule import MailRule
from .mail_rule_action_enum import MailRuleActionEnum
from .mail_rule_request import MailRuleRequest
from .mail_rule_request_set_permissions import MailRuleRequestSetPermissions
from .mail_rule_request_set_permissions_change import MailRuleRequestSetPermissionsChange
from .mail_rule_request_set_permissions_view import MailRuleRequestSetPermissionsView
from .matching_algorithm import MatchingAlgorithm
from .metadata import Metadata
from .metadata_archive_metadata import MetadataArchiveMetadata
from .metadata_original_metadata import MetadataOriginalMetadata
from .method_enum import MethodEnum
from .migration_status import MigrationStatus
from .mode_enum import ModeEnum
from .note_create_request_request import NoteCreateRequestRequest
from .notes import Notes
from .notes_request import NotesRequest
from .object_type_enum import ObjectTypeEnum
from .operation_enum import OperationEnum
from .output_type_enum import OutputTypeEnum
from .paginated_correspondent_list import PaginatedCorrespondentList
from .paginated_custom_field_list import PaginatedCustomFieldList
from .paginated_document_list import PaginatedDocumentList
from .paginated_document_type_list import PaginatedDocumentTypeList
from .paginated_group_list import PaginatedGroupList
from .paginated_log_entry_list import PaginatedLogEntryList
from .paginated_mail_account_list import PaginatedMailAccountList
from .paginated_mail_rule_list import PaginatedMailRuleList
from .paginated_notes_list import PaginatedNotesList
from .paginated_processed_mail_list import PaginatedProcessedMailList
from .paginated_saved_view_list import PaginatedSavedViewList
from .paginated_share_link_list import PaginatedShareLinkList
from .paginated_storage_path_list import PaginatedStoragePathList
from .paginated_tag_list import PaginatedTagList
from .paginated_user_list import PaginatedUserList
from .paginated_workflow_action_list import PaginatedWorkflowActionList
from .paginated_workflow_list import PaginatedWorkflowList
from .paginated_workflow_trigger_list import PaginatedWorkflowTriggerList
from .paperless_auth_token import PaperlessAuthToken
from .paperless_auth_token_request import PaperlessAuthTokenRequest
from .patched_application_configuration_request import PatchedApplicationConfigurationRequest
from .patched_correspondent_request import PatchedCorrespondentRequest
from .patched_correspondent_request_set_permissions import PatchedCorrespondentRequestSetPermissions
from .patched_correspondent_request_set_permissions_change import PatchedCorrespondentRequestSetPermissionsChange
from .patched_correspondent_request_set_permissions_view import PatchedCorrespondentRequestSetPermissionsView
from .patched_custom_field_request import PatchedCustomFieldRequest
from .patched_document_request import PatchedDocumentRequest
from .patched_document_request_set_permissions import PatchedDocumentRequestSetPermissions
from .patched_document_request_set_permissions_change import PatchedDocumentRequestSetPermissionsChange
from .patched_document_request_set_permissions_view import PatchedDocumentRequestSetPermissionsView
from .patched_document_type_request import PatchedDocumentTypeRequest
from .patched_document_type_request_set_permissions import PatchedDocumentTypeRequestSetPermissions
from .patched_document_type_request_set_permissions_change import PatchedDocumentTypeRequestSetPermissionsChange
from .patched_document_type_request_set_permissions_view import PatchedDocumentTypeRequestSetPermissionsView
from .patched_group_request import PatchedGroupRequest
from .patched_mail_account_request import PatchedMailAccountRequest
from .patched_mail_account_request_set_permissions import PatchedMailAccountRequestSetPermissions
from .patched_mail_account_request_set_permissions_change import PatchedMailAccountRequestSetPermissionsChange
from .patched_mail_account_request_set_permissions_view import PatchedMailAccountRequestSetPermissionsView
from .patched_mail_rule_request import PatchedMailRuleRequest
from .patched_mail_rule_request_set_permissions import PatchedMailRuleRequestSetPermissions
from .patched_mail_rule_request_set_permissions_change import PatchedMailRuleRequestSetPermissionsChange
from .patched_mail_rule_request_set_permissions_view import PatchedMailRuleRequestSetPermissionsView
from .patched_profile_request import PatchedProfileRequest
from .patched_saved_view_request import PatchedSavedViewRequest
from .patched_share_link_request import PatchedShareLinkRequest
from .patched_storage_path_request import PatchedStoragePathRequest
from .patched_storage_path_request_set_permissions import PatchedStoragePathRequestSetPermissions
from .patched_storage_path_request_set_permissions_change import PatchedStoragePathRequestSetPermissionsChange
from .patched_storage_path_request_set_permissions_view import PatchedStoragePathRequestSetPermissionsView
from .patched_tag_request import PatchedTagRequest
from .patched_tag_request_set_permissions import PatchedTagRequestSetPermissions
from .patched_tag_request_set_permissions_change import PatchedTagRequestSetPermissionsChange
from .patched_tag_request_set_permissions_view import PatchedTagRequestSetPermissionsView
from .patched_user_request import PatchedUserRequest
from .patched_workflow_action_request import PatchedWorkflowActionRequest
from .patched_workflow_request import PatchedWorkflowRequest
from .patched_workflow_trigger_request import PatchedWorkflowTriggerRequest
from .pdf_layout_enum import PdfLayoutEnum
from .post_document_request import PostDocumentRequest
from .processed_mail import ProcessedMail
from .processed_mail_request import ProcessedMailRequest
from .profile import Profile
from .profile_disconnect_social_account_create_body import ProfileDisconnectSocialAccountCreateBody
from .profile_social_account_providers_retrieve_response_200 import ProfileSocialAccountProvidersRetrieveResponse200
from .profile_totp_create_body import ProfileTotpCreateBody
from .profile_totp_create_response_200 import ProfileTotpCreateResponse200
from .profile_totp_retrieve_response_200 import ProfileTotpRetrieveResponse200
from .remote_version_retrieve_response_200 import RemoteVersionRetrieveResponse200
from .rule_type_enum import RuleTypeEnum
from .sanity_check import SanityCheck
from .saved_view import SavedView
from .saved_view_filter_rule import SavedViewFilterRule
from .saved_view_filter_rule_request import SavedViewFilterRuleRequest
from .saved_view_request import SavedViewRequest
from .schedule_date_field_enum import ScheduleDateFieldEnum
from .search_result import SearchResult
from .selection_data import SelectionData
from .share_link import ShareLink
from .share_link_request import ShareLinkRequest
from .skip_archive_file_enum import SkipArchiveFileEnum
from .social_account import SocialAccount
from .social_account_request import SocialAccountRequest
from .sources_enum import SourcesEnum
from .statistics_retrieve_response_200 import StatisticsRetrieveResponse200
from .status_enum import StatusEnum
from .storage import Storage
from .storage_path import StoragePath
from .storage_path_counts import StoragePathCounts
from .storage_path_request import StoragePathRequest
from .storage_path_request_set_permissions import StoragePathRequestSetPermissions
from .storage_path_request_set_permissions_change import StoragePathRequestSetPermissionsChange
from .storage_path_request_set_permissions_view import StoragePathRequestSetPermissionsView
from .suggestions import Suggestions
from .system_status import SystemStatus
from .tag import Tag
from .tag_counts import TagCounts
from .tag_request import TagRequest
from .tag_request_set_permissions import TagRequestSetPermissions
from .tag_request_set_permissions_change import TagRequestSetPermissionsChange
from .tag_request_set_permissions_view import TagRequestSetPermissionsView
from .task_name_enum import TaskNameEnum
from .tasks import Tasks
from .tasks_list_task_name import TasksListTaskName
from .tasks_list_task_state import TasksListTaskState
from .tasks_list_task_type import TasksListTaskType
from .tasks_view import TasksView
from .tasks_view_request import TasksViewRequest
from .tasks_view_type_enum import TasksViewTypeEnum
from .trash_action_enum import TrashActionEnum
from .trash_request import TrashRequest
from .ui_settings_view import UiSettingsView
from .ui_settings_view_request import UiSettingsViewRequest
from .ui_settings_view_request_settings_type_0 import UiSettingsViewRequestSettingsType0
from .ui_settings_view_settings_type_0 import UiSettingsViewSettingsType0
from .unpaper_clean_enum import UnpaperCleanEnum
from .user import User
from .user_request import UserRequest
from .workflow import Workflow
from .workflow_action import WorkflowAction
from .workflow_action_email import WorkflowActionEmail
from .workflow_action_email_request import WorkflowActionEmailRequest
from .workflow_action_request import WorkflowActionRequest
from .workflow_action_type_enum import WorkflowActionTypeEnum
from .workflow_action_webhook import WorkflowActionWebhook
from .workflow_action_webhook_request import WorkflowActionWebhookRequest
from .workflow_request import WorkflowRequest
from .workflow_trigger import WorkflowTrigger
from .workflow_trigger_matching_algorithm_enum import WorkflowTriggerMatchingAlgorithmEnum
from .workflow_trigger_request import WorkflowTriggerRequest
from .workflow_trigger_type_enum import WorkflowTriggerTypeEnum

__all__ = (
    "AccountTypeEnum",
    "AcknowledgeTasks",
    "AcknowledgeTasksBody",
    "Actor",
    "ApplicationConfiguration",
    "ApplicationConfigurationRequest",
    "AssignCorrespondentFromEnum",
    "AssignTitleFromEnum",
    "AttachmentTypeEnum",
    "BasicUser",
    "BasicUserRequest",
    "BlankEnum",
    "BulkDownload",
    "BulkDownloadRequest",
    "BulkEditDocumentsResult",
    "BulkEditObjectsRequest",
    "BulkEditObjectsRequestSetPermissions",
    "BulkEditRequest",
    "BulkEditRequestParameters",
    "BulkEditResult",
    "Classifier",
    "ColorConversionStrategyEnum",
    "CompressionEnum",
    "ConsumptionScopeEnum",
    "ContentEnum",
    "Correspondent",
    "CorrespondentCounts",
    "CorrespondentPermissions",
    "CorrespondentPermissionsChange",
    "CorrespondentPermissionsView",
    "CorrespondentRequest",
    "CorrespondentRequestSetPermissions",
    "CorrespondentRequestSetPermissionsChange",
    "CorrespondentRequestSetPermissionsView",
    "CustomField",
    "CustomFieldCounts",
    "CustomFieldInstance",
    "CustomFieldInstanceRequest",
    "CustomFieldInstanceRequestValueType3",
    "CustomFieldInstanceValueType3",
    "CustomFieldRequest",
    "Database",
    "DataTypeEnum",
    "DisplayModeEnum",
    "Document",
    "DocumentListRequest",
    "DocumentPermissions",
    "DocumentPermissionsChange",
    "DocumentPermissionsView",
    "DocumentRequest",
    "DocumentRequestSetPermissions",
    "DocumentRequestSetPermissionsChange",
    "DocumentRequestSetPermissionsView",
    "DocumentShareLinksResponse200Item",
    "DocumentType",
    "DocumentTypeCounts",
    "DocumentTypePermissions",
    "DocumentTypePermissionsChange",
    "DocumentTypePermissionsView",
    "DocumentTypeRequest",
    "DocumentTypeRequestSetPermissions",
    "DocumentTypeRequestSetPermissionsChange",
    "DocumentTypeRequestSetPermissionsView",
    "EmailDocumentRequestRequest",
    "EmailDocumentResponse",
    "EmailDocumentsResponse",
    "EmailRequest",
    "FileVersionEnum",
    "Group",
    "GroupRequest",
    "ImapSecurityEnum",
    "Index",
    "LogEntry",
    "LogEntryChanges",
    "MailAccount",
    "MailAccountProcessResponse",
    "MailAccountRequest",
    "MailAccountRequestSetPermissions",
    "MailAccountRequestSetPermissionsChange",
    "MailAccountRequestSetPermissionsView",
    "MailAccountTestResponse",
    "MailRule",
    "MailRuleActionEnum",
    "MailRuleRequest",
    "MailRuleRequestSetPermissions",
    "MailRuleRequestSetPermissionsChange",
    "MailRuleRequestSetPermissionsView",
    "MatchingAlgorithm",
    "Metadata",
    "MetadataArchiveMetadata",
    "MetadataOriginalMetadata",
    "MethodEnum",
    "MigrationStatus",
    "ModeEnum",
    "NoteCreateRequestRequest",
    "Notes",
    "NotesRequest",
    "ObjectTypeEnum",
    "OperationEnum",
    "OutputTypeEnum",
    "PaginatedCorrespondentList",
    "PaginatedCustomFieldList",
    "PaginatedDocumentList",
    "PaginatedDocumentTypeList",
    "PaginatedGroupList",
    "PaginatedLogEntryList",
    "PaginatedMailAccountList",
    "PaginatedMailRuleList",
    "PaginatedNotesList",
    "PaginatedProcessedMailList",
    "PaginatedSavedViewList",
    "PaginatedShareLinkList",
    "PaginatedStoragePathList",
    "PaginatedTagList",
    "PaginatedUserList",
    "PaginatedWorkflowActionList",
    "PaginatedWorkflowList",
    "PaginatedWorkflowTriggerList",
    "PaperlessAuthToken",
    "PaperlessAuthTokenRequest",
    "PatchedApplicationConfigurationRequest",
    "PatchedCorrespondentRequest",
    "PatchedCorrespondentRequestSetPermissions",
    "PatchedCorrespondentRequestSetPermissionsChange",
    "PatchedCorrespondentRequestSetPermissionsView",
    "PatchedCustomFieldRequest",
    "PatchedDocumentRequest",
    "PatchedDocumentRequestSetPermissions",
    "PatchedDocumentRequestSetPermissionsChange",
    "PatchedDocumentRequestSetPermissionsView",
    "PatchedDocumentTypeRequest",
    "PatchedDocumentTypeRequestSetPermissions",
    "PatchedDocumentTypeRequestSetPermissionsChange",
    "PatchedDocumentTypeRequestSetPermissionsView",
    "PatchedGroupRequest",
    "PatchedMailAccountRequest",
    "PatchedMailAccountRequestSetPermissions",
    "PatchedMailAccountRequestSetPermissionsChange",
    "PatchedMailAccountRequestSetPermissionsView",
    "PatchedMailRuleRequest",
    "PatchedMailRuleRequestSetPermissions",
    "PatchedMailRuleRequestSetPermissionsChange",
    "PatchedMailRuleRequestSetPermissionsView",
    "PatchedProfileRequest",
    "PatchedSavedViewRequest",
    "PatchedShareLinkRequest",
    "PatchedStoragePathRequest",
    "PatchedStoragePathRequestSetPermissions",
    "PatchedStoragePathRequestSetPermissionsChange",
    "PatchedStoragePathRequestSetPermissionsView",
    "PatchedTagRequest",
    "PatchedTagRequestSetPermissions",
    "PatchedTagRequestSetPermissionsChange",
    "PatchedTagRequestSetPermissionsView",
    "PatchedUserRequest",
    "PatchedWorkflowActionRequest",
    "PatchedWorkflowRequest",
    "PatchedWorkflowTriggerRequest",
    "PdfLayoutEnum",
    "PostDocumentRequest",
    "ProcessedMail",
    "ProcessedMailRequest",
    "Profile",
    "ProfileDisconnectSocialAccountCreateBody",
    "ProfileSocialAccountProvidersRetrieveResponse200",
    "ProfileTotpCreateBody",
    "ProfileTotpCreateResponse200",
    "ProfileTotpRetrieveResponse200",
    "RemoteVersionRetrieveResponse200",
    "RuleTypeEnum",
    "SanityCheck",
    "SavedView",
    "SavedViewFilterRule",
    "SavedViewFilterRuleRequest",
    "SavedViewRequest",
    "ScheduleDateFieldEnum",
    "SearchResult",
    "SelectionData",
    "ShareLink",
    "ShareLinkRequest",
    "SkipArchiveFileEnum",
    "SocialAccount",
    "SocialAccountRequest",
    "SourcesEnum",
    "StatisticsRetrieveResponse200",
    "StatusEnum",
    "Storage",
    "StoragePath",
    "StoragePathCounts",
    "StoragePathRequest",
    "StoragePathRequestSetPermissions",
    "StoragePathRequestSetPermissionsChange",
    "StoragePathRequestSetPermissionsView",
    "Suggestions",
    "SystemStatus",
    "Tag",
    "TagCounts",
    "TagRequest",
    "TagRequestSetPermissions",
    "TagRequestSetPermissionsChange",
    "TagRequestSetPermissionsView",
    "TaskNameEnum",
    "Tasks",
    "TasksListTaskName",
    "TasksListTaskState",
    "TasksListTaskType",
    "TasksView",
    "TasksViewRequest",
    "TasksViewTypeEnum",
    "TrashActionEnum",
    "TrashRequest",
    "UiSettingsView",
    "UiSettingsViewRequest",
    "UiSettingsViewRequestSettingsType0",
    "UiSettingsViewSettingsType0",
    "UnpaperCleanEnum",
    "User",
    "UserRequest",
    "Workflow",
    "WorkflowAction",
    "WorkflowActionEmail",
    "WorkflowActionEmailRequest",
    "WorkflowActionRequest",
    "WorkflowActionTypeEnum",
    "WorkflowActionWebhook",
    "WorkflowActionWebhookRequest",
    "WorkflowRequest",
    "WorkflowTrigger",
    "WorkflowTriggerMatchingAlgorithmEnum",
    "WorkflowTriggerRequest",
    "WorkflowTriggerTypeEnum",
)
