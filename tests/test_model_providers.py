# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from .utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = [
        {
            "provider": "OpenAI",
            "api_key": "api_key",
            "deployment_name": "deployment_name",
            "endpoint": "endpoint",
            "scope": "Organization",
            "organization": 1,
            "created_by": 1,
            "created_at": "2024-01-15T09:30:00Z",
            "updated_at": "2024-01-15T09:30:00Z",
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "provider": None,
                "api_key": None,
                "deployment_name": None,
                "endpoint": None,
                "scope": None,
                "organization": "integer",
                "created_by": "integer",
                "created_at": "datetime",
                "updated_at": "datetime",
            }
        },
    )
    response = client.model_providers.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.model_providers.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "provider": "OpenAI",
        "api_key": "api_key",
        "deployment_name": "deployment_name",
        "endpoint": "endpoint",
        "scope": "Organization",
        "organization": 1,
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "provider": None,
        "api_key": None,
        "deployment_name": None,
        "endpoint": None,
        "scope": None,
        "organization": "integer",
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
    }
    response = client.model_providers.create(provider="OpenAI")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.model_providers.create(provider="OpenAI")
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "provider": "OpenAI",
        "api_key": "api_key",
        "deployment_name": "deployment_name",
        "endpoint": "endpoint",
        "scope": "Organization",
        "organization": 1,
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "provider": None,
        "api_key": None,
        "deployment_name": None,
        "endpoint": None,
        "scope": None,
        "organization": "integer",
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
    }
    response = client.model_providers.get(pk=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.model_providers.get(pk=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.model_providers.delete(pk=1) is None  # type: ignore[func-returns-value]

    assert await async_client.model_providers.delete(pk=1) is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "provider": "OpenAI",
        "api_key": "api_key",
        "deployment_name": "deployment_name",
        "endpoint": "endpoint",
        "scope": "Organization",
        "organization": 1,
        "created_by": 1,
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
    }
    expected_types: typing.Any = {
        "provider": None,
        "api_key": None,
        "deployment_name": None,
        "endpoint": None,
        "scope": None,
        "organization": "integer",
        "created_by": "integer",
        "created_at": "datetime",
        "updated_at": "datetime",
    }
    response = client.model_providers.update(pk=1, provider="OpenAI")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.model_providers.update(pk=1, provider="OpenAI")
    validate_response(async_response, expected_response, expected_types)
