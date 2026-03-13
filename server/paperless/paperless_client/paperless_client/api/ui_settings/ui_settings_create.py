from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ui_settings_view import UiSettingsView
from ...models.ui_settings_view_request import UiSettingsViewRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UiSettingsViewRequest | UiSettingsViewRequest | UiSettingsViewRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ui_settings/",
    }

    if isinstance(body, UiSettingsViewRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UiSettingsViewRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UiSettingsViewRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UiSettingsView | None:
    if response.status_code == 200:
        response_200 = UiSettingsView.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UiSettingsView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UiSettingsViewRequest | UiSettingsViewRequest | UiSettingsViewRequest | Unset = UNSET,
) -> Response[UiSettingsView]:
    """
    Args:
        body (UiSettingsViewRequest | Unset):
        body (UiSettingsViewRequest | Unset):
        body (UiSettingsViewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UiSettingsView]
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
    body: UiSettingsViewRequest | UiSettingsViewRequest | UiSettingsViewRequest | Unset = UNSET,
) -> UiSettingsView | None:
    """
    Args:
        body (UiSettingsViewRequest | Unset):
        body (UiSettingsViewRequest | Unset):
        body (UiSettingsViewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UiSettingsView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UiSettingsViewRequest | UiSettingsViewRequest | UiSettingsViewRequest | Unset = UNSET,
) -> Response[UiSettingsView]:
    """
    Args:
        body (UiSettingsViewRequest | Unset):
        body (UiSettingsViewRequest | Unset):
        body (UiSettingsViewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UiSettingsView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UiSettingsViewRequest | UiSettingsViewRequest | UiSettingsViewRequest | Unset = UNSET,
) -> UiSettingsView | None:
    """
    Args:
        body (UiSettingsViewRequest | Unset):
        body (UiSettingsViewRequest | Unset):
        body (UiSettingsViewRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UiSettingsView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
