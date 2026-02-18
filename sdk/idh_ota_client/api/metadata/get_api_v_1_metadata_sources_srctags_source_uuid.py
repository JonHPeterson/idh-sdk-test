from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_metadata_sources_srctags_source_uuid_response_400 import (
    GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400,
)
from ...models.get_api_v1_metadata_sources_srctags_source_uuid_response_404 import (
    GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404,
)
from ...models.get_api_v1_metadata_sources_srctags_source_uuid_response_500 import (
    GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500,
)
from ...models.source_tag_records import SourceTagRecords
from ...types import UNSET, Response


def _get_kwargs(
    source_uuid: str,
    *,
    query: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/metadata/sources/srctags/{source_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500,
        SourceTagRecords,
    ]
]:
    if response.status_code == 200:
        response_200 = SourceTagRecords.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500,
        SourceTagRecords,
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
    query: str,
) -> Response[
    Union[
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500,
        SourceTagRecords,
    ]
]:
    """Get source data tags for a specific source using a tag query

     Returns all source data tags for a specific source matching the query. Use [{}] as the query to
    return all tags for the source.

    Args:
        source_uuid (str):
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400, GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404, GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500, SourceTagRecords]]
    """

    kwargs = _get_kwargs(
        source_uuid=source_uuid,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    query: str,
) -> Optional[
    Union[
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500,
        SourceTagRecords,
    ]
]:
    """Get source data tags for a specific source using a tag query

     Returns all source data tags for a specific source matching the query. Use [{}] as the query to
    return all tags for the source.

    Args:
        source_uuid (str):
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400, GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404, GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500, SourceTagRecords]
    """

    return sync_detailed(
        source_uuid=source_uuid,
        client=client,
        query=query,
    ).parsed


async def asyncio_detailed(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    query: str,
) -> Response[
    Union[
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500,
        SourceTagRecords,
    ]
]:
    """Get source data tags for a specific source using a tag query

     Returns all source data tags for a specific source matching the query. Use [{}] as the query to
    return all tags for the source.

    Args:
        source_uuid (str):
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400, GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404, GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500, SourceTagRecords]]
    """

    kwargs = _get_kwargs(
        source_uuid=source_uuid,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_uuid: str,
    *,
    client: AuthenticatedClient,
    query: str,
) -> Optional[
    Union[
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404,
        GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500,
        SourceTagRecords,
    ]
]:
    """Get source data tags for a specific source using a tag query

     Returns all source data tags for a specific source matching the query. Use [{}] as the query to
    return all tags for the source.

    Args:
        source_uuid (str):
        query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiV1MetadataSourcesSrctagsSourceUUIDResponse400, GetApiV1MetadataSourcesSrctagsSourceUUIDResponse404, GetApiV1MetadataSourcesSrctagsSourceUUIDResponse500, SourceTagRecords]
    """

    return (
        await asyncio_detailed(
            source_uuid=source_uuid,
            client=client,
            query=query,
        )
    ).parsed
