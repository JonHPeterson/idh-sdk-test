from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tag_info_response_400 import GetTagInfoResponse400
from ...models.get_tag_info_response_404 import GetTagInfoResponse404
from ...models.get_tag_info_response_500 import GetTagInfoResponse500
from ...models.ts_get_tag_info_response import TSGetTagInfoResponse
from ...types import Response


def _get_kwargs(
    tag_uuid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/timeseries/taginfo/{tag_uuid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]]:
    if response.status_code == 200:
        response_200 = TSGetTagInfoResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetTagInfoResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetTagInfoResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetTagInfoResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tag_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]]:
    """Get timeseries tag info by tag UUID

     Get timeseries tag info by tag UUID

    Args:
        tag_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]]
    """

    kwargs = _get_kwargs(
        tag_uuid=tag_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]]:
    """Get timeseries tag info by tag UUID

     Get timeseries tag info by tag UUID

    Args:
        tag_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]
    """

    return sync_detailed(
        tag_uuid=tag_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    tag_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]]:
    """Get timeseries tag info by tag UUID

     Get timeseries tag info by tag UUID

    Args:
        tag_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]]
    """

    kwargs = _get_kwargs(
        tag_uuid=tag_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]]:
    """Get timeseries tag info by tag UUID

     Get timeseries tag info by tag UUID

    Args:
        tag_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTagInfoResponse400, GetTagInfoResponse404, GetTagInfoResponse500, TSGetTagInfoResponse]
    """

    return (
        await asyncio_detailed(
            tag_uuid=tag_uuid,
            client=client,
        )
    ).parsed
