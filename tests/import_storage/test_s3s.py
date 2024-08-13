# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from ..utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = [
        {
            "id": 1,
            "synchronizable": True,
            "presign": True,
            "last_sync": "2024-01-15T09:30:00Z",
            "last_sync_count": 1,
            "last_sync_job": "last_sync_job",
            "status": "initialized",
            "traceback": "traceback",
            "meta": {"key": "value"},
            "title": "title",
            "description": "description",
            "created_at": "2024-01-15T09:30:00Z",
            "bucket": "bucket",
            "prefix": "prefix",
            "regex_filter": "regex_filter",
            "use_blob_urls": True,
            "region_name": "region_name",
            "external_id": "external_id",
            "role_arn": "role_arn",
            "s3_endpoint": "s3_endpoint",
            "presign_ttl": 1,
            "recursive_scan": True,
            "project": 1,
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "id": "integer",
                "synchronizable": None,
                "presign": None,
                "last_sync": "datetime",
                "last_sync_count": "integer",
                "last_sync_job": None,
                "status": None,
                "traceback": None,
                "meta": ("dict", {0: (None, None)}),
                "title": None,
                "description": None,
                "created_at": "datetime",
                "bucket": None,
                "prefix": None,
                "regex_filter": None,
                "use_blob_urls": None,
                "region_name": None,
                "external_id": None,
                "role_arn": None,
                "s3_endpoint": None,
                "presign_ttl": "integer",
                "recursive_scan": None,
                "project": "integer",
            }
        },
    )
    response = client.import_storage.s3s.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.s3s.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "synchronizable": True,
        "presign": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"key": "value"},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "bucket": "bucket",
        "prefix": "prefix",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "region_name": "region_name",
        "external_id": "external_id",
        "role_arn": "role_arn",
        "s3_endpoint": "s3_endpoint",
        "presign_ttl": 1,
        "recursive_scan": True,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "synchronizable": None,
        "presign": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "bucket": None,
        "prefix": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "region_name": None,
        "external_id": None,
        "role_arn": None,
        "s3_endpoint": None,
        "presign_ttl": "integer",
        "recursive_scan": None,
        "project": "integer",
    }
    response = client.import_storage.s3s.create()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.s3s.create()
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "synchronizable": True,
        "presign": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"key": "value"},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "bucket": "bucket",
        "prefix": "prefix",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "region_name": "region_name",
        "external_id": "external_id",
        "role_arn": "role_arn",
        "s3_endpoint": "s3_endpoint",
        "presign_ttl": 1,
        "recursive_scan": True,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "synchronizable": None,
        "presign": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "bucket": None,
        "prefix": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "region_name": None,
        "external_id": None,
        "role_arn": None,
        "s3_endpoint": None,
        "presign_ttl": "integer",
        "recursive_scan": None,
        "project": "integer",
    }
    response = client.import_storage.s3s.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.s3s.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.import_storage.s3s.delete(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.import_storage.s3s.delete(id=1) is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "synchronizable": True,
        "presign": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"key": "value"},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "bucket": "bucket",
        "prefix": "prefix",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "region_name": "region_name",
        "external_id": "external_id",
        "role_arn": "role_arn",
        "s3_endpoint": "s3_endpoint",
        "presign_ttl": 1,
        "recursive_scan": True,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "synchronizable": None,
        "presign": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "bucket": None,
        "prefix": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "region_name": None,
        "external_id": None,
        "role_arn": None,
        "s3_endpoint": None,
        "presign_ttl": "integer",
        "recursive_scan": None,
        "project": "integer",
    }
    response = client.import_storage.s3s.update(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.s3s.update(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_validate(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.import_storage.s3s.validate() is None  # type: ignore[func-returns-value]

    assert await async_client.import_storage.s3s.validate() is None  # type: ignore[func-returns-value]


async def test_sync(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response: typing.Any = {
        "id": 1,
        "synchronizable": True,
        "presign": True,
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"key": "value"},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "bucket": "bucket",
        "prefix": "prefix",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "region_name": "region_name",
        "external_id": "external_id",
        "role_arn": "role_arn",
        "s3_endpoint": "s3_endpoint",
        "presign_ttl": 1,
        "recursive_scan": True,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "synchronizable": None,
        "presign": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "bucket": None,
        "prefix": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "region_name": None,
        "external_id": None,
        "role_arn": None,
        "s3_endpoint": None,
        "presign_ttl": "integer",
        "recursive_scan": None,
        "project": "integer",
    }
    response = client.import_storage.s3s.sync(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.s3s.sync(id=1)
    validate_response(async_response, expected_response, expected_types)
