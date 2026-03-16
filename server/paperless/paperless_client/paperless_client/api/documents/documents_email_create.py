from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_document_request_request import EmailDocumentRequestRequest
from ...models.email_document_response import EmailDocumentResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: EmailDocumentRequestRequest | EmailDocumentRequestRequest | EmailDocumentRequestRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/documents/{id}/email/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, EmailDocumentRequestRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, EmailDocumentRequestRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, EmailDocumentRequestRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EmailDocumentResponse | None:
    if response.status_code == 200:
        response_200 = EmailDocumentResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EmailDocumentResponse]:
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
    body: EmailDocumentRequestRequest | EmailDocumentRequestRequest | EmailDocumentRequestRequest | Unset = UNSET,
) -> Response[Any | EmailDocumentResponse]:
    """Email the document to one or more recipients as an attachment.

    Args:
        id (int):
        body (EmailDocumentRequestRequest):
        body (EmailDocumentRequestRequest):
        body (EmailDocumentRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmailDocumentResponse]
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
    body: EmailDocumentRequestRequest | EmailDocumentRequestRequest | EmailDocumentRequestRequest | Unset = UNSET,
) -> Any | EmailDocumentResponse | None:
    """Email the document to one or more recipients as an attachment.

    Args:
        id (int):
        body (EmailDocumentRequestRequest):
        body (EmailDocumentRequestRequest):
        body (EmailDocumentRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmailDocumentResponse
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
    body: EmailDocumentRequestRequest | EmailDocumentRequestRequest | EmailDocumentRequestRequest | Unset = UNSET,
) -> Response[Any | EmailDocumentResponse]:
    """Email the document to one or more recipients as an attachment.

    Args:
        id (int):
        body (EmailDocumentRequestRequest):
        body (EmailDocumentRequestRequest):
        body (EmailDocumentRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmailDocumentResponse]
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
    body: EmailDocumentRequestRequest | EmailDocumentRequestRequest | EmailDocumentRequestRequest | Unset = UNSET,
) -> Any | EmailDocumentResponse | None:
    """Email the document to one or more recipients as an attachment.

    Args:
        id (int):
        body (EmailDocumentRequestRequest):
        body (EmailDocumentRequestRequest):
        body (EmailDocumentRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmailDocumentResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
