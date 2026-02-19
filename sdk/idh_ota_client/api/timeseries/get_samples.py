from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_samples_response_500 import GetSamplesResponse500
from ...models.time_series_samples_response import TimeSeriesSamplesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    starttime: str,
    endtime: str,
    max_samples: int,
    tag_uuids: list[str],
    from_uoms: Union[Unset, list[str]] = UNSET,
    to_uoms: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["starttime"] = starttime

    params["endtime"] = endtime

    params["maxSamples"] = max_samples

    json_tag_uuids = tag_uuids

    params["tagUuids"] = json_tag_uuids

    json_from_uoms: Union[Unset, list[str]] = UNSET
    if not isinstance(from_uoms, Unset):
        json_from_uoms = from_uoms

    params["fromUoms"] = json_from_uoms

    json_to_uoms: Union[Unset, list[str]] = UNSET
    if not isinstance(to_uoms, Unset):
        json_to_uoms = to_uoms

    params["toUoms"] = json_to_uoms

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/timeseries/samples",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetSamplesResponse500, TimeSeriesSamplesResponse]]:
    if response.status_code == 200:
        response_200 = TimeSeriesSamplesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = GetSamplesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetSamplesResponse500, TimeSeriesSamplesResponse]]:
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
    max_samples: int,
    tag_uuids: list[str],
    from_uoms: Union[Unset, list[str]] = UNSET,
    to_uoms: Union[Unset, list[str]] = UNSET,
) -> Response[Union[GetSamplesResponse500, TimeSeriesSamplesResponse]]:
    r"""Get timeseries samples for tags

     Get samples (recorded data) for timeseries tags. Supports both JSON and binary (MessagePack)
    formats. For binary, set Accept header to \"application/msgpack\"

    Args:
        starttime (str):
        endtime (str):
        max_samples (int):
        tag_uuids (list[str]):
        from_uoms (Union[Unset, list[str]]):
        to_uoms (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSamplesResponse500, TimeSeriesSamplesResponse]]
    """

    kwargs = _get_kwargs(
        starttime=starttime,
        endtime=endtime,
        max_samples=max_samples,
        tag_uuids=tag_uuids,
        from_uoms=from_uoms,
        to_uoms=to_uoms,
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
    max_samples: int,
    tag_uuids: list[str],
    from_uoms: Union[Unset, list[str]] = UNSET,
    to_uoms: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[GetSamplesResponse500, TimeSeriesSamplesResponse]]:
    r"""Get timeseries samples for tags

     Get samples (recorded data) for timeseries tags. Supports both JSON and binary (MessagePack)
    formats. For binary, set Accept header to \"application/msgpack\"

    Args:
        starttime (str):
        endtime (str):
        max_samples (int):
        tag_uuids (list[str]):
        from_uoms (Union[Unset, list[str]]):
        to_uoms (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSamplesResponse500, TimeSeriesSamplesResponse]
    """

    return sync_detailed(
        client=client,
        starttime=starttime,
        endtime=endtime,
        max_samples=max_samples,
        tag_uuids=tag_uuids,
        from_uoms=from_uoms,
        to_uoms=to_uoms,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    starttime: str,
    endtime: str,
    max_samples: int,
    tag_uuids: list[str],
    from_uoms: Union[Unset, list[str]] = UNSET,
    to_uoms: Union[Unset, list[str]] = UNSET,
) -> Response[Union[GetSamplesResponse500, TimeSeriesSamplesResponse]]:
    r"""Get timeseries samples for tags

     Get samples (recorded data) for timeseries tags. Supports both JSON and binary (MessagePack)
    formats. For binary, set Accept header to \"application/msgpack\"

    Args:
        starttime (str):
        endtime (str):
        max_samples (int):
        tag_uuids (list[str]):
        from_uoms (Union[Unset, list[str]]):
        to_uoms (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSamplesResponse500, TimeSeriesSamplesResponse]]
    """

    kwargs = _get_kwargs(
        starttime=starttime,
        endtime=endtime,
        max_samples=max_samples,
        tag_uuids=tag_uuids,
        from_uoms=from_uoms,
        to_uoms=to_uoms,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    starttime: str,
    endtime: str,
    max_samples: int,
    tag_uuids: list[str],
    from_uoms: Union[Unset, list[str]] = UNSET,
    to_uoms: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[GetSamplesResponse500, TimeSeriesSamplesResponse]]:
    r"""Get timeseries samples for tags

     Get samples (recorded data) for timeseries tags. Supports both JSON and binary (MessagePack)
    formats. For binary, set Accept header to \"application/msgpack\"

    Args:
        starttime (str):
        endtime (str):
        max_samples (int):
        tag_uuids (list[str]):
        from_uoms (Union[Unset, list[str]]):
        to_uoms (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSamplesResponse500, TimeSeriesSamplesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            starttime=starttime,
            endtime=endtime,
            max_samples=max_samples,
            tag_uuids=tag_uuids,
            from_uoms=from_uoms,
            to_uoms=to_uoms,
        )
    ).parsed
