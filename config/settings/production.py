from config.env import env
from .base import * # noqa


DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^(http?://)?localhost(:\d+)?$',
    r'^(https?://)?api.example.sch.ir(:\d+)?$',
    r'^(https?://)?assets.example.sch.ir(:\d+)?$',
    r'^(https?://)?api.example.ir(:\d+)?$',
    r'^(https?://)?example.ir(:\d+)?$',
)
