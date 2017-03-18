HTTP_HOST = '127.0.0.1'
HTTP_PORT = 8080
DEBUG = False

SECRET_KEY = "\x02|\x86.\\\xea\xba\x89\xa3\xfc\r%s\x9e\x06\x9d\x01\x9c\x84\xa1b+uC"

# Flask-NegLog Settings
LOG_LEVEL = 'debug'
LOG_FILENAME = "logs/error.log"
LOG_BACKUP_COUNT = 10
LOG_MAX_BYTE = 1024 * 1024 * 10
LOG_FORMATTER = '%(asctime)s - %(levelname)s - %(message)s'
LOG_ENABLE_CONSOLE = True

# Flask-CORS Settings
CORS_ORIGINS = "*"
CORS_METHODS = "GET,POST,PUT"
CORS_ALLOW_HEADERS = "Content-Type,Host"
