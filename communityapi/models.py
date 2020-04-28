from communityapi import POSTS, USERS
from flask_restful import Resource, abort

def checkif_exists(type, item_id):
    if type == 'post':
        if item_id not in POSTS:
            abort(404, message="Post {} doesn't exist".format(item_id))
    elif type == 'user':
        if item_id not in USERS:
            abort(404, message="User {} doesn't exist".format(item_id))

class Post(Resource):
    def get(self, post_id):
        checkif_exists('post',post_id)
        return POSTS[post_id], 200

class User(Resource):
    def get(self, user_id):
        checkif_exists('user',user_id)
        return USERS[user_id], 200