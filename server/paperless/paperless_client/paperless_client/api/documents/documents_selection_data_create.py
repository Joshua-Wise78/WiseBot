from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_list_request import DocumentListRequest
from ...models.selection_data import SelectionData
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: DocumentListRequest | DocumentListRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/documents/selection_data/",
    }

    if isinstance(body, DocumentListRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"
    if isinstance(body, DocumentListRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SelectionData | None:
    if response.status_code == 200:
        response_200 = SelectionData.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SelectionData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DocumentListRequest | DocumentListRequest | Unset = UNSET,
) -> Response[SelectionData]:
    """Get selection data for the selected documents

    Args:
        body (DocumentListRequest):
        body (DocumentListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SelectionData]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DocumentListRequest | DocumentListRequest | Unset = UNSET,
) -> SelectionData | None:
    """Get selection data for the selected documents

    Args:
        body (DocumentListRequest):
        body (DocumentListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SelectionData
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DocumentListRequest | DocumentListRequest | Unset = UNSET,
) -> Response[SelectionData]:
    """Get selection data for the selected documents

    Args:
        body (DocumentListRequest):
        body (DocumentListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SelectionData]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DocumentListRequest | DocumentListRequest | Unset = UNSET,
) -> SelectionData | None:
    """Get selection data for the selected documents

    Args:
        body (DocumentListRequest):
        body (DocumentListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SelectionData
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
