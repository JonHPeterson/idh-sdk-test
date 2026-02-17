from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_timeseries_uom_convert_response_400 import GetApiV1TimeseriesUomConvertResponse400
from ...models.get_api_v1_timeseries_uom_convert_response_500 import GetApiV1TimeseriesUomConvertResponse500
from ...types import UNSET, Response


def _get_kwargs(
    *,
    value: float,
    from_uom: str,
    to_uom: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["value"] = value

    params["fromUOM"] = from_uom

    params["toUOM"] = to_uom

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/timeseries/uom/convert",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]]:
    if response.status_code == 200:
        response_200 = cast(float, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = GetApiV1TimeseriesUomConvertResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetApiV1TimeseriesUomConvertResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    value: float,
    from_uom: str,
    to_uom: str,
) -> Response[Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]]:
    r"""Convert a value from one unit of measure (UOM) to another

     Convert a value from one unit of measure (UOM) to another. For example, convert 100 from \"km/h\" to
    \"m/s\".

    Args:
        value (float):
        from_uom (str):
        to_uom (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]]
    """

    kwargs = _get_kwargs(
        value=value,
        from_uom=from_uom,
        to_uom=to_uom,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    value: float,
    from_uom: str,
    to_uom: str,
) -> Optional[Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]]:
    r"""Convert a value from one unit of measure (UOM) to another

     Convert a value from one unit of measure (UOM) to another. For example, convert 100 from \"km/h\" to
    \"m/s\".

    Args:
        value (float):
        from_uom (str):
        to_uom (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]
    """

    return sync_detailed(
        client=client,
        value=value,
        from_uom=from_uom,
        to_uom=to_uom,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    value: float,
    from_uom: str,
    to_uom: str,
) -> Response[Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]]:
    r"""Convert a value from one unit of measure (UOM) to another

     Convert a value from one unit of measure (UOM) to another. For example, convert 100 from \"km/h\" to
    \"m/s\".

    Args:
        value (float):
        from_uom (str):
        to_uom (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]]
    """

    kwargs = _get_kwargs(
        value=value,
        from_uom=from_uom,
        to_uom=to_uom,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    value: float,
    from_uom: str,
    to_uom: str,
) -> Optional[Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]]:
    r"""Convert a value from one unit of measure (UOM) to another

     Convert a value from one unit of measure (UOM) to another. For example, convert 100 from \"km/h\" to
    \"m/s\".

    Args:
        value (float):
        from_uom (str):
        to_uom (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesUomConvertResponse400, GetApiV1TimeseriesUomConvertResponse500, float]
    """

    return (
        await asyncio_detailed(
            client=client,
            value=value,
            from_uom=from_uom,
            to_uom=to_uom,
        )
    ).parsed
