from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_response import AssetResponse
from ...models.get_asset_by_uuid_response_400 import GetAssetByUUIDResponse400
from ...models.get_asset_by_uuid_response_500 import GetAssetByUUIDResponse500
from ...types import Response


def _get_kwargs(
    asset_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/assets/{asset_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]]:
    if response.status_code == 200:
        response_200 = AssetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAssetByUUIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetAssetByUUIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]]:
    """Get asset by UUID

     Get asset by UUID

    Args:
        asset_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]]
    """

    kwargs = _get_kwargs(
        asset_uuid=asset_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]]:
    """Get asset by UUID

     Get asset by UUID

    Args:
        asset_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]
    """

    return sync_detailed(
        asset_uuid=asset_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]]:
    """Get asset by UUID

     Get asset by UUID

    Args:
        asset_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]]
    """

    kwargs = _get_kwargs(
        asset_uuid=asset_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]]:
    """Get asset by UUID

     Get asset by UUID

    Args:
        asset_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssetResponse, GetAssetByUUIDResponse400, GetAssetByUUIDResponse500]
    """

    return (
        await asyncio_detailed(
            asset_uuid=asset_uuid,
            client=client,
        )
    ).parsed
