import pytest
from client.api_client import APIClient
from data.payloads import create_post_payload

@pytest.fixture(scope="session")
def api_client():
    return APIClient()

@pytest.fixture
def created_post(api_client):
    # Validate POST works
    res = api_client.post("/posts", create_post_payload())
    assert res.status_code == 201

    # JSONPlaceholder does not persist data
    # Always return a REAL existing post ID
    return 1

