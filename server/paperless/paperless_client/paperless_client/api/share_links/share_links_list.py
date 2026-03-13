import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_share_link_list import PaginatedShareLinkList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    expiration_date_gt: datetime.date | Unset = UNSET,
    expiration_date_gte: datetime.date | Unset = UNSET,
    expiration_date_lt: datetime.date | Unset = UNSET,
    expiration_date_lte: datetime.date | Unset = UNSET,
    expiration_day: float | Unset = UNSET,
    expiration_gt: datetime.datetime | Unset = UNSET,
    expiration_gte: datetime.datetime | Unset = UNSET,
    expiration_lt: datetime.datetime | Unset = UNSET,
    expiration_lte: datetime.datetime | Unset = UNSET,
    expiration_month: float | Unset = UNSET,
    expiration_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    json_expiration_date_gt: str | Unset = UNSET
    if not isinstance(expiration_date_gt, Unset):
        json_expiration_date_gt = expiration_date_gt.isoformat()
    params["expiration__date__gt"] = json_expiration_date_gt

    json_expiration_date_gte: str | Unset = UNSET
    if not isinstance(expiration_date_gte, Unset):
        json_expiration_date_gte = expiration_date_gte.isoformat()
    params["expiration__date__gte"] = json_expiration_date_gte

    json_expiration_date_lt: str | Unset = UNSET
    if not isinstance(expiration_date_lt, Unset):
        json_expiration_date_lt = expiration_date_lt.isoformat()
    params["expiration__date__lt"] = json_expiration_date_lt

    json_expiration_date_lte: str | Unset = UNSET
    if not isinstance(expiration_date_lte, Unset):
        json_expiration_date_lte = expiration_date_lte.isoformat()
    params["expiration__date__lte"] = json_expiration_date_lte

    params["expiration__day"] = expiration_day

    json_expiration_gt: str | Unset = UNSET
    if not isinstance(expiration_gt, Unset):
        json_expiration_gt = expiration_gt.isoformat()
    params["expiration__gt"] = json_expiration_gt

    json_expiration_gte: str | Unset = UNSET
    if not isinstance(expiration_gte, Unset):
        json_expiration_gte = expiration_gte.isoformat()
    params["expiration__gte"] = json_expiration_gte

    json_expiration_lt: str | Unset = UNSET
    if not isinstance(expiration_lt, Unset):
        json_expiration_lt = expiration_lt.isoformat()
    params["expiration__lt"] = json_expiration_lt

    json_expiration_lte: str | Unset = UNSET
    if not isinstance(expiration_lte, Unset):
        json_expiration_lte = expiration_lte.isoformat()
    params["expiration__lte"] = json_expiration_lte

    params["expiration__month"] = expiration_month

    params["expiration__year"] = expiration_year

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/share_links/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedShareLinkList | None:
    if response.status_code == 200:
        response_200 = PaginatedShareLinkList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedShareLinkList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    expiration_date_gt: datetime.date | Unset = UNSET,
    expiration_date_gte: datetime.date | Unset = UNSET,
    expiration_date_lt: datetime.date | Unset = UNSET,
    expiration_date_lte: datetime.date | Unset = UNSET,
    expiration_day: float | Unset = UNSET,
    expiration_gt: datetime.datetime | Unset = UNSET,
    expiration_gte: datetime.datetime | Unset = UNSET,
    expiration_lt: datetime.datetime | Unset = UNSET,
    expiration_lte: datetime.datetime | Unset = UNSET,
    expiration_month: float | Unset = UNSET,
    expiration_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[PaginatedShareLinkList]:
    """
    Args:
        created_date_gt (datetime.date | Unset):
        created_date_gte (datetime.date | Unset):
        created_date_lt (datetime.date | Unset):
        created_date_lte (datetime.date | Unset):
        created_day (float | Unset):
        created_gt (datetime.datetime | Unset):
        created_gte (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        created_lte (datetime.datetime | Unset):
        created_month (float | Unset):
        created_year (float | Unset):
        expiration_date_gt (datetime.date | Unset):
        expiration_date_gte (datetime.date | Unset):
        expiration_date_lt (datetime.date | Unset):
        expiration_date_lte (datetime.date | Unset):
        expiration_day (float | Unset):
        expiration_gt (datetime.datetime | Unset):
        expiration_gte (datetime.datetime | Unset):
        expiration_lt (datetime.datetime | Unset):
        expiration_lte (datetime.datetime | Unset):
        expiration_month (float | Unset):
        expiration_year (float | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedShareLinkList]
    """

    kwargs = _get_kwargs(
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
        expiration_date_gt=expiration_date_gt,
        expiration_date_gte=expiration_date_gte,
        expiration_date_lt=expiration_date_lt,
        expiration_date_lte=expiration_date_lte,
        expiration_day=expiration_day,
        expiration_gt=expiration_gt,
        expiration_gte=expiration_gte,
        expiration_lt=expiration_lt,
        expiration_lte=expiration_lte,
        expiration_month=expiration_month,
        expiration_year=expiration_year,
        ordering=ordering,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    expiration_date_gt: datetime.date | Unset = UNSET,
    expiration_date_gte: datetime.date | Unset = UNSET,
    expiration_date_lt: datetime.date | Unset = UNSET,
    expiration_date_lte: datetime.date | Unset = UNSET,
    expiration_day: float | Unset = UNSET,
    expiration_gt: datetime.datetime | Unset = UNSET,
    expiration_gte: datetime.datetime | Unset = UNSET,
    expiration_lt: datetime.datetime | Unset = UNSET,
    expiration_lte: datetime.datetime | Unset = UNSET,
    expiration_month: float | Unset = UNSET,
    expiration_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> PaginatedShareLinkList | None:
    """
    Args:
        created_date_gt (datetime.date | Unset):
        created_date_gte (datetime.date | Unset):
        created_date_lt (datetime.date | Unset):
        created_date_lte (datetime.date | Unset):
        created_day (float | Unset):
        created_gt (datetime.datetime | Unset):
        created_gte (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        created_lte (datetime.datetime | Unset):
        created_month (float | Unset):
        created_year (float | Unset):
        expiration_date_gt (datetime.date | Unset):
        expiration_date_gte (datetime.date | Unset):
        expiration_date_lt (datetime.date | Unset):
        expiration_date_lte (datetime.date | Unset):
        expiration_day (float | Unset):
        expiration_gt (datetime.datetime | Unset):
        expiration_gte (datetime.datetime | Unset):
        expiration_lt (datetime.datetime | Unset):
        expiration_lte (datetime.datetime | Unset):
        expiration_month (float | Unset):
        expiration_year (float | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedShareLinkList
    """

    return sync_detailed(
        client=client,
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
        expiration_date_gt=expiration_date_gt,
        expiration_date_gte=expiration_date_gte,
        expiration_date_lt=expiration_date_lt,
        expiration_date_lte=expiration_date_lte,
        expiration_day=expiration_day,
        expiration_gt=expiration_gt,
        expiration_gte=expiration_gte,
        expiration_lt=expiration_lt,
        expiration_lte=expiration_lte,
        expiration_month=expiration_month,
        expiration_year=expiration_year,
        ordering=ordering,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    expiration_date_gt: datetime.date | Unset = UNSET,
    expiration_date_gte: datetime.date | Unset = UNSET,
    expiration_date_lt: datetime.date | Unset = UNSET,
    expiration_date_lte: datetime.date | Unset = UNSET,
    expiration_day: float | Unset = UNSET,
    expiration_gt: datetime.datetime | Unset = UNSET,
    expiration_gte: datetime.datetime | Unset = UNSET,
    expiration_lt: datetime.datetime | Unset = UNSET,
    expiration_lte: datetime.datetime | Unset = UNSET,
    expiration_month: float | Unset = UNSET,
    expiration_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[PaginatedShareLinkList]:
    """
    Args:
        created_date_gt (datetime.date | Unset):
        created_date_gte (datetime.date | Unset):
        created_date_lt (datetime.date | Unset):
        created_date_lte (datetime.date | Unset):
        created_day (float | Unset):
        created_gt (datetime.datetime | Unset):
        created_gte (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        created_lte (datetime.datetime | Unset):
        created_month (float | Unset):
        created_year (float | Unset):
        expiration_date_gt (datetime.date | Unset):
        expiration_date_gte (datetime.date | Unset):
        expiration_date_lt (datetime.date | Unset):
        expiration_date_lte (datetime.date | Unset):
        expiration_day (float | Unset):
        expiration_gt (datetime.datetime | Unset):
        expiration_gte (datetime.datetime | Unset):
        expiration_lt (datetime.datetime | Unset):
        expiration_lte (datetime.datetime | Unset):
        expiration_month (float | Unset):
        expiration_year (float | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedShareLinkList]
    """

    kwargs = _get_kwargs(
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
        expiration_date_gt=expiration_date_gt,
        expiration_date_gte=expiration_date_gte,
        expiration_date_lt=expiration_date_lt,
        expiration_date_lte=expiration_date_lte,
        expiration_day=expiration_day,
        expiration_gt=expiration_gt,
        expiration_gte=expiration_gte,
        expiration_lt=expiration_lt,
        expiration_lte=expiration_lte,
        expiration_month=expiration_month,
        expiration_year=expiration_year,
        ordering=ordering,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created_date_gt: datetime.date | Unset = UNSET,
    created_date_gte: datetime.date | Unset = UNSET,
    created_date_lt: datetime.date | Unset = UNSET,
    created_date_lte: datetime.date | Unset = UNSET,
    created_day: float | Unset = UNSET,
    created_gt: datetime.datetime | Unset = UNSET,
    created_gte: datetime.datetime | Unset = UNSET,
    created_lt: datetime.datetime | Unset = UNSET,
    created_lte: datetime.datetime | Unset = UNSET,
    created_month: float | Unset = UNSET,
    created_year: float | Unset = UNSET,
    expiration_date_gt: datetime.date | Unset = UNSET,
    expiration_date_gte: datetime.date | Unset = UNSET,
    expiration_date_lt: datetime.date | Unset = UNSET,
    expiration_date_lte: datetime.date | Unset = UNSET,
    expiration_day: float | Unset = UNSET,
    expiration_gt: datetime.datetime | Unset = UNSET,
    expiration_gte: datetime.datetime | Unset = UNSET,
    expiration_lt: datetime.datetime | Unset = UNSET,
    expiration_lte: datetime.datetime | Unset = UNSET,
    expiration_month: float | Unset = UNSET,
    expiration_year: float | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> PaginatedShareLinkList | None:
    """
    Args:
        created_date_gt (datetime.date | Unset):
        created_date_gte (datetime.date | Unset):
        created_date_lt (datetime.date | Unset):
        created_date_lte (datetime.date | Unset):
        created_day (float | Unset):
        created_gt (datetime.datetime | Unset):
        created_gte (datetime.datetime | Unset):
        created_lt (datetime.datetime | Unset):
        created_lte (datetime.datetime | Unset):
        created_month (float | Unset):
        created_year (float | Unset):
        expiration_date_gt (datetime.date | Unset):
        expiration_date_gte (datetime.date | Unset):
        expiration_date_lt (datetime.date | Unset):
        expiration_date_lte (datetime.date | Unset):
        expiration_day (float | Unset):
        expiration_gt (datetime.datetime | Unset):
        expiration_gte (datetime.datetime | Unset):
        expiration_lt (datetime.datetime | Unset):
        expiration_lte (datetime.datetime | Unset):
        expiration_month (float | Unset):
        expiration_year (float | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedShareLinkList
    """

    return (
        await asyncio_detailed(
            client=client,
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
            expiration_date_gt=expiration_date_gt,
            expiration_date_gte=expiration_date_gte,
            expiration_date_lt=expiration_date_lt,
            expiration_date_lte=expiration_date_lte,
            expiration_day=expiration_day,
            expiration_gt=expiration_gt,
            expiration_gte=expiration_gte,
            expiration_lt=expiration_lt,
            expiration_lte=expiration_lte,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            ordering=ordering,
            page=page,
            page_size=page_size,
        )
    ).parsed
