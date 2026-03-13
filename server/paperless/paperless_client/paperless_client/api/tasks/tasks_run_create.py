from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tasks_view import TasksView
from ...models.tasks_view_request import TasksViewRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TasksViewRequest | TasksViewRequest | TasksViewRequest | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["task_id"] = task_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tasks/run/",
        "params": params,
    }

    if isinstance(body, TasksViewRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, TasksViewRequest):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, TasksViewRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TasksView | None:
    if response.status_code == 200:
        response_200 = TasksView.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TasksView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TasksViewRequest | TasksViewRequest | TasksViewRequest | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> Response[TasksView]:
    """
    Args:
        task_id (str | Unset):
        body (TasksViewRequest):
        body (TasksViewRequest):
        body (TasksViewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TasksView]
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
    body: TasksViewRequest | TasksViewRequest | TasksViewRequest | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> TasksView | None:
    """
    Args:
        task_id (str | Unset):
        body (TasksViewRequest):
        body (TasksViewRequest):
        body (TasksViewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TasksView
    """

    return sync_detailed(
        client=client,
        body=body,
        task_id=task_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TasksViewRequest | TasksViewRequest | TasksViewRequest | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> Response[TasksView]:
    """
    Args:
        task_id (str | Unset):
        body (TasksViewRequest):
        body (TasksViewRequest):
        body (TasksViewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TasksView]
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
    body: TasksViewRequest | TasksViewRequest | TasksViewRequest | Unset = UNSET,
    task_id: str | Unset = UNSET,
) -> TasksView | None:
    """
    Args:
        task_id (str | Unset):
        body (TasksViewRequest):
        body (TasksViewRequest):
        body (TasksViewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TasksView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            task_id=task_id,
        )
    ).parsed
