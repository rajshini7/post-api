import json

from data.payloads import (
    create_post_payload,
    put_post_payload,
    patch_post_payload
)


def test_create_post(api_client):
    payload = create_post_payload()
    print("\nPOST payload:", json.dumps(payload, indent=2))

    response = api_client.post("/posts", payload)
    print("POST response:", response.json())

    assert response.status_code == 201



def test_get_post(api_client, created_post):
    response = api_client.get(f"/posts/{created_post}")
    assert response.status_code == 200

    body = response.json()
    print("\nGET response:", body)

    # Known JSONPlaceholder post 1
    assert body["id"] == 1
    assert body["userId"] == 1
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)



def test_put_post(api_client, created_post):
    payload = put_post_payload(created_post)
    print("\nPUT payload:", payload)

    response = api_client.put(f"/posts/{created_post}", payload)
    assert response.status_code == 200

    body = response.json()
    print("PUT response:", body)

    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]



def test_patch_post(api_client, created_post):
    payload = patch_post_payload(created_post)
    print("\nPATCH payload:", payload)

    response = api_client.patch(f"/posts/{created_post}", payload)
    assert response.status_code == 200

    body = response.json()
    print("PATCH response:", body)

    assert body["title"] == payload["title"]



def test_delete_post(api_client, created_post):
    response = api_client.delete(f"/posts/{created_post}")
    assert response.status_code in (200, 204)
