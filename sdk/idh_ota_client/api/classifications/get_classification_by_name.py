from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.classification_response import ClassificationResponse
from ...models.get_classification_by_name_response_400 import GetClassificationByNameResponse400
from ...models.get_classification_by_name_response_500 import GetClassificationByNameResponse500
from ...types import Response


def _get_kwargs(
    name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/classifications{name}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]]:
    if response.status_code == 200:
        response_200 = ClassificationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetClassificationByNameResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetClassificationByNameResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]]:
    """Get classification by name

     Get classification by name

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]]:
    """Get classification by name

     Get classification by name

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]]:
    """Get classification by name

     Get classification by name

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]]:
    """Get classification by name

     Get classification by name

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClassificationResponse, GetClassificationByNameResponse400, GetClassificationByNameResponse500]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
