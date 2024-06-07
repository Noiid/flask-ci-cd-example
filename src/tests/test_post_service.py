from unittest.mock import MagicMock

import pytest
from blog.services.post_service import PostService, Category


@pytest.fixture
def service():
    repository = MagicMock()
    return PostService(repository)


@pytest.mark.parametrize(
    "post, expected_exception",
    [
        (
            {
                "id": 1,
                "title": "t",
                "content": "Content 1",
                "author": "Author 1",
                "category": "Tech",
            },
            ValueError,
        ),
        (
            {
                "id": 2,
                "title": "Post 1",
                "content": "c",
                "author": "Author 1",
                "category": "Tech",
            },
            ValueError,
        ),
        (
            {
                "id": 3,
                "title": "Post 1",
                "content": "Content 1",
                "author": "",
                "category": "Tech",
            },
            ValueError,
        ),
        (
            {
                "id": 4,
                "title": "Post 1",
                "content": "Content 1",
                "author": "Author 1",
                "category": "Invalid",
            },
            ValueError,
        ),
    ],
)
def test_validate_post(service, post, expected_exception):
    with pytest.raises(expected_exception):
        service.validate_post(post)


def test_create_post(service):
    post = {
        "id": 1,
        "title": "Post 1",
        "content": "Content 1",
        "author": "Author 1",
        "category": "Tech",
    }
    service.repository.save_post.return_value = post

    result = service.create_post(post)

    service.repository.save_post.assert_called_once_with(post)
    assert result == post


def test_get_post(service):
    post = {
        "id": 1,
        "title": "Post 1",
        "content": "Content 1",
        "author": "Author 1",
        "category": "Tech",
    }
    service.repository.get_post.return_value = post

    result = service.get_post(1)

    service.repository.get_post.assert_called_once_with(1)
    assert result == post


def test_delete_post(service):
    post = {
        "id": 1,
        "title": "Post 1",
        "content": "Content 1",
        "author": "Author 1",
        "category": "Tech",
    }
    service.repository.delete_post.return_value = post

    result = service.delete_post(1)

    service.repository.delete_post.assert_called_once_with(1)
    assert result == post


@pytest.mark.parametrize(
    "category, expected_posts",
    [
        (
            "Tech",
            [
                {
                    "id": 1,
                    "title": "Post 1",
                    "content": "Content 1",
                    "author": "Author 1",
                    "category": "Tech",
                }
            ],
        ),
        ("Business", []),
    ],
)
def test_get_posts_by_category(service, category, expected_posts):
    service.repository.get_posts_by_category.return_value = expected_posts

    result = service.get_posts_by_category(category)

    service.repository.get_posts_by_category.assert_called_once_with(category)
    assert result == expected_posts
