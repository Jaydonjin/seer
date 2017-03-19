from flask_restful import Resource
from flask import request
from app.main import api, r
import time


@api.resource('/api/v1/version')
class Version(Resource):
    @staticmethod
    def get():
        return dict(version='0.0.1')


@api.resource('/api/v1/user/<string:s_name>')
class User(Resource):
    @staticmethod
    def get(s_name):
        user = r.hgetall(s_name)
        if user:
            return user, 200
        else:
            return 'not existed', 404

    @staticmethod
    def post(s_name):
        cur_body = request.get_json(True)
        result = r.hmset(s_name, {'name': cur_body['name'], 'age': cur_body['age']})
        if result:
            return 'success', 200
        else:
            return 'failed', 500

    @staticmethod
    def delete(s_name):
        result = r.delete(s_name)
        if result:
            return 'success', 200
        else:
            return 'failed', 404


@api.resource('/api/v1/article')
class Article(Resource):
    @staticmethod
    def post():
        cur_body = request.get_json(True)
        pushdate = time.time()
        key = ''.join(['article', ':', str(r.incr('article:id'))])
        result = r.hmset(key, {'title': cur_body['title'], 'author': cur_body['author'],
                               'body': cur_body['body'], 'pushdate': pushdate,
                               'liketimes': cur_body['liketimes']})
        r.zadd('article:list:like', cur_body['liketimes'], key)
        print key
        if result:
            return 'success', 200
        else:
            return 'create article failed', 500


@api.resource('/api/v1/article/list/like')
class ArticleListLike(Resource):
    @staticmethod
    def get():
        result = r.zrevrange(name='article:list:like', start=0, end=-1)
        if result:
            result_arr = []
            for i in result:
                item = r.hgetall(i)
                result_arr.append(item)
            return result_arr, 200
        else:
            return 'not find article', 400
