from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_timeseries_aggregatesamples_response_500 import GetApiV1TimeseriesAggregatesamplesResponse500
from ...models.time_series_samples_response import TimeSeriesSamplesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    starttime: str,
    endtime: str,
    aggregate_type: int,
    window: float,
    max_samples: int,
    tag_uui_ds: list[str],
    from_units: Union[Unset, list[str]] = UNSET,
    to_units: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["starttime"] = starttime

    params["endtime"] = endtime

    params["aggregate_type"] = aggregate_type

    params["window"] = window

    params["maxSamples"] = max_samples

    json_tag_uui_ds = tag_uui_ds

    params["tagUUIDs"] = json_tag_uui_ds

    json_from_units: Union[Unset, list[str]] = UNSET
    if not isinstance(from_units, Unset):
        json_from_units = from_units

    params["fromUnits"] = json_from_units

    json_to_units: Union[Unset, list[str]] = UNSET
    if not isinstance(to_units, Unset):
        json_to_units = to_units

    params["toUnits"] = json_to_units

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/timeseries/aggregatesamples",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]]:
    if response.status_code == 200:
        response_200 = TimeSeriesSamplesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = GetApiV1TimeseriesAggregatesamplesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    starttime: str,
    endtime: str,
    aggregate_type: int,
    window: float,
    max_samples: int,
    tag_uui_ds: list[str],
    from_units: Union[Unset, list[str]] = UNSET,
    to_units: Union[Unset, list[str]] = UNSET,
) -> Response[Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]]:
    r"""Get aggregate timeseries samples for tags

     Get data for timeseries tags aggregated. Supports both JSON and binary (MessagePack) formats. For
    binary, set Accept header to \"application/msgpack\"

    Args:
        starttime (str):
        endtime (str):
        aggregate_type (int):
        window (float):
        max_samples (int):
        tag_uui_ds (list[str]):
        from_units (Union[Unset, list[str]]):
        to_units (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]]
    """

    kwargs = _get_kwargs(
        starttime=starttime,
        endtime=endtime,
        aggregate_type=aggregate_type,
        window=window,
        max_samples=max_samples,
        tag_uui_ds=tag_uui_ds,
        from_units=from_units,
        to_units=to_units,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    starttime: str,
    endtime: str,
    aggregate_type: int,
    window: float,
    max_samples: int,
    tag_uui_ds: list[str],
    from_units: Union[Unset, list[str]] = UNSET,
    to_units: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]]:
    r"""Get aggregate timeseries samples for tags

     Get data for timeseries tags aggregated. Supports both JSON and binary (MessagePack) formats. For
    binary, set Accept header to \"application/msgpack\"

    Args:
        starttime (str):
        endtime (str):
        aggregate_type (int):
        window (float):
        max_samples (int):
        tag_uui_ds (list[str]):
        from_units (Union[Unset, list[str]]):
        to_units (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]
    """

    return sync_detailed(
        client=client,
        starttime=starttime,
        endtime=endtime,
        aggregate_type=aggregate_type,
        window=window,
        max_samples=max_samples,
        tag_uui_ds=tag_uui_ds,
        from_units=from_units,
        to_units=to_units,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    starttime: str,
    endtime: str,
    aggregate_type: int,
    window: float,
    max_samples: int,
    tag_uui_ds: list[str],
    from_units: Union[Unset, list[str]] = UNSET,
    to_units: Union[Unset, list[str]] = UNSET,
) -> Response[Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]]:
    r"""Get aggregate timeseries samples for tags

     Get data for timeseries tags aggregated. Supports both JSON and binary (MessagePack) formats. For
    binary, set Accept header to \"application/msgpack\"

    Args:
        starttime (str):
        endtime (str):
        aggregate_type (int):
        window (float):
        max_samples (int):
        tag_uui_ds (list[str]):
        from_units (Union[Unset, list[str]]):
        to_units (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]]
    """

    kwargs = _get_kwargs(
        starttime=starttime,
        endtime=endtime,
        aggregate_type=aggregate_type,
        window=window,
        max_samples=max_samples,
        tag_uui_ds=tag_uui_ds,
        from_units=from_units,
        to_units=to_units,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    starttime: str,
    endtime: str,
    aggregate_type: int,
    window: float,
    max_samples: int,
    tag_uui_ds: list[str],
    from_units: Union[Unset, list[str]] = UNSET,
    to_units: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]]:
    r"""Get aggregate timeseries samples for tags

     Get data for timeseries tags aggregated. Supports both JSON and binary (MessagePack) formats. For
    binary, set Accept header to \"application/msgpack\"

    Args:
        starttime (str):
        endtime (str):
        aggregate_type (int):
        window (float):
        max_samples (int):
        tag_uui_ds (list[str]):
        from_units (Union[Unset, list[str]]):
        to_units (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesAggregatesamplesResponse500, TimeSeriesSamplesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            starttime=starttime,
            endtime=endtime,
            aggregate_type=aggregate_type,
            window=window,
            max_samples=max_samples,
            tag_uui_ds=tag_uui_ds,
            from_units=from_units,
            to_units=to_units,
        )
    ).parsed
