HTTP_HOST = '127.0.0.1'
HTTP_PORT = 8080
DEBUG = False

SECRET_KEY = "\x02|\x86.\\\xea\xba\x89\xa3\xfc\r%s\x9e\x06\x9d\x01\x9c\x84\xa1b+uC"

# Flask-CORS Settings
CORS_ORIGINS = "*"
CORS_METHODS = "GET,POST,PUT"
CORS_ALLOW_HEADERS = "Content-Type,Host"

# DB
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/seer'
