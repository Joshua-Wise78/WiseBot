from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.profile_totp_create_body import ProfileTotpCreateBody
from ...models.profile_totp_create_response_200 import ProfileTotpCreateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ProfileTotpCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/profile/totp/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProfileTotpCreateResponse200 | None:
    if response.status_code == 200:
        response_200 = ProfileTotpCreateResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProfileTotpCreateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProfileTotpCreateBody | Unset = UNSET,
) -> Response[ProfileTotpCreateResponse200]:
    """Validates a TOTP code and activates the TOTP authenticator

    Args:
        body (ProfileTotpCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileTotpCreateResponse200]
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
    body: ProfileTotpCreateBody | Unset = UNSET,
) -> ProfileTotpCreateResponse200 | None:
    """Validates a TOTP code and activates the TOTP authenticator

    Args:
        body (ProfileTotpCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileTotpCreateResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProfileTotpCreateBody | Unset = UNSET,
) -> Response[ProfileTotpCreateResponse200]:
    """Validates a TOTP code and activates the TOTP authenticator

    Args:
        body (ProfileTotpCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProfileTotpCreateResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProfileTotpCreateBody | Unset = UNSET,
) -> ProfileTotpCreateResponse200 | None:
    """Validates a TOTP code and activates the TOTP authenticator

    Args:
        body (ProfileTotpCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProfileTotpCreateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
