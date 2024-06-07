from blog.repositories.post_repository import PostRepository

from enum import Enum


class Category(Enum):
    TECH = "Tech"
    BUSINESS = "Business"
    HEALTH = "Health"
    SPORTS = "Sports"


class PostService:
    def __init__(self, repository):
        self.repository: PostRepository = repository

    def validate_post(self, post):
        title = post.get("title")
        content = post.get("content")
        author = post.get("author")
        category = post.get("category")
        if not title or not isinstance(title, str) or not (5 <= len(title) <= 100):
            raise ValueError("Post title must be a string between 5 and 100 characters")

        if not content or not isinstance(content, str) or len(content) < 5:
            raise ValueError(
                "Post content must be a string and at least 5 characters long"
            )

        if not author or not isinstance(author, str):
            raise ValueError("Post author must be a string")

        if category not in [category.value for category in Category]:
            raise ValueError(
                "Post category must be one of: Tech, Business, Health, Sports"
            )

    def create_post(self, post):
        self.validate_post(post)
        return self.repository.save_post(post)

    def get_post(self, id):
        return self.repository.get_post(int(id))

    def delete_post(self, id):
        return self.repository.delete_post(int(id))
    
    def get_all(self):
        return self.repository.get_all()

    def get_posts_by_category(self, category):
        if category not in [category.value for category in Category]:
            raise ValueError("Invalid category")
        return self.repository.get_posts_by_category(category)
