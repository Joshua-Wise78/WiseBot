from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_result import SearchResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    db_only: bool | Unset = UNSET,
    query: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["db_only"] = db_only

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/search/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchResult | None:
    if response.status_code == 200:
        response_200 = SearchResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    db_only: bool | Unset = UNSET,
    query: str,
) -> Response[SearchResult]:
    """Global search

    Args:
        db_only (bool | Unset):
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResult]
    """

    kwargs = _get_kwargs(
        db_only=db_only,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    db_only: bool | Unset = UNSET,
    query: str,
) -> SearchResult | None:
    """Global search

    Args:
        db_only (bool | Unset):
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResult
    """

    return sync_detailed(
        client=client,
        db_only=db_only,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    db_only: bool | Unset = UNSET,
    query: str,
) -> Response[SearchResult]:
    """Global search

    Args:
        db_only (bool | Unset):
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResult]
    """

    kwargs = _get_kwargs(
        db_only=db_only,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    db_only: bool | Unset = UNSET,
    query: str,
) -> SearchResult | None:
    """Global search

    Args:
        db_only (bool | Unset):
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResult
    """

    return (
        await asyncio_detailed(
            client=client,
            db_only=db_only,
            query=query,
        )
    ).parsed
