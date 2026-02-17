from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_metadata_sources_statesets_source_uuid_response_200 import (
    GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200,
)
from ...models.get_api_v1_metadata_sources_statesets_source_uuid_response_404 import (
    GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404,
)
from ...models.get_api_v1_metadata_sources_statesets_source_uuid_response_500 import (
    GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500,
)
from ...types import Response


def _get_kwargs(
    source_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/metadata/sources/statesets/{source_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500,
    ]
]:
    """Get a map of all state sets by id and name for a specific source

     Get a map of all state sets by id and name for a specific source

    Args:
        source_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200, GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404, GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500]]
    """

    kwargs = _get_kwargs(
        source_uuid=source_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500,
    ]
]:
    """Get a map of all state sets by id and name for a specific source

     Get a map of all state sets by id and name for a specific source

    Args:
        source_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200, GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404, GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500]
    """

    return sync_detailed(
        source_uuid=source_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500,
    ]
]:
    """Get a map of all state sets by id and name for a specific source

     Get a map of all state sets by id and name for a specific source

    Args:
        source_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200, GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404, GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500]]
    """

    kwargs = _get_kwargs(
        source_uuid=source_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500,
    ]
]:
    """Get a map of all state sets by id and name for a specific source

     Get a map of all state sets by id and name for a specific source

    Args:
        source_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1MetadataSourcesStatesetsSourceUUIDResponse200, GetApiV1MetadataSourcesStatesetsSourceUUIDResponse404, GetApiV1MetadataSourcesStatesetsSourceUUIDResponse500]
    """

    return (
        await asyncio_detailed(
            source_uuid=source_uuid,
            client=client,
        )
    ).parsed
