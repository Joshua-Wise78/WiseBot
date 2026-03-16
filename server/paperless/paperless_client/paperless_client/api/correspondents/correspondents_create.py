from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.correspondent import Correspondent
from ...models.correspondent_request import CorrespondentRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CorrespondentRequest | CorrespondentRequest | CorrespondentRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/correspondents/",
    }

    if isinstance(body, CorrespondentRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CorrespondentRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CorrespondentRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Correspondent | None:
    if response.status_code == 201:
        response_201 = Correspondent.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Correspondent]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CorrespondentRequest | CorrespondentRequest | CorrespondentRequest | Unset = UNSET,
) -> Response[Correspondent]:
    """Mixin to add document count to queryset, permissions-aware if needed

    Args:
        body (CorrespondentRequest):
        body (CorrespondentRequest):
        body (CorrespondentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Correspondent]
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
    body: CorrespondentRequest | CorrespondentRequest | CorrespondentRequest | Unset = UNSET,
) -> Correspondent | None:
    """Mixin to add document count to queryset, permissions-aware if needed

    Args:
        body (CorrespondentRequest):
        body (CorrespondentRequest):
        body (CorrespondentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Correspondent
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CorrespondentRequest | CorrespondentRequest | CorrespondentRequest | Unset = UNSET,
) -> Response[Correspondent]:
    """Mixin to add document count to queryset, permissions-aware if needed

    Args:
        body (CorrespondentRequest):
        body (CorrespondentRequest):
        body (CorrespondentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Correspondent]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CorrespondentRequest | CorrespondentRequest | CorrespondentRequest | Unset = UNSET,
) -> Correspondent | None:
    """Mixin to add document count to queryset, permissions-aware if needed

    Args:
        body (CorrespondentRequest):
        body (CorrespondentRequest):
        body (CorrespondentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Correspondent
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
