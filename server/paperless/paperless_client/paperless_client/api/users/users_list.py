from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_list import PaginatedUserList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    username_icontains: str | Unset = UNSET,
    username_iendswith: str | Unset = UNSET,
    username_iexact: str | Unset = UNSET,
    username_istartswith: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["username__icontains"] = username_icontains

    params["username__iendswith"] = username_iendswith

    params["username__iexact"] = username_iexact

    params["username__istartswith"] = username_istartswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedUserList | None:
    if response.status_code == 200:
        response_200 = PaginatedUserList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedUserList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    username_icontains: str | Unset = UNSET,
    username_iendswith: str | Unset = UNSET,
    username_iexact: str | Unset = UNSET,
    username_istartswith: str | Unset = UNSET,
) -> Response[PaginatedUserList]:
    """
    Args:
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        username_icontains (str | Unset):
        username_iendswith (str | Unset):
        username_iexact (str | Unset):
        username_istartswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList]
    """

    kwargs = _get_kwargs(
        ordering=ordering,
        page=page,
        page_size=page_size,
        username_icontains=username_icontains,
        username_iendswith=username_iendswith,
        username_iexact=username_iexact,
        username_istartswith=username_istartswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    username_icontains: str | Unset = UNSET,
    username_iendswith: str | Unset = UNSET,
    username_iexact: str | Unset = UNSET,
    username_istartswith: str | Unset = UNSET,
) -> PaginatedUserList | None:
    """
    Args:
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        username_icontains (str | Unset):
        username_iendswith (str | Unset):
        username_iexact (str | Unset):
        username_istartswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList
    """

    return sync_detailed(
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        username_icontains=username_icontains,
        username_iendswith=username_iendswith,
        username_iexact=username_iexact,
        username_istartswith=username_istartswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    username_icontains: str | Unset = UNSET,
    username_iendswith: str | Unset = UNSET,
    username_iexact: str | Unset = UNSET,
    username_istartswith: str | Unset = UNSET,
) -> Response[PaginatedUserList]:
    """
    Args:
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        username_icontains (str | Unset):
        username_iendswith (str | Unset):
        username_iexact (str | Unset):
        username_istartswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList]
    """

    kwargs = _get_kwargs(
        ordering=ordering,
        page=page,
        page_size=page_size,
        username_icontains=username_icontains,
        username_iendswith=username_iendswith,
        username_iexact=username_iexact,
        username_istartswith=username_istartswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    username_icontains: str | Unset = UNSET,
    username_iendswith: str | Unset = UNSET,
    username_iexact: str | Unset = UNSET,
    username_istartswith: str | Unset = UNSET,
) -> PaginatedUserList | None:
    """
    Args:
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        username_icontains (str | Unset):
        username_iendswith (str | Unset):
        username_iexact (str | Unset):
        username_istartswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList
    """

    return (
        await asyncio_detailed(
            client=client,
            ordering=ordering,
            page=page,
            page_size=page_size,
            username_icontains=username_icontains,
            username_iendswith=username_iendswith,
            username_iexact=username_iexact,
            username_istartswith=username_istartswith,
        )
    ).parsed
