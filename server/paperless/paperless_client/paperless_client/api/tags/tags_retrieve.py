from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tag import Tag
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    full_perms: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["full_perms"] = full_perms

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tags/{id}/".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Tag | None:
    if response.status_code == 200:
        response_200 = Tag.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Tag]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    full_perms: bool | Unset = UNSET,
) -> Response[Tag]:
    """Mixin to add document count to queryset, permissions-aware if needed

    Args:
        id (int):
        full_perms (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Tag]
    """

    kwargs = _get_kwargs(
        id=id,
        full_perms=full_perms,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    full_perms: bool | Unset = UNSET,
) -> Tag | None:
    """Mixin to add document count to queryset, permissions-aware if needed

    Args:
        id (int):
        full_perms (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Tag
    """

    return sync_detailed(
        id=id,
        client=client,
        full_perms=full_perms,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    full_perms: bool | Unset = UNSET,
) -> Response[Tag]:
    """Mixin to add document count to queryset, permissions-aware if needed

    Args:
        id (int):
        full_perms (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Tag]
    """

    kwargs = _get_kwargs(
        id=id,
        full_perms=full_perms,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    full_perms: bool | Unset = UNSET,
) -> Tag | None:
    """Mixin to add document count to queryset, permissions-aware if needed

    Args:
        id (int):
        full_perms (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Tag
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            full_perms=full_perms,
        )
    ).parsed
