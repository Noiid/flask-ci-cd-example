class PostRepository:
    def __init__(self):
        self.posts = {}
        self.id = 1

    def get_all(self):
        return list(self.posts.values())

    def save_post(self, post):
        post["id"] = self.id
        self.posts[self.id] = post
        self.id += 1
        return post

    def get_post(self, id):
        print(self.posts)
        return self.posts.get(id)

    def delete_post(self, id):
        print(id)
        return self.posts.pop(id, None)

    def get_posts_by_category(self, category):
        return [post for post in self.posts.values() if post["category"] == category]
