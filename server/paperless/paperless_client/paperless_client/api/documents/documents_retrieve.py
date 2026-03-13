from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document import Document
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["full_perms"] = full_perms

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/documents/{id}/".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Document | None:
    if response.status_code == 200:
        response_200 = Document.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Document]:
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
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
) -> Response[Any | Document]:
    """Retrieve a single document

    Args:
        id (int):
        fields (list[str] | Unset):
        full_perms (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Document]
    """

    kwargs = _get_kwargs(
        id=id,
        fields=fields,
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
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
) -> Any | Document | None:
    """Retrieve a single document

    Args:
        id (int):
        fields (list[str] | Unset):
        full_perms (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Document
    """

    return sync_detailed(
        id=id,
        client=client,
        fields=fields,
        full_perms=full_perms,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
) -> Response[Any | Document]:
    """Retrieve a single document

    Args:
        id (int):
        fields (list[str] | Unset):
        full_perms (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Document]
    """

    kwargs = _get_kwargs(
        id=id,
        fields=fields,
        full_perms=full_perms,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    fields: list[str] | Unset = UNSET,
    full_perms: bool | Unset = UNSET,
) -> Any | Document | None:
    """Retrieve a single document

    Args:
        id (int):
        fields (list[str] | Unset):
        full_perms (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Document
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            fields=fields,
            full_perms=full_perms,
        )
    ).parsed
