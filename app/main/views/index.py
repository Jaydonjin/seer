from flask_restful import Resource

from app.main import api


@api.resource('/api/v1/version')
class Version(Resource):
    @staticmethod
    def get():
        return dict(version='0.0.1')
