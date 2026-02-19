from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_prefixes_response_500 import ListPrefixesResponse500
from ...models.prefix_list_response import PrefixListResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/uom/prefixes",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ListPrefixesResponse500, PrefixListResponse]]:
    if response.status_code == 200:
        response_200 = PrefixListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = ListPrefixesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ListPrefixesResponse500, PrefixListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ListPrefixesResponse500, PrefixListResponse]]:
    """Get list of supported unit of measure (UOM) prefixes for timeseries queries

     Get list of supported unit of measure (UOM) prefixes for timeseries queries such as kilo, milli,
    micro, etc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListPrefixesResponse500, PrefixListResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ListPrefixesResponse500, PrefixListResponse]]:
    """Get list of supported unit of measure (UOM) prefixes for timeseries queries

     Get list of supported unit of measure (UOM) prefixes for timeseries queries such as kilo, milli,
    micro, etc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListPrefixesResponse500, PrefixListResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ListPrefixesResponse500, PrefixListResponse]]:
    """Get list of supported unit of measure (UOM) prefixes for timeseries queries

     Get list of supported unit of measure (UOM) prefixes for timeseries queries such as kilo, milli,
    micro, etc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListPrefixesResponse500, PrefixListResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ListPrefixesResponse500, PrefixListResponse]]:
    """Get list of supported unit of measure (UOM) prefixes for timeseries queries

     Get list of supported unit of measure (UOM) prefixes for timeseries queries such as kilo, milli,
    micro, etc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListPrefixesResponse500, PrefixListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
