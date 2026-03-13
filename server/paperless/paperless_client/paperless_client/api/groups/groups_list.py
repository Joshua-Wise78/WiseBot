from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_group_list import PaginatedGroupList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name__icontains"] = name_icontains

    params["name__iendswith"] = name_iendswith

    params["name__iexact"] = name_iexact

    params["name__istartswith"] = name_istartswith

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/groups/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedGroupList | None:
    if response.status_code == 200:
        response_200 = PaginatedGroupList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedGroupList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[PaginatedGroupList]:
    """
    Args:
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_istartswith (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGroupList]
    """

    kwargs = _get_kwargs(
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_istartswith=name_istartswith,
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
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> PaginatedGroupList | None:
    """
    Args:
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_istartswith (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGroupList
    """

    return sync_detailed(
        client=client,
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_istartswith=name_istartswith,
        ordering=ordering,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[PaginatedGroupList]:
    """
    Args:
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_istartswith (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGroupList]
    """

    kwargs = _get_kwargs(
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_istartswith=name_istartswith,
        ordering=ordering,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> PaginatedGroupList | None:
    """
    Args:
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_istartswith (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGroupList
    """

    return (
        await asyncio_detailed(
            client=client,
            name_icontains=name_icontains,
            name_iendswith=name_iendswith,
            name_iexact=name_iexact,
            name_istartswith=name_istartswith,
            ordering=ordering,
            page=page,
            page_size=page_size,
        )
    ).parsed
