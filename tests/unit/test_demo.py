from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_demo_root_should_return_index_page_returning_200_status_code() -> None:
    response = client.get("/demo/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Static Site Example" in response.text


def test_get_demo_about_should_return_about_page_returning_200_status_code() -> None:
    response = client.get("/demo/about")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "About" in response.text


def test_get_demo_docs_should_return_docs_page_returning_200_status_code() -> None:
    response = client.get("/demo/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Documentation" in response.text


def test_get_demo_credits_should_return_credits_page_returning_200_status_code() -> (
    None
):
    response = client.get("/demo/credits")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Credits" in response.text
