from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workflow_trigger import WorkflowTrigger
from ...models.workflow_trigger_request import WorkflowTriggerRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: WorkflowTriggerRequest | WorkflowTriggerRequest | WorkflowTriggerRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/workflow_triggers/",
    }

    if isinstance(body, WorkflowTriggerRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, WorkflowTriggerRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, WorkflowTriggerRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WorkflowTrigger | None:
    if response.status_code == 201:
        response_201 = WorkflowTrigger.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WorkflowTrigger]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WorkflowTriggerRequest | WorkflowTriggerRequest | WorkflowTriggerRequest | Unset = UNSET,
) -> Response[WorkflowTrigger]:
    """
    Args:
        body (WorkflowTriggerRequest):
        body (WorkflowTriggerRequest):
        body (WorkflowTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowTrigger]
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
    body: WorkflowTriggerRequest | WorkflowTriggerRequest | WorkflowTriggerRequest | Unset = UNSET,
) -> WorkflowTrigger | None:
    """
    Args:
        body (WorkflowTriggerRequest):
        body (WorkflowTriggerRequest):
        body (WorkflowTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowTrigger
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WorkflowTriggerRequest | WorkflowTriggerRequest | WorkflowTriggerRequest | Unset = UNSET,
) -> Response[WorkflowTrigger]:
    """
    Args:
        body (WorkflowTriggerRequest):
        body (WorkflowTriggerRequest):
        body (WorkflowTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowTrigger]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WorkflowTriggerRequest | WorkflowTriggerRequest | WorkflowTriggerRequest | Unset = UNSET,
) -> WorkflowTrigger | None:
    """
    Args:
        body (WorkflowTriggerRequest):
        body (WorkflowTriggerRequest):
        body (WorkflowTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowTrigger
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
