from communityapi import api
from communityapi.models import Post, User
from communityapi import USERS, POSTS
from flask_restful import Resource

class PostList(Resource):
    def get(self):
        return POSTS, 200

class UserList(Resource):
    def get(self):
        return USERS, 200

class Index(Resource):
    def get(self):
        return "API v0.0.1", 200

api.add_resource(Index, "/")
api.add_resource(PostList, "/posts")
api.add_resource(Post, "/posts/<int:post_id>")
api.add_resource(UserList, "/users")
api.add_resource(User, "/users/<int:user_id>")