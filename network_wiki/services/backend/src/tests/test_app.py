import pytest
import pytest_asyncio
from httpx import AsyncClient

BASE_URL = "http://0.0.0.0:8000"

@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(base_url="http://0.0.0.0:8000") as client:
        yield client

@pytest.mark.asyncio
async def test_ping(async_client):
    response = await async_client.get(f"{BASE_URL}/uso/uso")
    assert response.status_code == 200

