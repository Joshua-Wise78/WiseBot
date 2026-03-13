from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.profile_disconnect_social_account_create_body import ProfileDisconnectSocialAccountCreateBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ProfileDisconnectSocialAccountCreateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/profile/disconnect_social_account/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> int | str | None:
    if response.status_code == 200:
        response_200 = cast(int, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[int | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProfileDisconnectSocialAccountCreateBody | Unset = UNSET,
) -> Response[int | str]:
    """Disconnects a social account provider from the user account

    Args:
        body (ProfileDisconnectSocialAccountCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int | str]
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
    body: ProfileDisconnectSocialAccountCreateBody | Unset = UNSET,
) -> int | str | None:
    """Disconnects a social account provider from the user account

    Args:
        body (ProfileDisconnectSocialAccountCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProfileDisconnectSocialAccountCreateBody | Unset = UNSET,
) -> Response[int | str]:
    """Disconnects a social account provider from the user account

    Args:
        body (ProfileDisconnectSocialAccountCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[int | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProfileDisconnectSocialAccountCreateBody | Unset = UNSET,
) -> int | str | None:
    """Disconnects a social account provider from the user account

    Args:
        body (ProfileDisconnectSocialAccountCreateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        int | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
