from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_notes_list import PaginatedNotesList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id_path: int,
    *,
    id_query: int | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id_query

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/documents/{id_path}/notes/".format(
            id_path=quote(str(id_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PaginatedNotesList | None:
    if response.status_code == 200:
        response_200 = PaginatedNotesList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PaginatedNotesList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_path: int,
    *,
    client: AuthenticatedClient,
    id_query: int | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[Any | PaginatedNotesList]:
    """View, add, or delete notes for the document

    Args:
        id_path (int):
        id_query (int | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedNotesList]
    """

    kwargs = _get_kwargs(
        id_path=id_path,
        id_query=id_query,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_path: int,
    *,
    client: AuthenticatedClient,
    id_query: int | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Any | PaginatedNotesList | None:
    """View, add, or delete notes for the document

    Args:
        id_path (int):
        id_query (int | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedNotesList
    """

    return sync_detailed(
        id_path=id_path,
        client=client,
        id_query=id_query,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    id_path: int,
    *,
    client: AuthenticatedClient,
    id_query: int | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[Any | PaginatedNotesList]:
    """View, add, or delete notes for the document

    Args:
        id_path (int):
        id_query (int | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PaginatedNotesList]
    """

    kwargs = _get_kwargs(
        id_path=id_path,
        id_query=id_query,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_path: int,
    *,
    client: AuthenticatedClient,
    id_query: int | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Any | PaginatedNotesList | None:
    """View, add, or delete notes for the document

    Args:
        id_path (int):
        id_query (int | Unset):
        page (int | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PaginatedNotesList
    """

    return (
        await asyncio_detailed(
            id_path=id_path,
            client=client,
            id_query=id_query,
            page=page,
            page_size=page_size,
        )
    ).parsed
