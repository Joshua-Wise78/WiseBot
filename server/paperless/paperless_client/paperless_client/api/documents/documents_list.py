import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_document_list import PaginatedDocumentList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    added_date_gt: datetime.date | Unset = UNSET,
    added_date_gte: datetime.date | Unset = UNSET,
    added_date_lt: datetime.date | Unset = UNSET,
    added_date_lte: datetime.date | Unset = UNSET,
    added_day: float | Unset = UNSET,
    added_gt: datetime.datetime | Unset = UNSET,
    added_gte: datetime.datetime | Unset = UNSET,
    added_lt: datetime.datetime | Unset = UNSET,
    added_lte: datetime.datetime | Unset = UNSET,
    added_month: float | Unset = UNSET,
    added_year: float | Unset = UNSET,
    archive_serial_number: int | Unset = UNSET,
    archive_serial_number_gt: int | Unset = UNSET,
    archive_serial_number_gte: int | Unset = UNSET,
    archive_serial_number_isnull: bool | Unset = UNSET,
    archive_serial_number_lt: int | Unset = UNSET,
    archive_serial_number_lte: int | Unset = UNSET,
    checksum_icontains: str | Unset = UNSET,
    checksum_iendswith: str | Unset = UNSET,
    checksum_iexact: str | Unset = UNSET,
    checksum_istartswith: str | Unset = UNSET,
    content_icontains: str | Unset = UNSET,
    content_iendswith: str | Unset = UNSET,
    content_iexact: str | Unset = UNSET,
    content_istartswith: str | Unset = UNSET,
    correspondent_id: int | Unset = UNSET,
    correspondent_id_in: list[int] | Unset = UNSET,
    correspondent_id_none: int | Unset = UNSET,
    correspondent_isnull: bool | Unset = UNSET,
    correspondent_name_icontains: str | Unset = UNSET,
    correspondent_name_iendswith: str | Unset = UNSET,
    correspondent_name_iexact: str | Unset = UNSET,
    correspondent_name_istartswith: str | Unset = UNSET,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.date | Unset = UNSET,
    created_gte: datetime.date | Unset = UNSET,
    created_lt: datetime.date | Unset = UNSET,
    created_lte: datetime.date | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    custom_field_query: str | Unset = UNSET,
    custom_fields_icontains: str | Unset = UNSET,
    custom_fields_id_all: int | Unset = UNSET,
    custom_fields_id_in: int | Unset = UNSET,
    custom_fields_id_none: int | Unset = UNSET,
    document_type_id: int | Unset = UNSET,
    document_type_id_in: list[int] | Unset = UNSET,
    document_type_id_none: int | Unset = UNSET,
    document_type_isnull: bool | Unset = UNSET,
    document_type_name_icontains: str | Unset = UNSET,
    document_type_name_iendswith: str | Unset = UNSET,
    document_type_name_iexact: str | Unset = UNSET,
    document_type_name_istartswith: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
    has_custom_fields: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_in_inbox: bool | Unset = UNSET,
    is_tagged: bool | Unset = UNSET,
    mime_type: str | Unset = UNSET,
    modified_date_gt: datetime.date | Unset = UNSET,
    modified_date_gte: datetime.date | Unset = UNSET,
    modified_date_lt: datetime.date | Unset = UNSET,
    modified_date_lte: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_gt: datetime.datetime | Unset = UNSET,
    modified_gte: datetime.datetime | Unset = UNSET,
    modified_lt: datetime.datetime | Unset = UNSET,
    modified_lte: datetime.datetime | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    original_filename_icontains: str | Unset = UNSET,
    original_filename_iendswith: str | Unset = UNSET,
    original_filename_iexact: str | Unset = UNSET,
    original_filename_istartswith: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    owner_id_in: list[int] | Unset = UNSET,
    owner_id_none: int | Unset = UNSET,
    owner_isnull: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    query: str | Unset = UNSET,
    search: str | Unset = UNSET,
    shared_by_id: bool | Unset = UNSET,
    storage_path_id: int | Unset = UNSET,
    storage_path_id_in: list[int] | Unset = UNSET,
    storage_path_id_none: int | Unset = UNSET,
    storage_path_isnull: bool | Unset = UNSET,
    storage_path_name_icontains: str | Unset = UNSET,
    storage_path_name_iendswith: str | Unset = UNSET,
    storage_path_name_iexact: str | Unset = UNSET,
    storage_path_name_istartswith: str | Unset = UNSET,
    tags_id: int | Unset = UNSET,
    tags_id_all: int | Unset = UNSET,
    tags_id_in: int | Unset = UNSET,
    tags_id_none: int | Unset = UNSET,
    tags_name_icontains: str | Unset = UNSET,
    tags_name_iendswith: str | Unset = UNSET,
    tags_name_iexact: str | Unset = UNSET,
    tags_name_istartswith: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_content: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added_date_gt: str | Unset = UNSET
    if not isinstance(added_date_gt, Unset):
        json_added_date_gt = added_date_gt.isoformat()
    params["added__date__gt"] = json_added_date_gt

    json_added_date_gte: str | Unset = UNSET
    if not isinstance(added_date_gte, Unset):
        json_added_date_gte = added_date_gte.isoformat()
    params["added__date__gte"] = json_added_date_gte

    json_added_date_lt: str | Unset = UNSET
    if not isinstance(added_date_lt, Unset):
        json_added_date_lt = added_date_lt.isoformat()
    params["added__date__lt"] = json_added_date_lt

    json_added_date_lte: str | Unset = UNSET
    if not isinstance(added_date_lte, Unset):
        json_added_date_lte = added_date_lte.isoformat()
    params["added__date__lte"] = json_added_date_lte

    params["added__day"] = added_day

    json_added_gt: str | Unset = UNSET
    if not isinstance(added_gt, Unset):
        json_added_gt = added_gt.isoformat()
    params["added__gt"] = json_added_gt

    json_added_gte: str | Unset = UNSET
    if not isinstance(added_gte, Unset):
        json_added_gte = added_gte.isoformat()
    params["added__gte"] = json_added_gte

    json_added_lt: str | Unset = UNSET
    if not isinstance(added_lt, Unset):
        json_added_lt = added_lt.isoformat()
    params["added__lt"] = json_added_lt

    json_added_lte: str | Unset = UNSET
    if not isinstance(added_lte, Unset):
        json_added_lte = added_lte.isoformat()
    params["added__lte"] = json_added_lte

    params["added__month"] = added_month

    params["added__year"] = added_year

    params["archive_serial_number"] = archive_serial_number

    params["archive_serial_number__gt"] = archive_serial_number_gt

    params["archive_serial_number__gte"] = archive_serial_number_gte

    params["archive_serial_number__isnull"] = archive_serial_number_isnull

    params["archive_serial_number__lt"] = archive_serial_number_lt

    params["archive_serial_number__lte"] = archive_serial_number_lte

    params["checksum__icontains"] = checksum_icontains

    params["checksum__iendswith"] = checksum_iendswith

    params["checksum__iexact"] = checksum_iexact

    params["checksum__istartswith"] = checksum_istartswith

    params["content__icontains"] = content_icontains

    params["content__iendswith"] = content_iendswith

    params["content__iexact"] = content_iexact

    params["content__istartswith"] = content_istartswith

    params["correspondent__id"] = correspondent_id

    json_correspondent_id_in: list[int] | Unset = UNSET
    if not isinstance(correspondent_id_in, Unset):
        json_correspondent_id_in = correspondent_id_in

    params["correspondent__id__in"] = json_correspondent_id_in

    params["correspondent__id__none"] = correspondent_id_none

    params["correspondent__isnull"] = correspondent_isnull

    params["correspondent__name__icontains"] = correspondent_name_icontains

    params["correspondent__name__iendswith"] = correspondent_name_iendswith

    params["correspondent__name__iexact"] = correspondent_name_iexact

    params["correspondent__name__istartswith"] = correspondent_name_istartswith

    json_created_date_gt: str | Unset = UNSET
    if not isinstance(created_date_gt, Unset):
        json_created_date_gt = created_date_gt.isoformat()
    params["created__date__gt"] = json_created_date_gt

    json_created_date_gte: str | Unset = UNSET
    if not isinstance(created_date_gte, Unset):
        json_created_date_gte = created_date_gte.isoformat()
    params["created__date__gte"] = json_created_date_gte

    json_created_date_lt: str | Unset = UNSET
    if not isinstance(created_date_lt, Unset):
        json_created_date_lt = created_date_lt.isoformat()
    params["created__date__lt"] = json_created_date_lt

    json_created_date_lte: str | Unset = UNSET
    if not isinstance(created_date_lte, Unset):
        json_created_date_lte = created_date_lte.isoformat()
    params["created__date__lte"] = json_created_date_lte

    params["created__day"] = created_day

    json_created_gt: str | Unset = UNSET
    if not isinstance(created_gt, Unset):
        json_created_gt = created_gt.isoformat()
    params["created__gt"] = json_created_gt

    json_created_gte: str | Unset = UNSET
    if not isinstance(created_gte, Unset):
        json_created_gte = created_gte.isoformat()
    params["created__gte"] = json_created_gte

    json_created_lt: str | Unset = UNSET
    if not isinstance(created_lt, Unset):
        json_created_lt = created_lt.isoformat()
    params["created__lt"] = json_created_lt

    json_created_lte: str | Unset = UNSET
    if not isinstance(created_lte, Unset):
        json_created_lte = created_lte.isoformat()
    params["created__lte"] = json_created_lte

    params["created__month"] = created_month

    params["created__year"] = created_year

    params["custom_field_query"] = custom_field_query

    params["custom_fields__icontains"] = custom_fields_icontains

    params["custom_fields__id__all"] = custom_fields_id_all

    params["custom_fields__id__in"] = custom_fields_id_in

    params["custom_fields__id__none"] = custom_fields_id_none

    params["document_type__id"] = document_type_id

    json_document_type_id_in: list[int] | Unset = UNSET
    if not isinstance(document_type_id_in, Unset):
        json_document_type_id_in = document_type_id_in

    params["document_type__id__in"] = json_document_type_id_in

    params["document_type__id__none"] = document_type_id_none

    params["document_type__isnull"] = document_type_isnull

    params["document_type__name__icontains"] = document_type_name_icontains

    params["document_type__name__iendswith"] = document_type_name_iendswith

    params["document_type__name__iexact"] = document_type_name_iexact

    params["document_type__name__istartswith"] = document_type_name_istartswith

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["full_perms"] = full_perms

    params["has_custom_fields"] = has_custom_fields

    params["id"] = id

    json_id_in: list[int] | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = id_in

    params["id__in"] = json_id_in

    params["is_in_inbox"] = is_in_inbox

    params["is_tagged"] = is_tagged

    params["mime_type"] = mime_type

    json_modified_date_gt: str | Unset = UNSET
    if not isinstance(modified_date_gt, Unset):
        json_modified_date_gt = modified_date_gt.isoformat()
    params["modified__date__gt"] = json_modified_date_gt

    json_modified_date_gte: str | Unset = UNSET
    if not isinstance(modified_date_gte, Unset):
        json_modified_date_gte = modified_date_gte.isoformat()
    params["modified__date__gte"] = json_modified_date_gte

    json_modified_date_lt: str | Unset = UNSET
    if not isinstance(modified_date_lt, Unset):
        json_modified_date_lt = modified_date_lt.isoformat()
    params["modified__date__lt"] = json_modified_date_lt

    json_modified_date_lte: str | Unset = UNSET
    if not isinstance(modified_date_lte, Unset):
        json_modified_date_lte = modified_date_lte.isoformat()
    params["modified__date__lte"] = json_modified_date_lte

    params["modified__day"] = modified_day

    json_modified_gt: str | Unset = UNSET
    if not isinstance(modified_gt, Unset):
        json_modified_gt = modified_gt.isoformat()
    params["modified__gt"] = json_modified_gt

    json_modified_gte: str | Unset = UNSET
    if not isinstance(modified_gte, Unset):
        json_modified_gte = modified_gte.isoformat()
    params["modified__gte"] = json_modified_gte

    json_modified_lt: str | Unset = UNSET
    if not isinstance(modified_lt, Unset):
        json_modified_lt = modified_lt.isoformat()
    params["modified__lt"] = json_modified_lt

    json_modified_lte: str | Unset = UNSET
    if not isinstance(modified_lte, Unset):
        json_modified_lte = modified_lte.isoformat()
    params["modified__lte"] = json_modified_lte

    params["modified__month"] = modified_month

    params["modified__year"] = modified_year

    params["ordering"] = ordering

    params["original_filename__icontains"] = original_filename_icontains

    params["original_filename__iendswith"] = original_filename_iendswith

    params["original_filename__iexact"] = original_filename_iexact

    params["original_filename__istartswith"] = original_filename_istartswith

    params["owner__id"] = owner_id

    json_owner_id_in: list[int] | Unset = UNSET
    if not isinstance(owner_id_in, Unset):
        json_owner_id_in = owner_id_in

    params["owner__id__in"] = json_owner_id_in

    params["owner__id__none"] = owner_id_none

    params["owner__isnull"] = owner_isnull

    params["page"] = page

    params["page_size"] = page_size

    params["query"] = query

    params["search"] = search

    params["shared_by__id"] = shared_by_id

    params["storage_path__id"] = storage_path_id

    json_storage_path_id_in: list[int] | Unset = UNSET
    if not isinstance(storage_path_id_in, Unset):
        json_storage_path_id_in = storage_path_id_in

    params["storage_path__id__in"] = json_storage_path_id_in

    params["storage_path__id__none"] = storage_path_id_none

    params["storage_path__isnull"] = storage_path_isnull

    params["storage_path__name__icontains"] = storage_path_name_icontains

    params["storage_path__name__iendswith"] = storage_path_name_iendswith

    params["storage_path__name__iexact"] = storage_path_name_iexact

    params["storage_path__name__istartswith"] = storage_path_name_istartswith

    params["tags__id"] = tags_id

    params["tags__id__all"] = tags_id_all

    params["tags__id__in"] = tags_id_in

    params["tags__id__none"] = tags_id_none

    params["tags__name__icontains"] = tags_name_icontains

    params["tags__name__iendswith"] = tags_name_iendswith

    params["tags__name__iexact"] = tags_name_iexact

    params["tags__name__istartswith"] = tags_name_istartswith

    params["title__icontains"] = title_icontains

    params["title__iendswith"] = title_iendswith

    params["title__iexact"] = title_iexact

    params["title__istartswith"] = title_istartswith

    params["title_content"] = title_content

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/documents/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedDocumentList | None:
    if response.status_code == 200:
        response_200 = PaginatedDocumentList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedDocumentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    added_date_gt: datetime.date | Unset = UNSET,
    added_date_gte: datetime.date | Unset = UNSET,
    added_date_lt: datetime.date | Unset = UNSET,
    added_date_lte: datetime.date | Unset = UNSET,
    added_day: float | Unset = UNSET,
    added_gt: datetime.datetime | Unset = UNSET,
    added_gte: datetime.datetime | Unset = UNSET,
    added_lt: datetime.datetime | Unset = UNSET,
    added_lte: datetime.datetime | Unset = UNSET,
    added_month: float | Unset = UNSET,
    added_year: float | Unset = UNSET,
    archive_serial_number: int | Unset = UNSET,
    archive_serial_number_gt: int | Unset = UNSET,
    archive_serial_number_gte: int | Unset = UNSET,
    archive_serial_number_isnull: bool | Unset = UNSET,
    archive_serial_number_lt: int | Unset = UNSET,
    archive_serial_number_lte: int | Unset = UNSET,
    checksum_icontains: str | Unset = UNSET,
    checksum_iendswith: str | Unset = UNSET,
    checksum_iexact: str | Unset = UNSET,
    checksum_istartswith: str | Unset = UNSET,
    content_icontains: str | Unset = UNSET,
    content_iendswith: str | Unset = UNSET,
    content_iexact: str | Unset = UNSET,
    content_istartswith: str | Unset = UNSET,
    correspondent_id: int | Unset = UNSET,
    correspondent_id_in: list[int] | Unset = UNSET,
    correspondent_id_none: int | Unset = UNSET,
    correspondent_isnull: bool | Unset = UNSET,
    correspondent_name_icontains: str | Unset = UNSET,
    correspondent_name_iendswith: str | Unset = UNSET,
    correspondent_name_iexact: str | Unset = UNSET,
    correspondent_name_istartswith: str | Unset = UNSET,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.date | Unset = UNSET,
    created_gte: datetime.date | Unset = UNSET,
    created_lt: datetime.date | Unset = UNSET,
    created_lte: datetime.date | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    custom_field_query: str | Unset = UNSET,
    custom_fields_icontains: str | Unset = UNSET,
    custom_fields_id_all: int | Unset = UNSET,
    custom_fields_id_in: int | Unset = UNSET,
    custom_fields_id_none: int | Unset = UNSET,
    document_type_id: int | Unset = UNSET,
    document_type_id_in: list[int] | Unset = UNSET,
    document_type_id_none: int | Unset = UNSET,
    document_type_isnull: bool | Unset = UNSET,
    document_type_name_icontains: str | Unset = UNSET,
    document_type_name_iendswith: str | Unset = UNSET,
    document_type_name_iexact: str | Unset = UNSET,
    document_type_name_istartswith: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
    has_custom_fields: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_in_inbox: bool | Unset = UNSET,
    is_tagged: bool | Unset = UNSET,
    mime_type: str | Unset = UNSET,
    modified_date_gt: datetime.date | Unset = UNSET,
    modified_date_gte: datetime.date | Unset = UNSET,
    modified_date_lt: datetime.date | Unset = UNSET,
    modified_date_lte: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_gt: datetime.datetime | Unset = UNSET,
    modified_gte: datetime.datetime | Unset = UNSET,
    modified_lt: datetime.datetime | Unset = UNSET,
    modified_lte: datetime.datetime | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    original_filename_icontains: str | Unset = UNSET,
    original_filename_iendswith: str | Unset = UNSET,
    original_filename_iexact: str | Unset = UNSET,
    original_filename_istartswith: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    owner_id_in: list[int] | Unset = UNSET,
    owner_id_none: int | Unset = UNSET,
    owner_isnull: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    query: str | Unset = UNSET,
    search: str | Unset = UNSET,
    shared_by_id: bool | Unset = UNSET,
    storage_path_id: int | Unset = UNSET,
    storage_path_id_in: list[int] | Unset = UNSET,
    storage_path_id_none: int | Unset = UNSET,
    storage_path_isnull: bool | Unset = UNSET,
    storage_path_name_icontains: str | Unset = UNSET,
    storage_path_name_iendswith: str | Unset = UNSET,
    storage_path_name_iexact: str | Unset = UNSET,
    storage_path_name_istartswith: str | Unset = UNSET,
    tags_id: int | Unset = UNSET,
    tags_id_all: int | Unset = UNSET,
    tags_id_in: int | Unset = UNSET,
    tags_id_none: int | Unset = UNSET,
    tags_name_icontains: str | Unset = UNSET,
    tags_name_iendswith: str | Unset = UNSET,
    tags_name_iexact: str | Unset = UNSET,
    tags_name_istartswith: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_content: str | Unset = UNSET,
) -> Response[PaginatedDocumentList]:
    """Document views including search

    Args:
        added_date_gt (datetime.date | Unset):
        added_date_gte (datetime.date | Unset):
        added_date_lt (datetime.date | Unset):
        added_date_lte (datetime.date | Unset):
        added_day (float | Unset):
        added_gt (datetime.datetime | Unset):
        added_gte (datetime.datetime | Unset):
        added_lt (datetime.datetime | Unset):
        added_lte (datetime.datetime | Unset):
        added_month (float | Unset):
        added_year (float | Unset):
        archive_serial_number (int | Unset):
        archive_serial_number_gt (int | Unset):
        archive_serial_number_gte (int | Unset):
        archive_serial_number_isnull (bool | Unset):
        archive_serial_number_lt (int | Unset):
        archive_serial_number_lte (int | Unset):
        checksum_icontains (str | Unset):
        checksum_iendswith (str | Unset):
        checksum_iexact (str | Unset):
        checksum_istartswith (str | Unset):
        content_icontains (str | Unset):
        content_iendswith (str | Unset):
        content_iexact (str | Unset):
        content_istartswith (str | Unset):
        correspondent_id (int | Unset):
        correspondent_id_in (list[int] | Unset):
        correspondent_id_none (int | Unset):
        correspondent_isnull (bool | Unset):
        correspondent_name_icontains (str | Unset):
        correspondent_name_iendswith (str | Unset):
        correspondent_name_iexact (str | Unset):
        correspondent_name_istartswith (str | Unset):
        created_date_gt (datetime.date | Unset):
        created_date_gte (datetime.date | Unset):
        created_date_lt (datetime.date | Unset):
        created_date_lte (datetime.date | Unset):
        created_day (float | Unset):
        created_gt (datetime.date | Unset):
        created_gte (datetime.date | Unset):
        created_lt (datetime.date | Unset):
        created_lte (datetime.date | Unset):
        created_month (float | Unset):
        created_year (float | Unset):
        custom_field_query (str | Unset):
        custom_fields_icontains (str | Unset):
        custom_fields_id_all (int | Unset):
        custom_fields_id_in (int | Unset):
        custom_fields_id_none (int | Unset):
        document_type_id (int | Unset):
        document_type_id_in (list[int] | Unset):
        document_type_id_none (int | Unset):
        document_type_isnull (bool | Unset):
        document_type_name_icontains (str | Unset):
        document_type_name_iendswith (str | Unset):
        document_type_name_iexact (str | Unset):
        document_type_name_istartswith (str | Unset):
        fields (list[str] | Unset):
        full_perms (bool | Unset):
        has_custom_fields (bool | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        is_in_inbox (bool | Unset):
        is_tagged (bool | Unset):
        mime_type (str | Unset):
        modified_date_gt (datetime.date | Unset):
        modified_date_gte (datetime.date | Unset):
        modified_date_lt (datetime.date | Unset):
        modified_date_lte (datetime.date | Unset):
        modified_day (float | Unset):
        modified_gt (datetime.datetime | Unset):
        modified_gte (datetime.datetime | Unset):
        modified_lt (datetime.datetime | Unset):
        modified_lte (datetime.datetime | Unset):
        modified_month (float | Unset):
        modified_year (float | Unset):
        ordering (str | Unset):
        original_filename_icontains (str | Unset):
        original_filename_iendswith (str | Unset):
        original_filename_iexact (str | Unset):
        original_filename_istartswith (str | Unset):
        owner_id (int | Unset):
        owner_id_in (list[int] | Unset):
        owner_id_none (int | Unset):
        owner_isnull (bool | Unset):
        page (int | Unset):
        page_size (int | Unset):
        query (str | Unset):
        search (str | Unset):
        shared_by_id (bool | Unset):
        storage_path_id (int | Unset):
        storage_path_id_in (list[int] | Unset):
        storage_path_id_none (int | Unset):
        storage_path_isnull (bool | Unset):
        storage_path_name_icontains (str | Unset):
        storage_path_name_iendswith (str | Unset):
        storage_path_name_iexact (str | Unset):
        storage_path_name_istartswith (str | Unset):
        tags_id (int | Unset):
        tags_id_all (int | Unset):
        tags_id_in (int | Unset):
        tags_id_none (int | Unset):
        tags_name_icontains (str | Unset):
        tags_name_iendswith (str | Unset):
        tags_name_iexact (str | Unset):
        tags_name_istartswith (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_istartswith (str | Unset):
        title_content (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDocumentList]
    """

    kwargs = _get_kwargs(
        added_date_gt=added_date_gt,
        added_date_gte=added_date_gte,
        added_date_lt=added_date_lt,
        added_date_lte=added_date_lte,
        added_day=added_day,
        added_gt=added_gt,
        added_gte=added_gte,
        added_lt=added_lt,
        added_lte=added_lte,
        added_month=added_month,
        added_year=added_year,
        archive_serial_number=archive_serial_number,
        archive_serial_number_gt=archive_serial_number_gt,
        archive_serial_number_gte=archive_serial_number_gte,
        archive_serial_number_isnull=archive_serial_number_isnull,
        archive_serial_number_lt=archive_serial_number_lt,
        archive_serial_number_lte=archive_serial_number_lte,
        checksum_icontains=checksum_icontains,
        checksum_iendswith=checksum_iendswith,
        checksum_iexact=checksum_iexact,
        checksum_istartswith=checksum_istartswith,
        content_icontains=content_icontains,
        content_iendswith=content_iendswith,
        content_iexact=content_iexact,
        content_istartswith=content_istartswith,
        correspondent_id=correspondent_id,
        correspondent_id_in=correspondent_id_in,
        correspondent_id_none=correspondent_id_none,
        correspondent_isnull=correspondent_isnull,
        correspondent_name_icontains=correspondent_name_icontains,
        correspondent_name_iendswith=correspondent_name_iendswith,
        correspondent_name_iexact=correspondent_name_iexact,
        correspondent_name_istartswith=correspondent_name_istartswith,
        created_date_gt=created_date_gt,
        created_date_gte=created_date_gte,
        created_date_lt=created_date_lt,
        created_date_lte=created_date_lte,
        created_day=created_day,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_month=created_month,
        created_year=created_year,
        custom_field_query=custom_field_query,
        custom_fields_icontains=custom_fields_icontains,
        custom_fields_id_all=custom_fields_id_all,
        custom_fields_id_in=custom_fields_id_in,
        custom_fields_id_none=custom_fields_id_none,
        document_type_id=document_type_id,
        document_type_id_in=document_type_id_in,
        document_type_id_none=document_type_id_none,
        document_type_isnull=document_type_isnull,
        document_type_name_icontains=document_type_name_icontains,
        document_type_name_iendswith=document_type_name_iendswith,
        document_type_name_iexact=document_type_name_iexact,
        document_type_name_istartswith=document_type_name_istartswith,
        fields=fields,
        full_perms=full_perms,
        has_custom_fields=has_custom_fields,
        id=id,
        id_in=id_in,
        is_in_inbox=is_in_inbox,
        is_tagged=is_tagged,
        mime_type=mime_type,
        modified_date_gt=modified_date_gt,
        modified_date_gte=modified_date_gte,
        modified_date_lt=modified_date_lt,
        modified_date_lte=modified_date_lte,
        modified_day=modified_day,
        modified_gt=modified_gt,
        modified_gte=modified_gte,
        modified_lt=modified_lt,
        modified_lte=modified_lte,
        modified_month=modified_month,
        modified_year=modified_year,
        ordering=ordering,
        original_filename_icontains=original_filename_icontains,
        original_filename_iendswith=original_filename_iendswith,
        original_filename_iexact=original_filename_iexact,
        original_filename_istartswith=original_filename_istartswith,
        owner_id=owner_id,
        owner_id_in=owner_id_in,
        owner_id_none=owner_id_none,
        owner_isnull=owner_isnull,
        page=page,
        page_size=page_size,
        query=query,
        search=search,
        shared_by_id=shared_by_id,
        storage_path_id=storage_path_id,
        storage_path_id_in=storage_path_id_in,
        storage_path_id_none=storage_path_id_none,
        storage_path_isnull=storage_path_isnull,
        storage_path_name_icontains=storage_path_name_icontains,
        storage_path_name_iendswith=storage_path_name_iendswith,
        storage_path_name_iexact=storage_path_name_iexact,
        storage_path_name_istartswith=storage_path_name_istartswith,
        tags_id=tags_id,
        tags_id_all=tags_id_all,
        tags_id_in=tags_id_in,
        tags_id_none=tags_id_none,
        tags_name_icontains=tags_name_icontains,
        tags_name_iendswith=tags_name_iendswith,
        tags_name_iexact=tags_name_iexact,
        tags_name_istartswith=tags_name_istartswith,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_istartswith=title_istartswith,
        title_content=title_content,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    added_date_gt: datetime.date | Unset = UNSET,
    added_date_gte: datetime.date | Unset = UNSET,
    added_date_lt: datetime.date | Unset = UNSET,
    added_date_lte: datetime.date | Unset = UNSET,
    added_day: float | Unset = UNSET,
    added_gt: datetime.datetime | Unset = UNSET,
    added_gte: datetime.datetime | Unset = UNSET,
    added_lt: datetime.datetime | Unset = UNSET,
    added_lte: datetime.datetime | Unset = UNSET,
    added_month: float | Unset = UNSET,
    added_year: float | Unset = UNSET,
    archive_serial_number: int | Unset = UNSET,
    archive_serial_number_gt: int | Unset = UNSET,
    archive_serial_number_gte: int | Unset = UNSET,
    archive_serial_number_isnull: bool | Unset = UNSET,
    archive_serial_number_lt: int | Unset = UNSET,
    archive_serial_number_lte: int | Unset = UNSET,
    checksum_icontains: str | Unset = UNSET,
    checksum_iendswith: str | Unset = UNSET,
    checksum_iexact: str | Unset = UNSET,
    checksum_istartswith: str | Unset = UNSET,
    content_icontains: str | Unset = UNSET,
    content_iendswith: str | Unset = UNSET,
    content_iexact: str | Unset = UNSET,
    content_istartswith: str | Unset = UNSET,
    correspondent_id: int | Unset = UNSET,
    correspondent_id_in: list[int] | Unset = UNSET,
    correspondent_id_none: int | Unset = UNSET,
    correspondent_isnull: bool | Unset = UNSET,
    correspondent_name_icontains: str | Unset = UNSET,
    correspondent_name_iendswith: str | Unset = UNSET,
    correspondent_name_iexact: str | Unset = UNSET,
    correspondent_name_istartswith: str | Unset = UNSET,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.date | Unset = UNSET,
    created_gte: datetime.date | Unset = UNSET,
    created_lt: datetime.date | Unset = UNSET,
    created_lte: datetime.date | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    custom_field_query: str | Unset = UNSET,
    custom_fields_icontains: str | Unset = UNSET,
    custom_fields_id_all: int | Unset = UNSET,
    custom_fields_id_in: int | Unset = UNSET,
    custom_fields_id_none: int | Unset = UNSET,
    document_type_id: int | Unset = UNSET,
    document_type_id_in: list[int] | Unset = UNSET,
    document_type_id_none: int | Unset = UNSET,
    document_type_isnull: bool | Unset = UNSET,
    document_type_name_icontains: str | Unset = UNSET,
    document_type_name_iendswith: str | Unset = UNSET,
    document_type_name_iexact: str | Unset = UNSET,
    document_type_name_istartswith: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
    has_custom_fields: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_in_inbox: bool | Unset = UNSET,
    is_tagged: bool | Unset = UNSET,
    mime_type: str | Unset = UNSET,
    modified_date_gt: datetime.date | Unset = UNSET,
    modified_date_gte: datetime.date | Unset = UNSET,
    modified_date_lt: datetime.date | Unset = UNSET,
    modified_date_lte: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_gt: datetime.datetime | Unset = UNSET,
    modified_gte: datetime.datetime | Unset = UNSET,
    modified_lt: datetime.datetime | Unset = UNSET,
    modified_lte: datetime.datetime | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    original_filename_icontains: str | Unset = UNSET,
    original_filename_iendswith: str | Unset = UNSET,
    original_filename_iexact: str | Unset = UNSET,
    original_filename_istartswith: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    owner_id_in: list[int] | Unset = UNSET,
    owner_id_none: int | Unset = UNSET,
    owner_isnull: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    query: str | Unset = UNSET,
    search: str | Unset = UNSET,
    shared_by_id: bool | Unset = UNSET,
    storage_path_id: int | Unset = UNSET,
    storage_path_id_in: list[int] | Unset = UNSET,
    storage_path_id_none: int | Unset = UNSET,
    storage_path_isnull: bool | Unset = UNSET,
    storage_path_name_icontains: str | Unset = UNSET,
    storage_path_name_iendswith: str | Unset = UNSET,
    storage_path_name_iexact: str | Unset = UNSET,
    storage_path_name_istartswith: str | Unset = UNSET,
    tags_id: int | Unset = UNSET,
    tags_id_all: int | Unset = UNSET,
    tags_id_in: int | Unset = UNSET,
    tags_id_none: int | Unset = UNSET,
    tags_name_icontains: str | Unset = UNSET,
    tags_name_iendswith: str | Unset = UNSET,
    tags_name_iexact: str | Unset = UNSET,
    tags_name_istartswith: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_content: str | Unset = UNSET,
) -> PaginatedDocumentList | None:
    """Document views including search

    Args:
        added_date_gt (datetime.date | Unset):
        added_date_gte (datetime.date | Unset):
        added_date_lt (datetime.date | Unset):
        added_date_lte (datetime.date | Unset):
        added_day (float | Unset):
        added_gt (datetime.datetime | Unset):
        added_gte (datetime.datetime | Unset):
        added_lt (datetime.datetime | Unset):
        added_lte (datetime.datetime | Unset):
        added_month (float | Unset):
        added_year (float | Unset):
        archive_serial_number (int | Unset):
        archive_serial_number_gt (int | Unset):
        archive_serial_number_gte (int | Unset):
        archive_serial_number_isnull (bool | Unset):
        archive_serial_number_lt (int | Unset):
        archive_serial_number_lte (int | Unset):
        checksum_icontains (str | Unset):
        checksum_iendswith (str | Unset):
        checksum_iexact (str | Unset):
        checksum_istartswith (str | Unset):
        content_icontains (str | Unset):
        content_iendswith (str | Unset):
        content_iexact (str | Unset):
        content_istartswith (str | Unset):
        correspondent_id (int | Unset):
        correspondent_id_in (list[int] | Unset):
        correspondent_id_none (int | Unset):
        correspondent_isnull (bool | Unset):
        correspondent_name_icontains (str | Unset):
        correspondent_name_iendswith (str | Unset):
        correspondent_name_iexact (str | Unset):
        correspondent_name_istartswith (str | Unset):
        created_date_gt (datetime.date | Unset):
        created_date_gte (datetime.date | Unset):
        created_date_lt (datetime.date | Unset):
        created_date_lte (datetime.date | Unset):
        created_day (float | Unset):
        created_gt (datetime.date | Unset):
        created_gte (datetime.date | Unset):
        created_lt (datetime.date | Unset):
        created_lte (datetime.date | Unset):
        created_month (float | Unset):
        created_year (float | Unset):
        custom_field_query (str | Unset):
        custom_fields_icontains (str | Unset):
        custom_fields_id_all (int | Unset):
        custom_fields_id_in (int | Unset):
        custom_fields_id_none (int | Unset):
        document_type_id (int | Unset):
        document_type_id_in (list[int] | Unset):
        document_type_id_none (int | Unset):
        document_type_isnull (bool | Unset):
        document_type_name_icontains (str | Unset):
        document_type_name_iendswith (str | Unset):
        document_type_name_iexact (str | Unset):
        document_type_name_istartswith (str | Unset):
        fields (list[str] | Unset):
        full_perms (bool | Unset):
        has_custom_fields (bool | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        is_in_inbox (bool | Unset):
        is_tagged (bool | Unset):
        mime_type (str | Unset):
        modified_date_gt (datetime.date | Unset):
        modified_date_gte (datetime.date | Unset):
        modified_date_lt (datetime.date | Unset):
        modified_date_lte (datetime.date | Unset):
        modified_day (float | Unset):
        modified_gt (datetime.datetime | Unset):
        modified_gte (datetime.datetime | Unset):
        modified_lt (datetime.datetime | Unset):
        modified_lte (datetime.datetime | Unset):
        modified_month (float | Unset):
        modified_year (float | Unset):
        ordering (str | Unset):
        original_filename_icontains (str | Unset):
        original_filename_iendswith (str | Unset):
        original_filename_iexact (str | Unset):
        original_filename_istartswith (str | Unset):
        owner_id (int | Unset):
        owner_id_in (list[int] | Unset):
        owner_id_none (int | Unset):
        owner_isnull (bool | Unset):
        page (int | Unset):
        page_size (int | Unset):
        query (str | Unset):
        search (str | Unset):
        shared_by_id (bool | Unset):
        storage_path_id (int | Unset):
        storage_path_id_in (list[int] | Unset):
        storage_path_id_none (int | Unset):
        storage_path_isnull (bool | Unset):
        storage_path_name_icontains (str | Unset):
        storage_path_name_iendswith (str | Unset):
        storage_path_name_iexact (str | Unset):
        storage_path_name_istartswith (str | Unset):
        tags_id (int | Unset):
        tags_id_all (int | Unset):
        tags_id_in (int | Unset):
        tags_id_none (int | Unset):
        tags_name_icontains (str | Unset):
        tags_name_iendswith (str | Unset):
        tags_name_iexact (str | Unset):
        tags_name_istartswith (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_istartswith (str | Unset):
        title_content (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDocumentList
    """

    return sync_detailed(
        client=client,
        added_date_gt=added_date_gt,
        added_date_gte=added_date_gte,
        added_date_lt=added_date_lt,
        added_date_lte=added_date_lte,
        added_day=added_day,
        added_gt=added_gt,
        added_gte=added_gte,
        added_lt=added_lt,
        added_lte=added_lte,
        added_month=added_month,
        added_year=added_year,
        archive_serial_number=archive_serial_number,
        archive_serial_number_gt=archive_serial_number_gt,
        archive_serial_number_gte=archive_serial_number_gte,
        archive_serial_number_isnull=archive_serial_number_isnull,
        archive_serial_number_lt=archive_serial_number_lt,
        archive_serial_number_lte=archive_serial_number_lte,
        checksum_icontains=checksum_icontains,
        checksum_iendswith=checksum_iendswith,
        checksum_iexact=checksum_iexact,
        checksum_istartswith=checksum_istartswith,
        content_icontains=content_icontains,
        content_iendswith=content_iendswith,
        content_iexact=content_iexact,
        content_istartswith=content_istartswith,
        correspondent_id=correspondent_id,
        correspondent_id_in=correspondent_id_in,
        correspondent_id_none=correspondent_id_none,
        correspondent_isnull=correspondent_isnull,
        correspondent_name_icontains=correspondent_name_icontains,
        correspondent_name_iendswith=correspondent_name_iendswith,
        correspondent_name_iexact=correspondent_name_iexact,
        correspondent_name_istartswith=correspondent_name_istartswith,
        created_date_gt=created_date_gt,
        created_date_gte=created_date_gte,
        created_date_lt=created_date_lt,
        created_date_lte=created_date_lte,
        created_day=created_day,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_month=created_month,
        created_year=created_year,
        custom_field_query=custom_field_query,
        custom_fields_icontains=custom_fields_icontains,
        custom_fields_id_all=custom_fields_id_all,
        custom_fields_id_in=custom_fields_id_in,
        custom_fields_id_none=custom_fields_id_none,
        document_type_id=document_type_id,
        document_type_id_in=document_type_id_in,
        document_type_id_none=document_type_id_none,
        document_type_isnull=document_type_isnull,
        document_type_name_icontains=document_type_name_icontains,
        document_type_name_iendswith=document_type_name_iendswith,
        document_type_name_iexact=document_type_name_iexact,
        document_type_name_istartswith=document_type_name_istartswith,
        fields=fields,
        full_perms=full_perms,
        has_custom_fields=has_custom_fields,
        id=id,
        id_in=id_in,
        is_in_inbox=is_in_inbox,
        is_tagged=is_tagged,
        mime_type=mime_type,
        modified_date_gt=modified_date_gt,
        modified_date_gte=modified_date_gte,
        modified_date_lt=modified_date_lt,
        modified_date_lte=modified_date_lte,
        modified_day=modified_day,
        modified_gt=modified_gt,
        modified_gte=modified_gte,
        modified_lt=modified_lt,
        modified_lte=modified_lte,
        modified_month=modified_month,
        modified_year=modified_year,
        ordering=ordering,
        original_filename_icontains=original_filename_icontains,
        original_filename_iendswith=original_filename_iendswith,
        original_filename_iexact=original_filename_iexact,
        original_filename_istartswith=original_filename_istartswith,
        owner_id=owner_id,
        owner_id_in=owner_id_in,
        owner_id_none=owner_id_none,
        owner_isnull=owner_isnull,
        page=page,
        page_size=page_size,
        query=query,
        search=search,
        shared_by_id=shared_by_id,
        storage_path_id=storage_path_id,
        storage_path_id_in=storage_path_id_in,
        storage_path_id_none=storage_path_id_none,
        storage_path_isnull=storage_path_isnull,
        storage_path_name_icontains=storage_path_name_icontains,
        storage_path_name_iendswith=storage_path_name_iendswith,
        storage_path_name_iexact=storage_path_name_iexact,
        storage_path_name_istartswith=storage_path_name_istartswith,
        tags_id=tags_id,
        tags_id_all=tags_id_all,
        tags_id_in=tags_id_in,
        tags_id_none=tags_id_none,
        tags_name_icontains=tags_name_icontains,
        tags_name_iendswith=tags_name_iendswith,
        tags_name_iexact=tags_name_iexact,
        tags_name_istartswith=tags_name_istartswith,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_istartswith=title_istartswith,
        title_content=title_content,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    added_date_gt: datetime.date | Unset = UNSET,
    added_date_gte: datetime.date | Unset = UNSET,
    added_date_lt: datetime.date | Unset = UNSET,
    added_date_lte: datetime.date | Unset = UNSET,
    added_day: float | Unset = UNSET,
    added_gt: datetime.datetime | Unset = UNSET,
    added_gte: datetime.datetime | Unset = UNSET,
    added_lt: datetime.datetime | Unset = UNSET,
    added_lte: datetime.datetime | Unset = UNSET,
    added_month: float | Unset = UNSET,
    added_year: float | Unset = UNSET,
    archive_serial_number: int | Unset = UNSET,
    archive_serial_number_gt: int | Unset = UNSET,
    archive_serial_number_gte: int | Unset = UNSET,
    archive_serial_number_isnull: bool | Unset = UNSET,
    archive_serial_number_lt: int | Unset = UNSET,
    archive_serial_number_lte: int | Unset = UNSET,
    checksum_icontains: str | Unset = UNSET,
    checksum_iendswith: str | Unset = UNSET,
    checksum_iexact: str | Unset = UNSET,
    checksum_istartswith: str | Unset = UNSET,
    content_icontains: str | Unset = UNSET,
    content_iendswith: str | Unset = UNSET,
    content_iexact: str | Unset = UNSET,
    content_istartswith: str | Unset = UNSET,
    correspondent_id: int | Unset = UNSET,
    correspondent_id_in: list[int] | Unset = UNSET,
    correspondent_id_none: int | Unset = UNSET,
    correspondent_isnull: bool | Unset = UNSET,
    correspondent_name_icontains: str | Unset = UNSET,
    correspondent_name_iendswith: str | Unset = UNSET,
    correspondent_name_iexact: str | Unset = UNSET,
    correspondent_name_istartswith: str | Unset = UNSET,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.date | Unset = UNSET,
    created_gte: datetime.date | Unset = UNSET,
    created_lt: datetime.date | Unset = UNSET,
    created_lte: datetime.date | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    custom_field_query: str | Unset = UNSET,
    custom_fields_icontains: str | Unset = UNSET,
    custom_fields_id_all: int | Unset = UNSET,
    custom_fields_id_in: int | Unset = UNSET,
    custom_fields_id_none: int | Unset = UNSET,
    document_type_id: int | Unset = UNSET,
    document_type_id_in: list[int] | Unset = UNSET,
    document_type_id_none: int | Unset = UNSET,
    document_type_isnull: bool | Unset = UNSET,
    document_type_name_icontains: str | Unset = UNSET,
    document_type_name_iendswith: str | Unset = UNSET,
    document_type_name_iexact: str | Unset = UNSET,
    document_type_name_istartswith: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
    has_custom_fields: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_in_inbox: bool | Unset = UNSET,
    is_tagged: bool | Unset = UNSET,
    mime_type: str | Unset = UNSET,
    modified_date_gt: datetime.date | Unset = UNSET,
    modified_date_gte: datetime.date | Unset = UNSET,
    modified_date_lt: datetime.date | Unset = UNSET,
    modified_date_lte: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_gt: datetime.datetime | Unset = UNSET,
    modified_gte: datetime.datetime | Unset = UNSET,
    modified_lt: datetime.datetime | Unset = UNSET,
    modified_lte: datetime.datetime | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    original_filename_icontains: str | Unset = UNSET,
    original_filename_iendswith: str | Unset = UNSET,
    original_filename_iexact: str | Unset = UNSET,
    original_filename_istartswith: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    owner_id_in: list[int] | Unset = UNSET,
    owner_id_none: int | Unset = UNSET,
    owner_isnull: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    query: str | Unset = UNSET,
    search: str | Unset = UNSET,
    shared_by_id: bool | Unset = UNSET,
    storage_path_id: int | Unset = UNSET,
    storage_path_id_in: list[int] | Unset = UNSET,
    storage_path_id_none: int | Unset = UNSET,
    storage_path_isnull: bool | Unset = UNSET,
    storage_path_name_icontains: str | Unset = UNSET,
    storage_path_name_iendswith: str | Unset = UNSET,
    storage_path_name_iexact: str | Unset = UNSET,
    storage_path_name_istartswith: str | Unset = UNSET,
    tags_id: int | Unset = UNSET,
    tags_id_all: int | Unset = UNSET,
    tags_id_in: int | Unset = UNSET,
    tags_id_none: int | Unset = UNSET,
    tags_name_icontains: str | Unset = UNSET,
    tags_name_iendswith: str | Unset = UNSET,
    tags_name_iexact: str | Unset = UNSET,
    tags_name_istartswith: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_content: str | Unset = UNSET,
) -> Response[PaginatedDocumentList]:
    """Document views including search

    Args:
        added_date_gt (datetime.date | Unset):
        added_date_gte (datetime.date | Unset):
        added_date_lt (datetime.date | Unset):
        added_date_lte (datetime.date | Unset):
        added_day (float | Unset):
        added_gt (datetime.datetime | Unset):
        added_gte (datetime.datetime | Unset):
        added_lt (datetime.datetime | Unset):
        added_lte (datetime.datetime | Unset):
        added_month (float | Unset):
        added_year (float | Unset):
        archive_serial_number (int | Unset):
        archive_serial_number_gt (int | Unset):
        archive_serial_number_gte (int | Unset):
        archive_serial_number_isnull (bool | Unset):
        archive_serial_number_lt (int | Unset):
        archive_serial_number_lte (int | Unset):
        checksum_icontains (str | Unset):
        checksum_iendswith (str | Unset):
        checksum_iexact (str | Unset):
        checksum_istartswith (str | Unset):
        content_icontains (str | Unset):
        content_iendswith (str | Unset):
        content_iexact (str | Unset):
        content_istartswith (str | Unset):
        correspondent_id (int | Unset):
        correspondent_id_in (list[int] | Unset):
        correspondent_id_none (int | Unset):
        correspondent_isnull (bool | Unset):
        correspondent_name_icontains (str | Unset):
        correspondent_name_iendswith (str | Unset):
        correspondent_name_iexact (str | Unset):
        correspondent_name_istartswith (str | Unset):
        created_date_gt (datetime.date | Unset):
        created_date_gte (datetime.date | Unset):
        created_date_lt (datetime.date | Unset):
        created_date_lte (datetime.date | Unset):
        created_day (float | Unset):
        created_gt (datetime.date | Unset):
        created_gte (datetime.date | Unset):
        created_lt (datetime.date | Unset):
        created_lte (datetime.date | Unset):
        created_month (float | Unset):
        created_year (float | Unset):
        custom_field_query (str | Unset):
        custom_fields_icontains (str | Unset):
        custom_fields_id_all (int | Unset):
        custom_fields_id_in (int | Unset):
        custom_fields_id_none (int | Unset):
        document_type_id (int | Unset):
        document_type_id_in (list[int] | Unset):
        document_type_id_none (int | Unset):
        document_type_isnull (bool | Unset):
        document_type_name_icontains (str | Unset):
        document_type_name_iendswith (str | Unset):
        document_type_name_iexact (str | Unset):
        document_type_name_istartswith (str | Unset):
        fields (list[str] | Unset):
        full_perms (bool | Unset):
        has_custom_fields (bool | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        is_in_inbox (bool | Unset):
        is_tagged (bool | Unset):
        mime_type (str | Unset):
        modified_date_gt (datetime.date | Unset):
        modified_date_gte (datetime.date | Unset):
        modified_date_lt (datetime.date | Unset):
        modified_date_lte (datetime.date | Unset):
        modified_day (float | Unset):
        modified_gt (datetime.datetime | Unset):
        modified_gte (datetime.datetime | Unset):
        modified_lt (datetime.datetime | Unset):
        modified_lte (datetime.datetime | Unset):
        modified_month (float | Unset):
        modified_year (float | Unset):
        ordering (str | Unset):
        original_filename_icontains (str | Unset):
        original_filename_iendswith (str | Unset):
        original_filename_iexact (str | Unset):
        original_filename_istartswith (str | Unset):
        owner_id (int | Unset):
        owner_id_in (list[int] | Unset):
        owner_id_none (int | Unset):
        owner_isnull (bool | Unset):
        page (int | Unset):
        page_size (int | Unset):
        query (str | Unset):
        search (str | Unset):
        shared_by_id (bool | Unset):
        storage_path_id (int | Unset):
        storage_path_id_in (list[int] | Unset):
        storage_path_id_none (int | Unset):
        storage_path_isnull (bool | Unset):
        storage_path_name_icontains (str | Unset):
        storage_path_name_iendswith (str | Unset):
        storage_path_name_iexact (str | Unset):
        storage_path_name_istartswith (str | Unset):
        tags_id (int | Unset):
        tags_id_all (int | Unset):
        tags_id_in (int | Unset):
        tags_id_none (int | Unset):
        tags_name_icontains (str | Unset):
        tags_name_iendswith (str | Unset):
        tags_name_iexact (str | Unset):
        tags_name_istartswith (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_istartswith (str | Unset):
        title_content (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDocumentList]
    """

    kwargs = _get_kwargs(
        added_date_gt=added_date_gt,
        added_date_gte=added_date_gte,
        added_date_lt=added_date_lt,
        added_date_lte=added_date_lte,
        added_day=added_day,
        added_gt=added_gt,
        added_gte=added_gte,
        added_lt=added_lt,
        added_lte=added_lte,
        added_month=added_month,
        added_year=added_year,
        archive_serial_number=archive_serial_number,
        archive_serial_number_gt=archive_serial_number_gt,
        archive_serial_number_gte=archive_serial_number_gte,
        archive_serial_number_isnull=archive_serial_number_isnull,
        archive_serial_number_lt=archive_serial_number_lt,
        archive_serial_number_lte=archive_serial_number_lte,
        checksum_icontains=checksum_icontains,
        checksum_iendswith=checksum_iendswith,
        checksum_iexact=checksum_iexact,
        checksum_istartswith=checksum_istartswith,
        content_icontains=content_icontains,
        content_iendswith=content_iendswith,
        content_iexact=content_iexact,
        content_istartswith=content_istartswith,
        correspondent_id=correspondent_id,
        correspondent_id_in=correspondent_id_in,
        correspondent_id_none=correspondent_id_none,
        correspondent_isnull=correspondent_isnull,
        correspondent_name_icontains=correspondent_name_icontains,
        correspondent_name_iendswith=correspondent_name_iendswith,
        correspondent_name_iexact=correspondent_name_iexact,
        correspondent_name_istartswith=correspondent_name_istartswith,
        created_date_gt=created_date_gt,
        created_date_gte=created_date_gte,
        created_date_lt=created_date_lt,
        created_date_lte=created_date_lte,
        created_day=created_day,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_month=created_month,
        created_year=created_year,
        custom_field_query=custom_field_query,
        custom_fields_icontains=custom_fields_icontains,
        custom_fields_id_all=custom_fields_id_all,
        custom_fields_id_in=custom_fields_id_in,
        custom_fields_id_none=custom_fields_id_none,
        document_type_id=document_type_id,
        document_type_id_in=document_type_id_in,
        document_type_id_none=document_type_id_none,
        document_type_isnull=document_type_isnull,
        document_type_name_icontains=document_type_name_icontains,
        document_type_name_iendswith=document_type_name_iendswith,
        document_type_name_iexact=document_type_name_iexact,
        document_type_name_istartswith=document_type_name_istartswith,
        fields=fields,
        full_perms=full_perms,
        has_custom_fields=has_custom_fields,
        id=id,
        id_in=id_in,
        is_in_inbox=is_in_inbox,
        is_tagged=is_tagged,
        mime_type=mime_type,
        modified_date_gt=modified_date_gt,
        modified_date_gte=modified_date_gte,
        modified_date_lt=modified_date_lt,
        modified_date_lte=modified_date_lte,
        modified_day=modified_day,
        modified_gt=modified_gt,
        modified_gte=modified_gte,
        modified_lt=modified_lt,
        modified_lte=modified_lte,
        modified_month=modified_month,
        modified_year=modified_year,
        ordering=ordering,
        original_filename_icontains=original_filename_icontains,
        original_filename_iendswith=original_filename_iendswith,
        original_filename_iexact=original_filename_iexact,
        original_filename_istartswith=original_filename_istartswith,
        owner_id=owner_id,
        owner_id_in=owner_id_in,
        owner_id_none=owner_id_none,
        owner_isnull=owner_isnull,
        page=page,
        page_size=page_size,
        query=query,
        search=search,
        shared_by_id=shared_by_id,
        storage_path_id=storage_path_id,
        storage_path_id_in=storage_path_id_in,
        storage_path_id_none=storage_path_id_none,
        storage_path_isnull=storage_path_isnull,
        storage_path_name_icontains=storage_path_name_icontains,
        storage_path_name_iendswith=storage_path_name_iendswith,
        storage_path_name_iexact=storage_path_name_iexact,
        storage_path_name_istartswith=storage_path_name_istartswith,
        tags_id=tags_id,
        tags_id_all=tags_id_all,
        tags_id_in=tags_id_in,
        tags_id_none=tags_id_none,
        tags_name_icontains=tags_name_icontains,
        tags_name_iendswith=tags_name_iendswith,
        tags_name_iexact=tags_name_iexact,
        tags_name_istartswith=tags_name_istartswith,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_istartswith=title_istartswith,
        title_content=title_content,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    added_date_gt: datetime.date | Unset = UNSET,
    added_date_gte: datetime.date | Unset = UNSET,
    added_date_lt: datetime.date | Unset = UNSET,
    added_date_lte: datetime.date | Unset = UNSET,
    added_day: float | Unset = UNSET,
    added_gt: datetime.datetime | Unset = UNSET,
    added_gte: datetime.datetime | Unset = UNSET,
    added_lt: datetime.datetime | Unset = UNSET,
    added_lte: datetime.datetime | Unset = UNSET,
    added_month: float | Unset = UNSET,
    added_year: float | Unset = UNSET,
    archive_serial_number: int | Unset = UNSET,
    archive_serial_number_gt: int | Unset = UNSET,
    archive_serial_number_gte: int | Unset = UNSET,
    archive_serial_number_isnull: bool | Unset = UNSET,
    archive_serial_number_lt: int | Unset = UNSET,
    archive_serial_number_lte: int | Unset = UNSET,
    checksum_icontains: str | Unset = UNSET,
    checksum_iendswith: str | Unset = UNSET,
    checksum_iexact: str | Unset = UNSET,
    checksum_istartswith: str | Unset = UNSET,
    content_icontains: str | Unset = UNSET,
    content_iendswith: str | Unset = UNSET,
    content_iexact: str | Unset = UNSET,
    content_istartswith: str | Unset = UNSET,
    correspondent_id: int | Unset = UNSET,
    correspondent_id_in: list[int] | Unset = UNSET,
    correspondent_id_none: int | Unset = UNSET,
    correspondent_isnull: bool | Unset = UNSET,
    correspondent_name_icontains: str | Unset = UNSET,
    correspondent_name_iendswith: str | Unset = UNSET,
    correspondent_name_iexact: str | Unset = UNSET,
    correspondent_name_istartswith: str | Unset = UNSET,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.date | Unset = UNSET,
    created_gte: datetime.date | Unset = UNSET,
    created_lt: datetime.date | Unset = UNSET,
    created_lte: datetime.date | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    custom_field_query: str | Unset = UNSET,
    custom_fields_icontains: str | Unset = UNSET,
    custom_fields_id_all: int | Unset = UNSET,
    custom_fields_id_in: int | Unset = UNSET,
    custom_fields_id_none: int | Unset = UNSET,
    document_type_id: int | Unset = UNSET,
    document_type_id_in: list[int] | Unset = UNSET,
    document_type_id_none: int | Unset = UNSET,
    document_type_isnull: bool | Unset = UNSET,
    document_type_name_icontains: str | Unset = UNSET,
    document_type_name_iendswith: str | Unset = UNSET,
    document_type_name_iexact: str | Unset = UNSET,
    document_type_name_istartswith: str | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
    has_custom_fields: bool | Unset = UNSET,
    id: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    is_in_inbox: bool | Unset = UNSET,
    is_tagged: bool | Unset = UNSET,
    mime_type: str | Unset = UNSET,
    modified_date_gt: datetime.date | Unset = UNSET,
    modified_date_gte: datetime.date | Unset = UNSET,
    modified_date_lt: datetime.date | Unset = UNSET,
    modified_date_lte: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_gt: datetime.datetime | Unset = UNSET,
    modified_gte: datetime.datetime | Unset = UNSET,
    modified_lt: datetime.datetime | Unset = UNSET,
    modified_lte: datetime.datetime | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    original_filename_icontains: str | Unset = UNSET,
    original_filename_iendswith: str | Unset = UNSET,
    original_filename_iexact: str | Unset = UNSET,
    original_filename_istartswith: str | Unset = UNSET,
    owner_id: int | Unset = UNSET,
    owner_id_in: list[int] | Unset = UNSET,
    owner_id_none: int | Unset = UNSET,
    owner_isnull: bool | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    query: str | Unset = UNSET,
    search: str | Unset = UNSET,
    shared_by_id: bool | Unset = UNSET,
    storage_path_id: int | Unset = UNSET,
    storage_path_id_in: list[int] | Unset = UNSET,
    storage_path_id_none: int | Unset = UNSET,
    storage_path_isnull: bool | Unset = UNSET,
    storage_path_name_icontains: str | Unset = UNSET,
    storage_path_name_iendswith: str | Unset = UNSET,
    storage_path_name_iexact: str | Unset = UNSET,
    storage_path_name_istartswith: str | Unset = UNSET,
    tags_id: int | Unset = UNSET,
    tags_id_all: int | Unset = UNSET,
    tags_id_in: int | Unset = UNSET,
    tags_id_none: int | Unset = UNSET,
    tags_name_icontains: str | Unset = UNSET,
    tags_name_iendswith: str | Unset = UNSET,
    tags_name_iexact: str | Unset = UNSET,
    tags_name_istartswith: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_content: str | Unset = UNSET,
) -> PaginatedDocumentList | None:
    """Document views including search

    Args:
        added_date_gt (datetime.date | Unset):
        added_date_gte (datetime.date | Unset):
        added_date_lt (datetime.date | Unset):
        added_date_lte (datetime.date | Unset):
        added_day (float | Unset):
        added_gt (datetime.datetime | Unset):
        added_gte (datetime.datetime | Unset):
        added_lt (datetime.datetime | Unset):
        added_lte (datetime.datetime | Unset):
        added_month (float | Unset):
        added_year (float | Unset):
        archive_serial_number (int | Unset):
        archive_serial_number_gt (int | Unset):
        archive_serial_number_gte (int | Unset):
        archive_serial_number_isnull (bool | Unset):
        archive_serial_number_lt (int | Unset):
        archive_serial_number_lte (int | Unset):
        checksum_icontains (str | Unset):
        checksum_iendswith (str | Unset):
        checksum_iexact (str | Unset):
        checksum_istartswith (str | Unset):
        content_icontains (str | Unset):
        content_iendswith (str | Unset):
        content_iexact (str | Unset):
        content_istartswith (str | Unset):
        correspondent_id (int | Unset):
        correspondent_id_in (list[int] | Unset):
        correspondent_id_none (int | Unset):
        correspondent_isnull (bool | Unset):
        correspondent_name_icontains (str | Unset):
        correspondent_name_iendswith (str | Unset):
        correspondent_name_iexact (str | Unset):
        correspondent_name_istartswith (str | Unset):
        created_date_gt (datetime.date | Unset):
        created_date_gte (datetime.date | Unset):
        created_date_lt (datetime.date | Unset):
        created_date_lte (datetime.date | Unset):
        created_day (float | Unset):
        created_gt (datetime.date | Unset):
        created_gte (datetime.date | Unset):
        created_lt (datetime.date | Unset):
        created_lte (datetime.date | Unset):
        created_month (float | Unset):
        created_year (float | Unset):
        custom_field_query (str | Unset):
        custom_fields_icontains (str | Unset):
        custom_fields_id_all (int | Unset):
        custom_fields_id_in (int | Unset):
        custom_fields_id_none (int | Unset):
        document_type_id (int | Unset):
        document_type_id_in (list[int] | Unset):
        document_type_id_none (int | Unset):
        document_type_isnull (bool | Unset):
        document_type_name_icontains (str | Unset):
        document_type_name_iendswith (str | Unset):
        document_type_name_iexact (str | Unset):
        document_type_name_istartswith (str | Unset):
        fields (list[str] | Unset):
        full_perms (bool | Unset):
        has_custom_fields (bool | Unset):
        id (int | Unset):
        id_in (list[int] | Unset):
        is_in_inbox (bool | Unset):
        is_tagged (bool | Unset):
        mime_type (str | Unset):
        modified_date_gt (datetime.date | Unset):
        modified_date_gte (datetime.date | Unset):
        modified_date_lt (datetime.date | Unset):
        modified_date_lte (datetime.date | Unset):
        modified_day (float | Unset):
        modified_gt (datetime.datetime | Unset):
        modified_gte (datetime.datetime | Unset):
        modified_lt (datetime.datetime | Unset):
        modified_lte (datetime.datetime | Unset):
        modified_month (float | Unset):
        modified_year (float | Unset):
        ordering (str | Unset):
        original_filename_icontains (str | Unset):
        original_filename_iendswith (str | Unset):
        original_filename_iexact (str | Unset):
        original_filename_istartswith (str | Unset):
        owner_id (int | Unset):
        owner_id_in (list[int] | Unset):
        owner_id_none (int | Unset):
        owner_isnull (bool | Unset):
        page (int | Unset):
        page_size (int | Unset):
        query (str | Unset):
        search (str | Unset):
        shared_by_id (bool | Unset):
        storage_path_id (int | Unset):
        storage_path_id_in (list[int] | Unset):
        storage_path_id_none (int | Unset):
        storage_path_isnull (bool | Unset):
        storage_path_name_icontains (str | Unset):
        storage_path_name_iendswith (str | Unset):
        storage_path_name_iexact (str | Unset):
        storage_path_name_istartswith (str | Unset):
        tags_id (int | Unset):
        tags_id_all (int | Unset):
        tags_id_in (int | Unset):
        tags_id_none (int | Unset):
        tags_name_icontains (str | Unset):
        tags_name_iendswith (str | Unset):
        tags_name_iexact (str | Unset):
        tags_name_istartswith (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_istartswith (str | Unset):
        title_content (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDocumentList
    """

    return (
        await asyncio_detailed(
            client=client,
            added_date_gt=added_date_gt,
            added_date_gte=added_date_gte,
            added_date_lt=added_date_lt,
            added_date_lte=added_date_lte,
            added_day=added_day,
            added_gt=added_gt,
            added_gte=added_gte,
            added_lt=added_lt,
            added_lte=added_lte,
            added_month=added_month,
            added_year=added_year,
            archive_serial_number=archive_serial_number,
            archive_serial_number_gt=archive_serial_number_gt,
            archive_serial_number_gte=archive_serial_number_gte,
            archive_serial_number_isnull=archive_serial_number_isnull,
            archive_serial_number_lt=archive_serial_number_lt,
            archive_serial_number_lte=archive_serial_number_lte,
            checksum_icontains=checksum_icontains,
            checksum_iendswith=checksum_iendswith,
            checksum_iexact=checksum_iexact,
            checksum_istartswith=checksum_istartswith,
            content_icontains=content_icontains,
            content_iendswith=content_iendswith,
            content_iexact=content_iexact,
            content_istartswith=content_istartswith,
            correspondent_id=correspondent_id,
            correspondent_id_in=correspondent_id_in,
            correspondent_id_none=correspondent_id_none,
            correspondent_isnull=correspondent_isnull,
            correspondent_name_icontains=correspondent_name_icontains,
            correspondent_name_iendswith=correspondent_name_iendswith,
            correspondent_name_iexact=correspondent_name_iexact,
            correspondent_name_istartswith=correspondent_name_istartswith,
            created_date_gt=created_date_gt,
            created_date_gte=created_date_gte,
            created_date_lt=created_date_lt,
            created_date_lte=created_date_lte,
            created_day=created_day,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_month=created_month,
            created_year=created_year,
            custom_field_query=custom_field_query,
            custom_fields_icontains=custom_fields_icontains,
            custom_fields_id_all=custom_fields_id_all,
            custom_fields_id_in=custom_fields_id_in,
            custom_fields_id_none=custom_fields_id_none,
            document_type_id=document_type_id,
            document_type_id_in=document_type_id_in,
            document_type_id_none=document_type_id_none,
            document_type_isnull=document_type_isnull,
            document_type_name_icontains=document_type_name_icontains,
            document_type_name_iendswith=document_type_name_iendswith,
            document_type_name_iexact=document_type_name_iexact,
            document_type_name_istartswith=document_type_name_istartswith,
            fields=fields,
            full_perms=full_perms,
            has_custom_fields=has_custom_fields,
            id=id,
            id_in=id_in,
            is_in_inbox=is_in_inbox,
            is_tagged=is_tagged,
            mime_type=mime_type,
            modified_date_gt=modified_date_gt,
            modified_date_gte=modified_date_gte,
            modified_date_lt=modified_date_lt,
            modified_date_lte=modified_date_lte,
            modified_day=modified_day,
            modified_gt=modified_gt,
            modified_gte=modified_gte,
            modified_lt=modified_lt,
            modified_lte=modified_lte,
            modified_month=modified_month,
            modified_year=modified_year,
            ordering=ordering,
            original_filename_icontains=original_filename_icontains,
            original_filename_iendswith=original_filename_iendswith,
            original_filename_iexact=original_filename_iexact,
            original_filename_istartswith=original_filename_istartswith,
            owner_id=owner_id,
            owner_id_in=owner_id_in,
            owner_id_none=owner_id_none,
            owner_isnull=owner_isnull,
            page=page,
            page_size=page_size,
            query=query,
            search=search,
            shared_by_id=shared_by_id,
            storage_path_id=storage_path_id,
            storage_path_id_in=storage_path_id_in,
            storage_path_id_none=storage_path_id_none,
            storage_path_isnull=storage_path_isnull,
            storage_path_name_icontains=storage_path_name_icontains,
            storage_path_name_iendswith=storage_path_name_iendswith,
            storage_path_name_iexact=storage_path_name_iexact,
            storage_path_name_istartswith=storage_path_name_istartswith,
            tags_id=tags_id,
            tags_id_all=tags_id_all,
            tags_id_in=tags_id_in,
            tags_id_none=tags_id_none,
            tags_name_icontains=tags_name_icontains,
            tags_name_iendswith=tags_name_iendswith,
            tags_name_iexact=tags_name_iexact,
            tags_name_istartswith=tags_name_istartswith,
            title_icontains=title_icontains,
            title_iendswith=title_iendswith,
            title_iexact=title_iexact,
            title_istartswith=title_istartswith,
            title_content=title_content,
        )
    ).parsed
