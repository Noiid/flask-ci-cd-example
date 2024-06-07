from flask import Blueprint, request, jsonify
from blog.repositories.post_repository import PostRepository
from blog.services.post_service import PostService
from flasgger import swag_from

post_routes = Blueprint("post_routes", __name__)

repository: PostRepository = PostRepository()
service: PostService = PostService(repository=repository)


@post_routes.route("/posts", methods=["POST"])
@swag_from("../docs/create_post.yml")
def create_post():
    post = request.get_json()
    try:
        post = service.create_post(post)
    except ValueError as e:
        return {"error": str(e)}, 400

    return post, 201


@post_routes.route("/posts/<string:id>", methods=["GET"])
@swag_from("../docs/get_post.yml")
def get_post(id):
    post = service.get_post(id)
    if post is None:
        return {"error": "Post not found"}, 404
    return post


@post_routes.route("/posts/<string:id>", methods=["DELETE"])
@swag_from(
    {
        "tags": ["Posts"],
        "parameters": [
            {
                "in": "path",
                "name": "id",
                "schema": {"type": "integer"},
                "required": True,
                "description": "The post ID",
            }
        ],
        "responses": {
            204: {"description": "Post deleted"},
            404: {"description": "Post not found"},
        },
    }
)
def delete_post(id):
    post = service.delete_post(id)
    if post is None:
        return {"error": "Post not found"}, 404
    return "", 204


@post_routes.route("/posts", methods=["GET"])
@swag_from("../docs/get_all_post.yml")
def get_all():
    posts = service.get_all()
    return posts


@post_routes.route("/posts/category/<string:category>", methods=["GET"])
@swag_from(
    "../docs/get_posts_by_category.yml",
)
def get_posts_by_category(category):
    try:
        posts = service.get_posts_by_category(category)
    except ValueError as e:
        return {"error": str(e)}, 400
    return posts
