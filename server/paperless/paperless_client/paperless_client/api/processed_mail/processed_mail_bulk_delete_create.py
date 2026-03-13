from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.processed_mail import ProcessedMail
from ...models.processed_mail_request import ProcessedMailRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ProcessedMailRequest | ProcessedMailRequest | ProcessedMailRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/processed_mail/bulk_delete/",
    }

    if isinstance(body, ProcessedMailRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ProcessedMailRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ProcessedMailRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProcessedMail | None:
    if response.status_code == 200:
        response_200 = ProcessedMail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProcessedMail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProcessedMailRequest | ProcessedMailRequest | ProcessedMailRequest | Unset = UNSET,
) -> Response[ProcessedMail]:
    """
    Args:
        body (ProcessedMailRequest | Unset):
        body (ProcessedMailRequest | Unset):
        body (ProcessedMailRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcessedMail]
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
    body: ProcessedMailRequest | ProcessedMailRequest | ProcessedMailRequest | Unset = UNSET,
) -> ProcessedMail | None:
    """
    Args:
        body (ProcessedMailRequest | Unset):
        body (ProcessedMailRequest | Unset):
        body (ProcessedMailRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcessedMail
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProcessedMailRequest | ProcessedMailRequest | ProcessedMailRequest | Unset = UNSET,
) -> Response[ProcessedMail]:
    """
    Args:
        body (ProcessedMailRequest | Unset):
        body (ProcessedMailRequest | Unset):
        body (ProcessedMailRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcessedMail]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProcessedMailRequest | ProcessedMailRequest | ProcessedMailRequest | Unset = UNSET,
) -> ProcessedMail | None:
    """
    Args:
        body (ProcessedMailRequest | Unset):
        body (ProcessedMailRequest | Unset):
        body (ProcessedMailRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcessedMail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
