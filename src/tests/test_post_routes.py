import pytest
from flask import json, Flask
from unittest.mock import MagicMock

from app import app
from blog.routes import post_routes


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_post(client):
    post_routes.service = MagicMock()
    post = {"id": "1", "title": "Post 1", "content": "Content 1"}
    post_routes.service.create_post.return_value = post

    response = client.post(
        "/posts", data=json.dumps(post), content_type="application/json"
    )

    post_routes.service.create_post.assert_called_once_with(post)
    assert response.status_code == 200
    assert json.loads(response.get_data()) == post


def test_get_post(client):
    post_routes.service = MagicMock()
    post = {"id": "1", "title": "Post 1", "content": "Content 1"}
    post_routes.service.get_post.return_value = post

    response = client.get("/posts/1")

    post_routes.service.get_post.assert_called_once_with("1")
    assert response.status_code == 200
    assert json.loads(response.get_data()) == post


def test_delete_post(client):
    post_routes.service = MagicMock()
    post = {"id": "1", "title": "Post 1", "content": "Content 1"}
    post_routes.service.delete_post.return_value = post

    response = client.delete("/posts/1")

    post_routes.service.delete_post.assert_called_once_with("1")
    assert response.status_code == 204
