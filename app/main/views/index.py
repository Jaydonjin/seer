from flask_restful import Resource
from flask import request
from app.main import api, r


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
        return user, 200

    @staticmethod
    def post(s_name):
        cur_body = request.get_json(True)
        result1 = r.hmset(s_name, {'name': cur_body['name'], 'age': cur_body['age']})
        print result1
        if result1:
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
