import redis


class RedisPool:
    def __init__(self):
        return

    @staticmethod
    def redis_pool(client_host='127.0.0.1', client_port=6379):
        pool = redis.ConnectionPool(host=client_host, port=client_port, db=0)
        return redis.StrictRedis(connection_pool=pool)


class ChangeKey:
    def __init__(self):
        return

    @staticmethod
    def change_string(self, r, key, value):
        bol = r.set(key, value)
        return bol


class Getkey:
    def __init__(self):
        return

    @staticmethod
    def get_string(r, key):
        value = r.get(key)
        return value

