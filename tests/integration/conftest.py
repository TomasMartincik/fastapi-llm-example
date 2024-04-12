import pytest_asyncio
from httpx import AsyncClient


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(base_url="http://app:8000") as client:
        yield client
