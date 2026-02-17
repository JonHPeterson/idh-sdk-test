from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_timeseries_uom_parse_uom_uom_string_response_400 import (
    GetApiV1TimeseriesUomParseUomUomStringResponse400,
)
from ...models.get_api_v1_timeseries_uom_parse_uom_uom_string_response_500 import (
    GetApiV1TimeseriesUomParseUomUomStringResponse500,
)
from ...models.parse_uom_result import ParseUOMResult
from ...types import Response


def _get_kwargs(
    uom_string: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/timeseries/uom/parse_uom/{uom_string}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetApiV1TimeseriesUomParseUomUomStringResponse400,
        GetApiV1TimeseriesUomParseUomUomStringResponse500,
        ParseUOMResult,
    ]
]:
    if response.status_code == 200:
        response_200 = ParseUOMResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetApiV1TimeseriesUomParseUomUomStringResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetApiV1TimeseriesUomParseUomUomStringResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetApiV1TimeseriesUomParseUomUomStringResponse400,
        GetApiV1TimeseriesUomParseUomUomStringResponse500,
        ParseUOMResult,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uom_string: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetApiV1TimeseriesUomParseUomUomStringResponse400,
        GetApiV1TimeseriesUomParseUomUomStringResponse500,
        ParseUOMResult,
    ]
]:
    """Parse a unit of measure (UOM) string into its components

     Parse a single unit of measure (UOM) string and display conversion information. Derived UOMs are not
    supported. .

    Args:
        uom_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesUomParseUomUomStringResponse400, GetApiV1TimeseriesUomParseUomUomStringResponse500, ParseUOMResult]]
    """

    kwargs = _get_kwargs(
        uom_string=uom_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uom_string: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetApiV1TimeseriesUomParseUomUomStringResponse400,
        GetApiV1TimeseriesUomParseUomUomStringResponse500,
        ParseUOMResult,
    ]
]:
    """Parse a unit of measure (UOM) string into its components

     Parse a single unit of measure (UOM) string and display conversion information. Derived UOMs are not
    supported. .

    Args:
        uom_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesUomParseUomUomStringResponse400, GetApiV1TimeseriesUomParseUomUomStringResponse500, ParseUOMResult]
    """

    return sync_detailed(
        uom_string=uom_string,
        client=client,
    ).parsed


async def asyncio_detailed(
    uom_string: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetApiV1TimeseriesUomParseUomUomStringResponse400,
        GetApiV1TimeseriesUomParseUomUomStringResponse500,
        ParseUOMResult,
    ]
]:
    """Parse a unit of measure (UOM) string into its components

     Parse a single unit of measure (UOM) string and display conversion information. Derived UOMs are not
    supported. .

    Args:
        uom_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1TimeseriesUomParseUomUomStringResponse400, GetApiV1TimeseriesUomParseUomUomStringResponse500, ParseUOMResult]]
    """

    kwargs = _get_kwargs(
        uom_string=uom_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uom_string: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetApiV1TimeseriesUomParseUomUomStringResponse400,
        GetApiV1TimeseriesUomParseUomUomStringResponse500,
        ParseUOMResult,
    ]
]:
    """Parse a unit of measure (UOM) string into its components

     Parse a single unit of measure (UOM) string and display conversion information. Derived UOMs are not
    supported. .

    Args:
        uom_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1TimeseriesUomParseUomUomStringResponse400, GetApiV1TimeseriesUomParseUomUomStringResponse500, ParseUOMResult]
    """

    return (
        await asyncio_detailed(
            uom_string=uom_string,
            client=client,
        )
    ).parsed
