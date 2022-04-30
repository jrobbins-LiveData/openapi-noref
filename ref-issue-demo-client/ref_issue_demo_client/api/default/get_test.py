from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_test_page import GetTestPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, GetTestPage] = UNSET,
) -> Dict[str, Any]:
    url = "{}/test".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_page: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(page, Unset):
        json_page = page.to_dict() if page else None

    if not isinstance(json_page, Unset) and json_page is not None:
        params.update(json_page)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[str]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, GetTestPage] = UNSET,
) -> Response[List[str]]:
    """test

     Returns a list

    Args:
        page (Union[Unset, None, GetTestPage]):

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, None, GetTestPage] = UNSET,
) -> Optional[List[str]]:
    """test

     Returns a list

    Args:
        page (Union[Unset, None, GetTestPage]):

    Returns:
        Response[List[str]]
    """

    return sync_detailed(
        client=client,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, GetTestPage] = UNSET,
) -> Response[List[str]]:
    """test

     Returns a list

    Args:
        page (Union[Unset, None, GetTestPage]):

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, GetTestPage] = UNSET,
) -> Optional[List[str]]:
    """test

     Returns a list

    Args:
        page (Union[Unset, None, GetTestPage]):

    Returns:
        Response[List[str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
        )
    ).parsed
