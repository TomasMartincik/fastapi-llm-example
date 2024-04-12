from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app
from tests.mocks.mock_llm_provider import MockLLMProvider


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture
def mock_llm_provider_success():
    return MockLLMProvider(behavior="succeed")


@pytest.fixture
def mock_llm_provider_none():
    return MockLLMProvider(behavior="fail_with_none")


@pytest.fixture
def mock_llm_provider_exception():
    return MockLLMProvider(behavior="fail_with_exception")
