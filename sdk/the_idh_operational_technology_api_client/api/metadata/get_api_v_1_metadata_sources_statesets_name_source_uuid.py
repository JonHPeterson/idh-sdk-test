from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_metadata_sources_statesets_name_source_uuid_response_404 import (
    GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404,
)
from ...models.get_api_v1_metadata_sources_statesets_name_source_uuid_response_500 import (
    GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500,
)
from ...models.md_state_set import MDStateSet
from ...types import UNSET, Response


def _get_kwargs(
    source_uuid: str,
    *,
    name: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/metadata/sources/statesets/name/{source_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500,
        MDStateSet,
    ]
]:
    if response.status_code == 200:
        response_200 = MDStateSet.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500,
        MDStateSet,
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
    name: str,
) -> Response[
    Union[
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500,
        MDStateSet,
    ]
]:
    """Get state set for a source by Name

     Get details for a specific state set by Name

    Args:
        source_uuid (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404, GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500, MDStateSet]]
    """

    kwargs = _get_kwargs(
        source_uuid=source_uuid,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> Optional[
    Union[
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500,
        MDStateSet,
    ]
]:
    """Get state set for a source by Name

     Get details for a specific state set by Name

    Args:
        source_uuid (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404, GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500, MDStateSet]
    """

    return sync_detailed(
        source_uuid=source_uuid,
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> Response[
    Union[
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500,
        MDStateSet,
    ]
]:
    """Get state set for a source by Name

     Get details for a specific state set by Name

    Args:
        source_uuid (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404, GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500, MDStateSet]]
    """

    kwargs = _get_kwargs(
        source_uuid=source_uuid,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    name: str,
) -> Optional[
    Union[
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404,
        GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500,
        MDStateSet,
    ]
]:
    """Get state set for a source by Name

     Get details for a specific state set by Name

    Args:
        source_uuid (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse404, GetApiV1MetadataSourcesStatesetsNameSourceUUIDResponse500, MDStateSet]
    """

    return (
        await asyncio_detailed(
            source_uuid=source_uuid,
            client=client,
            name=name,
        )
    ).parsed
