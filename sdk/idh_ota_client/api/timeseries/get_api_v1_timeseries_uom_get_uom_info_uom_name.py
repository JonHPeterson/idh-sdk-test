from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_timeseries_uom_get_uom_info_uom_name_response_404 import (
    GetApiV1TimeseriesUomGetUomInfoUomNameResponse404,
)
from ...models.get_api_v1_timeseries_uom_get_uom_info_uom_name_response_500 import (
    GetApiV1TimeseriesUomGetUomInfoUomNameResponse500,
)
from ...models.uom_info import UOMInfo
from ...types import Response


def _get_kwargs(
    uom_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/timeseries/uom/get_uom_info/{uom_name}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]
]:
    if response.status_code == 200:
        response_200 = UOMInfo.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetApiV1TimeseriesUomGetUomInfoUomNameResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetApiV1TimeseriesUomGetUomInfoUomNameResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uom_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]
]:
    """Get unit of measure (UOM) details by name for timeseries queries

     Get unit of measure (UOM) details by name for timeseries queries. These are single UOMs, not derived
    UOMs like m/second.

    Args:
        uom_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]]
    """

    kwargs = _get_kwargs(
        uom_name=uom_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uom_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]
]:
    """Get unit of measure (UOM) details by name for timeseries queries

     Get unit of measure (UOM) details by name for timeseries queries. These are single UOMs, not derived
    UOMs like m/second.

    Args:
        uom_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]
    """

    return sync_detailed(
        uom_name=uom_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    uom_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]
]:
    """Get unit of measure (UOM) details by name for timeseries queries

     Get unit of measure (UOM) details by name for timeseries queries. These are single UOMs, not derived
    UOMs like m/second.

    Args:
        uom_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]]
    """

    kwargs = _get_kwargs(
        uom_name=uom_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uom_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]
]:
    """Get unit of measure (UOM) details by name for timeseries queries

     Get unit of measure (UOM) details by name for timeseries queries. These are single UOMs, not derived
    UOMs like m/second.

    Args:
        uom_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesUomGetUomInfoUomNameResponse404, GetApiV1TimeseriesUomGetUomInfoUomNameResponse500, UOMInfo]
    """

    return (
        await asyncio_detailed(
            uom_name=uom_name,
            client=client,
        )
    ).parsed
