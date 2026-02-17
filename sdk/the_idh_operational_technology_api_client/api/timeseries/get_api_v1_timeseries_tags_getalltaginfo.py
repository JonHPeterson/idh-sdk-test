from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_timeseries_tags_getalltaginfo_response_200 import (
    GetApiV1TimeseriesTagsGetalltaginfoResponse200,
)
from ...models.get_api_v1_timeseries_tags_getalltaginfo_response_500 import (
    GetApiV1TimeseriesTagsGetalltaginfoResponse500,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    start_position: int,
    max_results: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["startPosition"] = start_position

    params["maxResults"] = max_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/timeseries/tags/getalltaginfo",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]]:
    if response.status_code == 200:
        response_200 = GetApiV1TimeseriesTagsGetalltaginfoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = GetApiV1TimeseriesTagsGetalltaginfoResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_position: int,
    max_results: int,
) -> Response[Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]]:
    """Get timeseries tag info for all tags

     Get timeseries tag info for all tags

    Args:
        start_position (int):
        max_results (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]]
    """

    kwargs = _get_kwargs(
        start_position=start_position,
        max_results=max_results,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_position: int,
    max_results: int,
) -> Optional[Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]]:
    """Get timeseries tag info for all tags

     Get timeseries tag info for all tags

    Args:
        start_position (int):
        max_results (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]
    """

    return sync_detailed(
        client=client,
        start_position=start_position,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_position: int,
    max_results: int,
) -> Response[Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]]:
    """Get timeseries tag info for all tags

     Get timeseries tag info for all tags

    Args:
        start_position (int):
        max_results (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]]
    """

    kwargs = _get_kwargs(
        start_position=start_position,
        max_results=max_results,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_position: int,
    max_results: int,
) -> Optional[Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]]:
    """Get timeseries tag info for all tags

     Get timeseries tag info for all tags

    Args:
        start_position (int):
        max_results (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesTagsGetalltaginfoResponse200, GetApiV1TimeseriesTagsGetalltaginfoResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_position=start_position,
            max_results=max_results,
        )
    ).parsed
