from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_uom_uoms_response_500 import GetApiV1UomUomsResponse500
from ...models.uom_info_table import UOMInfoTable
from ...types import UNSET, Response


def _get_kwargs(
    *,
    filter_string: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterString"] = filter_string

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/uom/uoms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetApiV1UomUomsResponse500, UOMInfoTable]]:
    if response.status_code == 200:
        response_200 = UOMInfoTable.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = GetApiV1UomUomsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetApiV1UomUomsResponse500, UOMInfoTable]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    filter_string: str,
) -> Response[Union[GetApiV1UomUomsResponse500, UOMInfoTable]]:
    """Get list of supported unit of measures (UOMs) for timeseries queries

     Get list of supported unit of measures (UOMs) for timeseries queries. Optionally filter by a search
    string that matches either the UOM name, symbol, or alias.

    Args:
        filter_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1UomUomsResponse500, UOMInfoTable]]
    """

    kwargs = _get_kwargs(
        filter_string=filter_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    filter_string: str,
) -> Optional[Union[GetApiV1UomUomsResponse500, UOMInfoTable]]:
    """Get list of supported unit of measures (UOMs) for timeseries queries

     Get list of supported unit of measures (UOMs) for timeseries queries. Optionally filter by a search
    string that matches either the UOM name, symbol, or alias.

    Args:
        filter_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1UomUomsResponse500, UOMInfoTable]
    """

    return sync_detailed(
        client=client,
        filter_string=filter_string,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    filter_string: str,
) -> Response[Union[GetApiV1UomUomsResponse500, UOMInfoTable]]:
    """Get list of supported unit of measures (UOMs) for timeseries queries

     Get list of supported unit of measures (UOMs) for timeseries queries. Optionally filter by a search
    string that matches either the UOM name, symbol, or alias.

    Args:
        filter_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1UomUomsResponse500, UOMInfoTable]]
    """

    kwargs = _get_kwargs(
        filter_string=filter_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    filter_string: str,
) -> Optional[Union[GetApiV1UomUomsResponse500, UOMInfoTable]]:
    """Get list of supported unit of measures (UOMs) for timeseries queries

     Get list of supported unit of measures (UOMs) for timeseries queries. Optionally filter by a search
    string that matches either the UOM name, symbol, or alias.

    Args:
        filter_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1UomUomsResponse500, UOMInfoTable]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_string=filter_string,
        )
    ).parsed
