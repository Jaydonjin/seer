from flask_restful import Resource
from flask import request, Response
from app.main import api, r
from app.main.mysql.db_controller import *
import time
import json


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


@api.resource('/api/v1/article', methods=['POST'])
class NewArticle(Resource):
    @staticmethod
    def post():
        cur_body = request.get_json(True)
        pushdate = time.time()
        result = create_article(cur_body['title'], cur_body['author'], cur_body['body'], cur_body['liketimes'],
                                pushdate)
        if result == 'success':
            response = Response('success', 200)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            return response

        else:
            response = Response('create failed', 200)
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response


@api.resource('/api/v1/article/<int:id>', methods=['GET'])
class Article(Resource):
    @staticmethod
    def get(id):
        key = ''.join(['article', ':', str(id)])
        pre_redis_time = time.time()
        redis_result = r.hgetall(key)
        redis_result2 = r.hgetall(key)
        redis_result3 = r.hgetall(key)
        redis_result4 = r.hgetall(key)
        redis_result5 = r.hgetall(key)
        redis_result6 = r.hgetall(key)
        redis_result7 = r.hgetall(key)
        redis_result8 = r.hgetall(key)
        redis_result9 = r.hgetall(key)
        redis_result10 = r.hgetall(key)
        cur_redis_time = time.time()
        if redis_result:
            usage_redis_time = cur_redis_time - pre_redis_time
            print 'redis', usage_redis_time
            redis_result['usage_time'] = usage_redis_time
            redis_result['data_from'] = 'redis'
            data = json.dumps(redis_result)
            response = Response(data, 200)
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
        else:
            pre_mysql_time = time.time()
            mysql_result = get_article_by_id(id)
            mysql_result2 = get_article_by_id(id)
            mysql_result3 = get_article_by_id(id)
            mysql_result4 = get_article_by_id(id)
            mysql_result5 = get_article_by_id(id)
            mysql_result6 = get_article_by_id(id)
            mysql_result7 = get_article_by_id(id)
            mysql_result8 = get_article_by_id(id)
            mysql_result9 = get_article_by_id(id)
            mysql_result10 = get_article_by_id(id)
            cur_mysql_time = time.time()
            usage_mysql_time = cur_mysql_time - pre_mysql_time
            print 'mysql', usage_mysql_time
            if mysql_result != 404:
                mysql_result['usage_time'] = usage_mysql_time
                mysql_result['data_from'] = 'mysql'
                data = json.dumps(mysql_result)
                key = ''.join(['article', ':', str(id)])
                result = r.hmset(key, {'title': mysql_result['title'], 'author': mysql_result['author'],
                                       'body': mysql_result['body'], 'push_date': mysql_result,
                                       'liketimes': mysql_result['like_time']})
                if result:
                    response = Response(data, 200)
                    response.headers['Access-Control-Allow-Origin'] = '*'
                else:
                    response = Response(data, 201)
                    response.headers['Access-Control-Allow-Origin'] = '*'
                    return response
            else:
                response = Response('not found article', 404)
                response.headers['Access-Control-Allow-Origin'] = '*'
                return response


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
