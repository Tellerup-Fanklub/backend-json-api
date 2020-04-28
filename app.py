from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

POSTS = {
    0: {
        "title": "Hello World!",
        "author_id": 0,
        "content": "Lorem Ipsum er ganske enkelt fyldtekst fra print- og typografiindustrien. Lorem Ipsum har været standard fyldtekst siden 1500-tallet, hvor en ukendt trykker sammensatte en tilfældig spalte for at trykke en bog til sammenligning af forskellige skrifttyper. Lorem Ipsum har ikke alene overlevet fem århundreder, men har også vundet indpas i elektronisk typografi uden væsentlige ændringer. Sætningen blev gjordt kendt i 1960'erne med lanceringen af Letraset-ark, som indeholdt afsnit med Lorem Ipsum, og senere med layoutprogrammer som Aldus PageMaker, som også indeholdt en udgave af Lorem Ipsum."
    }
}

USERS = {
    0: {
        "name": "user0",
    }
}

def checkif_exists(type, item_id):
    if type == 'post':
        if item_id not in POSTS:
            abort(404, message="Post {} doesn't exist".format(item_id))
    elif type == 'user':
        if item_id not in USERS:
            abort(404, message="User {} doesn't exist".format(item_id))

class Index(Resource):
    def get(self):
        return "API v0.0.1", 200

class PostList(Resource):
    def get(self):
        return POSTS, 200

class Post(Resource):
    def get(self, post_id):
        checkif_exists('post',post_id)
        return POSTS[post_id], 200

class UserList(Resource):
    def get(self):
        return USERS, 200

class User(Resource):
    def get(self, user_id):
        checkif_exists('user',user_id)
        return USERS[user_id], 200

api.add_resource(Index, "/")
api.add_resource(PostList, "/posts")
api.add_resource(Post, "/posts/<int:post_id>")
api.add_resource(UserList, "/users")
api.add_resource(User, "/users/<int:user_id>")

if __name__ == '__main__':
        app.run(host="0.0.0.0",debug=True)
