from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acknowledge_tasks import AcknowledgeTasks
from ...models.acknowledge_tasks_body import AcknowledgeTasksBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AcknowledgeTasksBody | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["task_id"] = task_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tasks/acknowledge/",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AcknowledgeTasks | Any | None:
    if response.status_code == 200:
        response_200 = AcknowledgeTasks.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AcknowledgeTasks | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AcknowledgeTasksBody | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> Response[AcknowledgeTasks | Any]:
    """Acknowledge a list of tasks

    Args:
        task_id (str | Unset):
        body (AcknowledgeTasksBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcknowledgeTasks | Any]
    """

    kwargs = _get_kwargs(
        body=body,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AcknowledgeTasksBody | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> AcknowledgeTasks | Any | None:
    """Acknowledge a list of tasks

    Args:
        task_id (str | Unset):
        body (AcknowledgeTasksBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcknowledgeTasks | Any
    """

    return sync_detailed(
        client=client,
        body=body,
        task_id=task_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AcknowledgeTasksBody | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> Response[AcknowledgeTasks | Any]:
    """Acknowledge a list of tasks

    Args:
        task_id (str | Unset):
        body (AcknowledgeTasksBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcknowledgeTasks | Any]
    """

    kwargs = _get_kwargs(
        body=body,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AcknowledgeTasksBody | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> AcknowledgeTasks | Any | None:
    """Acknowledge a list of tasks

    Args:
        task_id (str | Unset):
        body (AcknowledgeTasksBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcknowledgeTasks | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            task_id=task_id,
        )
    ).parsed
