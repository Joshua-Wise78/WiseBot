from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tasks_list_task_name import TasksListTaskName
from ...models.tasks_list_task_state import TasksListTaskState
from ...models.tasks_list_task_type import TasksListTaskType
from ...models.tasks_view import TasksView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    acknowledged: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    status: TasksListTaskState | Unset = UNSET,
    task_id: str | Unset = UNSET,
    task_name: TasksListTaskName | Unset = UNSET,
    type_: TasksListTaskType | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["acknowledged"] = acknowledged

    params["ordering"] = ordering

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["task_id"] = task_id

    json_task_name: str | Unset = UNSET
    if not isinstance(task_name, Unset):
        json_task_name = task_name.value

    params["task_name"] = json_task_name

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tasks/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[TasksView] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TasksView.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[TasksView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    acknowledged: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    status: TasksListTaskState | Unset = UNSET,
    task_id: str | Unset = UNSET,
    task_name: TasksListTaskName | Unset = UNSET,
    type_: TasksListTaskType | Unset = UNSET,
) -> Response[list[TasksView]]:
    """
    Args:
        acknowledged (bool | Unset):
        ordering (str | Unset):
        status (TasksListTaskState | Unset):
        task_id (str | Unset):
        task_name (TasksListTaskName | Unset):
        type_ (TasksListTaskType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TasksView]]
    """

    kwargs = _get_kwargs(
        acknowledged=acknowledged,
        ordering=ordering,
        status=status,
        task_id=task_id,
        task_name=task_name,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    acknowledged: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    status: TasksListTaskState | Unset = UNSET,
    task_id: str | Unset = UNSET,
    task_name: TasksListTaskName | Unset = UNSET,
    type_: TasksListTaskType | Unset = UNSET,
) -> list[TasksView] | None:
    """
    Args:
        acknowledged (bool | Unset):
        ordering (str | Unset):
        status (TasksListTaskState | Unset):
        task_id (str | Unset):
        task_name (TasksListTaskName | Unset):
        type_ (TasksListTaskType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TasksView]
    """

    return sync_detailed(
        client=client,
        acknowledged=acknowledged,
        ordering=ordering,
        status=status,
        task_id=task_id,
        task_name=task_name,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    acknowledged: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    status: TasksListTaskState | Unset = UNSET,
    task_id: str | Unset = UNSET,
    task_name: TasksListTaskName | Unset = UNSET,
    type_: TasksListTaskType | Unset = UNSET,
) -> Response[list[TasksView]]:
    """
    Args:
        acknowledged (bool | Unset):
        ordering (str | Unset):
        status (TasksListTaskState | Unset):
        task_id (str | Unset):
        task_name (TasksListTaskName | Unset):
        type_ (TasksListTaskType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[TasksView]]
    """

    kwargs = _get_kwargs(
        acknowledged=acknowledged,
        ordering=ordering,
        status=status,
        task_id=task_id,
        task_name=task_name,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    acknowledged: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    status: TasksListTaskState | Unset = UNSET,
    task_id: str | Unset = UNSET,
    task_name: TasksListTaskName | Unset = UNSET,
    type_: TasksListTaskType | Unset = UNSET,
) -> list[TasksView] | None:
    """
    Args:
        acknowledged (bool | Unset):
        ordering (str | Unset):
        status (TasksListTaskState | Unset):
        task_id (str | Unset):
        task_name (TasksListTaskName | Unset):
        type_ (TasksListTaskType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[TasksView]
    """

    return (
        await asyncio_detailed(
            client=client,
            acknowledged=acknowledged,
            ordering=ordering,
            status=status,
            task_id=task_id,
            task_name=task_name,
            type_=type_,
        )
    ).parsed
