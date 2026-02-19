from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_by_source_response_404 import GetTagsBySourceResponse404
from ...models.get_tags_by_source_response_500 import GetTagsBySourceResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_uuid: str,
    *,
    src_data_uui_ds: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_src_data_uui_ds: Union[Unset, list[str]] = UNSET
    if not isinstance(src_data_uui_ds, Unset):
        json_src_data_uui_ds = src_data_uui_ds

    params["srcDataUUIDs"] = json_src_data_uui_ds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/timeseries/tagsbysource/{source_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]]:
    if response.status_code == 200:
        response_200 = cast(list[str], response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetTagsBySourceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetTagsBySourceResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    src_data_uui_ds: Union[Unset, list[str]] = UNSET,
) -> Response[Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]]:
    """Get timeseries tag UUIDs for a specific source

     Get timeseries tag UUIDs for a specific source

    Args:
        source_uuid (str):
        src_data_uui_ds (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]]
    """

    kwargs = _get_kwargs(
        source_uuid=source_uuid,
        src_data_uui_ds=src_data_uui_ds,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    src_data_uui_ds: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]]:
    """Get timeseries tag UUIDs for a specific source

     Get timeseries tag UUIDs for a specific source

    Args:
        source_uuid (str):
        src_data_uui_ds (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]
    """

    return sync_detailed(
        source_uuid=source_uuid,
        client=client,
        src_data_uui_ds=src_data_uui_ds,
    ).parsed


async def asyncio_detailed(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    src_data_uui_ds: Union[Unset, list[str]] = UNSET,
) -> Response[Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]]:
    """Get timeseries tag UUIDs for a specific source

     Get timeseries tag UUIDs for a specific source

    Args:
        source_uuid (str):
        src_data_uui_ds (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]]
    """

    kwargs = _get_kwargs(
        source_uuid=source_uuid,
        src_data_uui_ds=src_data_uui_ds,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    src_data_uui_ds: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]]:
    """Get timeseries tag UUIDs for a specific source

     Get timeseries tag UUIDs for a specific source

    Args:
        source_uuid (str):
        src_data_uui_ds (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTagsBySourceResponse404, GetTagsBySourceResponse500, list[str]]
    """

    return (
        await asyncio_detailed(
            source_uuid=source_uuid,
            client=client,
            src_data_uui_ds=src_data_uui_ds,
        )
    ).parsed
