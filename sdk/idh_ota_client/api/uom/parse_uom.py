from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.parse_uom_response_400 import ParseUomResponse400
from ...models.parse_uom_response_500 import ParseUomResponse500
from ...models.parse_uom_result import ParseUOMResult
from ...types import UNSET, Response


def _get_kwargs(
    *,
    uom_string: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uomString"] = uom_string

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/uom/parse",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]]:
    if response.status_code == 200:
        response_200 = ParseUOMResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ParseUomResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ParseUomResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    uom_string: str,
) -> Response[Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]]:
    """Parse a unit of measure (UOM) string into its components

     Parse a single unit of measure (UOM) string and display conversion information. Derived UOMs are not
    supported. .

    Args:
        uom_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]]
    """

    kwargs = _get_kwargs(
        uom_string=uom_string,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uom_string: str,
) -> Optional[Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]]:
    """Parse a unit of measure (UOM) string into its components

     Parse a single unit of measure (UOM) string and display conversion information. Derived UOMs are not
    supported. .

    Args:
        uom_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]
    """

    return sync_detailed(
        client=client,
        uom_string=uom_string,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uom_string: str,
) -> Response[Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]]:
    """Parse a unit of measure (UOM) string into its components

     Parse a single unit of measure (UOM) string and display conversion information. Derived UOMs are not
    supported. .

    Args:
        uom_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]]
    """

    kwargs = _get_kwargs(
        uom_string=uom_string,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uom_string: str,
) -> Optional[Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]]:
    """Parse a unit of measure (UOM) string into its components

     Parse a single unit of measure (UOM) string and display conversion information. Derived UOMs are not
    supported. .

    Args:
        uom_string (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ParseUOMResult, ParseUomResponse400, ParseUomResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            uom_string=uom_string,
        )
    ).parsed
