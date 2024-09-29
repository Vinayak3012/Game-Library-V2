from datetime import timedelta


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'super-secret'  # You should set this to a long random string
    # Disable SQLAlchemy modification tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class devconfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///devdb.sqlite3'
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    WTF_CSRF_ENABLED = False
    SECURITY_JOIN_USER_ROLES = True

    def SECURITY_TOKEN_EXPIRE_TIMESTAMP(user): return int(
        (timedelta(hours=1)).total_seconds())
    # {},{},{'headers:{"Authentication-Token":""}}
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    SECURITY_TOKEN_MAX_AGE = 24 * 3600  # Token validity in seconds
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_ENABLED = True

    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_URL = "redis://localhost:6379/0"
    CACHE_DEFAULT_TIMEOUT = 300

    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"


class devconfig22(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///devdb.sqlite3'
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    WTF_CSRF_ENABLED = False

    # Flask-Security configurations
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    SECURITY_TOKEN_MAX_AGE = 24 * 3600  # 1 day in seconds
    # SECURITY_TOKEN_AUTHENTICATION_KEY = 'auth_token'
    SECURITY_TRACKABLE = True

    # Enable token authentication
    SECURITY_TOKEN_AUTHENTICATION_ENABLED = True
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 3

    CACHE_REDIS_URL = "redis://localhost:6379/0"
    CACHE_DEFAULT_TIMEOUT = 300

    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
