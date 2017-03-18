from flask import Blueprint
from flask_restful import Api
from redis import home as rds

url_prefix = '/seer'
main = Blueprint('main', __name__, url_prefix=url_prefix)

api = Api(main)
pool = rds.RedisPool()
r = pool.redis_pool("127.0.0.1", 6379)

from . import views