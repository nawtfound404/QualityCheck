
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_returns_success():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert isinstance(data["title"], str)
    assert data["title"] != ""
    assert isinstance(data["body"], str)
    assert data["body"] != ""


def test_get_nonexistent_post_returns_not_found():
    response = requests.get(
        f"{BASE_URL}/posts/999999",
        timeout=10,
    )

    assert response.status_code == 404
