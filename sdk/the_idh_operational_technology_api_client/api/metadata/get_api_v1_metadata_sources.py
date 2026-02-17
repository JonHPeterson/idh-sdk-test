from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_metadata_sources_response_200 import GetApiV1MetadataSourcesResponse200
from ...models.get_api_v1_metadata_sources_response_404 import GetApiV1MetadataSourcesResponse404
from ...models.get_api_v1_metadata_sources_response_500 import GetApiV1MetadataSourcesResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/metadata/sources",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]
]:
    if response.status_code == 200:
        response_200 = GetApiV1MetadataSourcesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetApiV1MetadataSourcesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetApiV1MetadataSourcesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]
]:
    """List all sources

     Get list of all PI sources

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]
]:
    """List all sources

     Get list of all PI sources

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]
]:
    """List all sources

     Get list of all PI sources

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]
]:
    """List all sources

     Get list of all PI sources

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1MetadataSourcesResponse200, GetApiV1MetadataSourcesResponse404, GetApiV1MetadataSourcesResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
