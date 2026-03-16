from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mail_account_process_response import MailAccountProcessResponse
from ...models.mail_account_request import MailAccountRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: MailAccountRequest | MailAccountRequest | MailAccountRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/mail_accounts/{id}/process/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, MailAccountRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MailAccountRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, MailAccountRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MailAccountProcessResponse | None:
    if response.status_code == 200:
        response_200 = MailAccountProcessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MailAccountProcessResponse]:
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
    body: MailAccountRequest | MailAccountRequest | MailAccountRequest | Unset = UNSET,
) -> Response[Any | MailAccountProcessResponse]:
    """Manually process the selected mail account for new messages.

    Args:
        id (int):
        body (MailAccountRequest):
        body (MailAccountRequest):
        body (MailAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MailAccountProcessResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: MailAccountRequest | MailAccountRequest | MailAccountRequest | Unset = UNSET,
) -> Any | MailAccountProcessResponse | None:
    """Manually process the selected mail account for new messages.

    Args:
        id (int):
        body (MailAccountRequest):
        body (MailAccountRequest):
        body (MailAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MailAccountProcessResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: MailAccountRequest | MailAccountRequest | MailAccountRequest | Unset = UNSET,
) -> Response[Any | MailAccountProcessResponse]:
    """Manually process the selected mail account for new messages.

    Args:
        id (int):
        body (MailAccountRequest):
        body (MailAccountRequest):
        body (MailAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MailAccountProcessResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: MailAccountRequest | MailAccountRequest | MailAccountRequest | Unset = UNSET,
) -> Any | MailAccountProcessResponse | None:
    """Manually process the selected mail account for new messages.

    Args:
        id (int):
        body (MailAccountRequest):
        body (MailAccountRequest):
        body (MailAccountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MailAccountProcessResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
