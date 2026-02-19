from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_source_by_name_or_uuid_response_404 import GetSourceByNameOrUuidResponse404
from ...models.get_source_by_name_or_uuid_response_500 import GetSourceByNameOrUuidResponse500
from ...models.sources_response import SourcesResponse
from ...types import Response


def _get_kwargs(
    name_or_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/metadata/sources/{name_or_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]]:
    if response.status_code == 200:
        response_200 = SourcesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetSourceByNameOrUuidResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSourceByNameOrUuidResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name_or_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]]:
    """Get source by Name or UUID

     Get details for a specific source

    Args:
        name_or_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]]
    """

    kwargs = _get_kwargs(
        name_or_uuid=name_or_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name_or_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]]:
    """Get source by Name or UUID

     Get details for a specific source

    Args:
        name_or_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]
    """

    return sync_detailed(
        name_or_uuid=name_or_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    name_or_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]]:
    """Get source by Name or UUID

     Get details for a specific source

    Args:
        name_or_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]]
    """

    kwargs = _get_kwargs(
        name_or_uuid=name_or_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name_or_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]]:
    """Get source by Name or UUID

     Get details for a specific source

    Args:
        name_or_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSourceByNameOrUuidResponse404, GetSourceByNameOrUuidResponse500, SourcesResponse]
    """

    return (
        await asyncio_detailed(
            name_or_uuid=name_or_uuid,
            client=client,
        )
    ).parsed
