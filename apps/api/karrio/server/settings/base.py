"""
Django settings for karrio.server project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import importlib
import dj_database_url
from pathlib import Path
from datetime import timedelta
from decouple import AutoConfig
from django.urls import reverse_lazy
from django.core.management.utils import get_random_secret_key
from corsheaders.defaults import default_headers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(BASE_DIR / "server" / "VERSION", "r") as v:
    VERSION = v.read().strip()


config = AutoConfig(search_path=Path().resolve())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG_MODE", default=True, cast=bool)

# custom env
WORK_DIR = config("WORK_DIR", default="")
Path(WORK_DIR).mkdir(parents=True, exist_ok=True)

USE_HTTPS = config("USE_HTTPS", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*").split(",")
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="http://*").split(",")

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    "x-test-mode",
    "x-org-id",
]

# HTTPS configuration
if USE_HTTPS is True:
    global SECURE_SSL_REDIRECT
    global SECURE_PROXY_SSL_HEADER
    global SESSION_COOKIE_SECURE
    global SECURE_HSTS_SECONDS
    global SECURE_HSTS_INCLUDE_SUBDOMAINS
    global CSRF_COOKIE_SECURE
    global SECURE_HSTS_PRELOAD

    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 1
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
    CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="https://*").split(
        ","
    )


# karrio packages settings
KARRIO_CONF = [
    app
    for app in [
        {
            "app": "karrio.server.core",
            "module": "karrio.server.core",
            "urls": "karrio.server.core.urls",
        },
        {
            "app": "karrio.server.iam",
            "module": "karrio.server.iam",
        },
        {
            "app": "karrio.server.providers",
            "module": "karrio.server.providers",
            "urls": "karrio.server.providers.urls",
        },
        {
            "app": "karrio.server.tracing",
            "module": "karrio.server.tracing",
        },
        {
            "app": "karrio.server.graph",
            "module": "karrio.server.graph",
            "urls": "karrio.server.graph.urls",
        },
        {
            "app": "karrio.server.proxy",
            "module": "karrio.server.proxy",
            "urls": "karrio.server.proxy.urls",
        },
        {
            "app": "karrio.server.manager",
            "module": "karrio.server.manager",
            "urls": "karrio.server.manager.urls",
        },
        {
            "app": "karrio.server.events",
            "module": "karrio.server.events",
            "urls": "karrio.server.events.urls",
        },
        {
            "app": "karrio.server.documents",
            "module": "karrio.server.documents",
            "urls": "karrio.server.documents.urls",
        },
        {
            "app": "karrio.server.data",
            "module": "karrio.server.data",
            "urls": "karrio.server.data.urls",
        },
        {
            "app": "karrio.server.admin",
            "module": "karrio.server.admin",
            "urls": "karrio.server.admin.urls",
        },
        {
            "app": "karrio.server.pricing",
            "module": "karrio.server.pricing",
        },
        {
            "app": "karrio.server.apps",
            "module": "karrio.server.apps",
        },
    ]
    if importlib.util.find_spec(app["module"]) is not None  # type:ignore
]

KARRIO_APPS = [cfg["app"] for cfg in KARRIO_CONF]
KARRIO_URLS = [cfg["urls"] for cfg in KARRIO_CONF if "urls" in cfg]

ALLOW_ADMIN_APPROVED_SIGNUP = config(
    "ALLOW_ADMIN_APPROVED_SIGNUP", default=False, cast=bool
)
ALLOW_SIGNUP = (
    config("ALLOW_SIGNUP", default=False, cast=bool) or ALLOW_ADMIN_APPROVED_SIGNUP
)
MULTI_ORGANIZATIONS = (
    importlib.util.find_spec("karrio.server.orgs") is not None  # type:ignore
)
ALLOW_MULTI_ACCOUNT = config(
    "ALLOW_MULTI_ACCOUNT", default=MULTI_ORGANIZATIONS, cast=bool
)
ADMIN_DASHBOARD = (
    importlib.util.find_spec("karrio.server.admin") is not None  # type:ignore
)
ORDERS_MANAGEMENT = (
    importlib.util.find_spec("karrio.server.orders") is not None  # type:ignore
)
APPS_MANAGEMENT = (
    importlib.util.find_spec("karrio.server.apps") is not None  # type:ignore
)
DOCUMENTS_MANAGEMENT = (
    importlib.util.find_spec("karrio.server.documents") is not None  # type:ignore
)
DATA_IMPORT_EXPORT = (
    importlib.util.find_spec("karrio.server.data") is not None  # type:ignore
)
CUSTOM_CARRIER_DEFINITION = (
    importlib.util.find_spec("karrio.mappers.generic") is not None  # type:ignore
)
MULTI_TENANTS = importlib.util.find_spec(  # type:ignore
    "karrio.server.tenants"
) is not None and config("MULTI_TENANT_ENABLE", default=False, cast=bool)
AUDIT_LOGGING = importlib.util.find_spec(  # type:ignore
    "karrio.server.audit"
) is not None and config("AUDIT_LOGGING", default=True, cast=bool)
PERSIST_SDK_TRACING = config("PERSIST_SDK_TRACING", default=True, cast=bool)
WORKFLOW_MANAGEMENT = (
    importlib.util.find_spec("karrio.server.automation") is not None  # type:ignore
)


# Feature flags
FEATURE_FLAGS = [
    ("AUDIT_LOGGING", bool),
    ("ALLOW_SIGNUP", bool),
    ("ALLOW_ADMIN_APPROVED_SIGNUP", bool),
    ("ALLOW_MULTI_ACCOUNT", bool),
    ("ADMIN_DASHBOARD", bool),
    ("MULTI_ORGANIZATIONS", bool),
    ("ORDERS_MANAGEMENT", bool),
    ("APPS_MANAGEMENT", bool),
    ("DOCUMENTS_MANAGEMENT", bool),
    ("DATA_IMPORT_EXPORT", bool),
    ("CUSTOM_CARRIER_DEFINITION", bool),
    ("PERSIST_SDK_TRACING", bool),
    ("ORDER_DATA_RETENTION", int),
    ("TRACKER_DATA_RETENTION", int),
    ("SHIPMENT_DATA_RETENTION", int),
    ("API_LOGS_DATA_RETENTION", int),
    ("WORKFLOW_MANAGEMENT", bool),
]


# components path settings
BASE_PATH = config("BASE_PATH", default="")
if len(BASE_PATH) > 0 and BASE_PATH.startswith("/"):
    BASE_PATH = BASE_PATH[1:]
if len(BASE_PATH) > 0 and not BASE_PATH.endswith("/"):
    BASE_PATH = BASE_PATH + "/"

ROOT_URLCONF = "karrio.server.urls"
LOGIN_URL = BASE_PATH + "/login/"
LOGOUT_REDIRECT_URL = BASE_PATH + "/login/"
LOGIN_REDIRECT_URL = BASE_PATH + "/admin/"
OPEN_API_PATH = "openapi/"

NAMESPACED_URLS = [
    ("api/", "rest_framework.urls", "rest_framework"),
    ("oauth/", "oauth2_provider.urls", "oauth2_provider"),
]

WHITENOISE_APP = ["whitenoise.runserver_nostatic"] if DEBUG else []
BASE_APPS = [
    "karrio.server.user",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    *WHITENOISE_APP,
    "django.contrib.staticfiles",
    "django.contrib.admin",
]

OTP_APPS = [
    "django_filters",
    "django_otp",
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "django_otp.plugins.otp_email",
    "two_factor",
    # "two_factor.plugins.phonenumber",
    "two_factor.plugins.email",
]

INSTALLED_APPS = [
    "constance",
    *KARRIO_APPS,
    *BASE_APPS,
    "rest_framework",
    "django_email_verification",
    "rest_framework_tracking",
    "drf_spectacular",
    "constance.backends.database",
    "huey.contrib.djhuey",
    "corsheaders",
    "oauth2_provider",
    *OTP_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "karrio.server.core.authentication.AuthenticationMiddleware",
    "karrio.server.core.authentication.TwoFactorAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "karrio.server.core.middleware.SessionContext",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "server" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "karrio.server.core.context_processors.get_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "karrio.server.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Karrio Middleware
# KARRIO_ENTITY_ACCESS_METHOD = 'karrio.server.core.middleware.CreatorAccess'
# KARRIO_ENTITY_ACCESS_METHOD = 'karrio.server.core.middleware.WideAccess'
MODEL_TRANSFORMERS: list = []
PERMISSION_CHECKS = ["karrio.server.core.permissions.check_feature_flags"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
_DB_NAME = config("DATABASE_NAME", default="db")
_DB_ENGINE = "sqlite3" if "sqlite3" in _DB_NAME else "postgresql"

CONN_MAX_AGE = config("DATABASE_CONN_MAX_AGE", default=0, cast=int)
DB_ENGINE = "django.db.backends.{}".format(
    config("DATABASE_ENGINE", default=_DB_ENGINE)
)
DB_NAME = (
    os.path.join(WORK_DIR, f"{_DB_NAME}{'' if '.sqlite3' in _DB_NAME else '.sqlite3'}")
    if "sqlite3" in DB_ENGINE
    else _DB_NAME
)

DATABASES = {
    "default": {
        "NAME": DB_NAME,
        "ENGINE": DB_ENGINE,
        "CONN_MAX_AGE": CONN_MAX_AGE,
        "PORT": config("DATABASE_PORT", default="5432"),
        "HOST": config("DATABASE_HOST", default="localhost"),
        "USER": config("DATABASE_USERNAME", default="postgres"),
        "PASSWORD": config("DATABASE_PASSWORD", default="postgres"),
    }
}

if config("DATABASE_URL", default=None):
    db_from_env = dj_database_url.config(
        conn_max_age=config("DATABASE_CONN_MAX_AGE", default=0, cast=int)
    )
    DATABASES["default"].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
AUTH_USER_MODEL = "user.User"


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_HOST = config("CDN_STATIC_HOST", default="") if not DEBUG else ""
STATIC_URL = STATIC_HOST + config(
    "STATIC_URL", default=f"{BASE_PATH}/static/".replace("//", "/")
)
STATIC_ROOT = config("STATIC_ROOT_DIR", default=(BASE_DIR / "server" / "staticfiles"))

STATICFILES_DIRS = [
    BASE_DIR / "server" / "static" / "karrio",
    BASE_DIR / "server" / "static" / "extra",
]
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Django REST framework
AUTHENTICATION_CLASSES = [
    "karrio.server.core.authentication.TokenBasicAuthentication",
    "karrio.server.core.authentication.TokenAuthentication",
    "karrio.server.core.authentication.OAuth2Authentication",
    "karrio.server.core.authentication.JWTAuthentication",
    "rest_framework.authentication.SessionAuthentication",
]
PERMISSION_CLASSES = [
    "rest_framework.permissions.IsAuthenticated",
    "karrio.server.core.permissions.AllowEnabledAPI",
]


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": PERMISSION_CLASSES,
    "DEFAULT_AUTHENTICATION_CLASSES": AUTHENTICATION_CLASSES,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
        "rest_framework.throttling.ScopedRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "60/minute",
        "user": "600/minute",
        "carrier_request": "300/minute",
    },
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "EXCEPTION_HANDLER": "karrio.server.core.exceptions.custom_exception_handler",
    "JSON_UNDERSCOREIZE": {"no_underscore_before_number": True},
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}

# JWT config
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        config("JWT_ACCESS_EXPIRY", default=30, cast=int)
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        config("JWT_REFRESH_EXPIRY", default=3, cast=int)
    ),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=15),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# Oauth2 config
OIDC_RSA_PRIVATE_KEY = config("OIDC_RSA_PRIVATE_KEY", default="").replace("\\n", "\n")
OAUTH2_PROVIDER_APPLICATION_MODEL = "oauth2_provider.Application"
OAUTH2_PROVIDER = {
    "PKCE_REQUIRED": False,
    "OIDC_ENABLED": True,
    "OIDC_RSA_PRIVATE_KEY": OIDC_RSA_PRIVATE_KEY,
    "SCOPES": {
        "read": "Reading scope",
        "write": "Writing scope",
        "openid": "OpenID connect",
    },
    "OAUTH2_VALIDATOR_CLASS": "karrio.server.core.oauth_validators.CustomOAuth2Validator",
}

# OpenAPI config
SPECTACULAR_SETTINGS = {
    "VERSION": VERSION,
    "SERVE_INCLUDE_SCHEMA": False,
    "ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE": True,
    "ENUM_GENERATE_CHOICE_DESCRIPTION": False,
    "ENUM_NAME_OVERRIDES": {
        "CountryEnum": "karrio.server.core.serializers.COUNTRIES",
        "CurrencyEnum": "karrio.server.core.serializers.CURRENCIES",
        "ShipmentStatus": "karrio.server.manager.serializers.SHIPMENT_STATUS",
    },
    "OAUTH2_FLOWS": ["authorizationCode"],
    "OAUTH2_AUTHORIZATION_URL": "/oauth/authorize/",
    "OAUTH2_TOKEN_URL": "/oauth/token/",
    "OAUTH2_REFRESH_URL": None,
    "OAUTH2_SCOPES": OAUTH2_PROVIDER["SCOPES"],
    "AUTHENTICATION_WHITELIST": [
        _ for _ in AUTHENTICATION_CLASSES if "Session" not in _
    ],
    "POSTPROCESSING_HOOKS": [
        "karrio.server.openapi.custom_postprocessing_hook",
    ],
    "PREPROCESSING_HOOKS": [],
}
SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "LOGIN_URL": reverse_lazy("admin:login"),
    "LOGOUT_URL": "/admin/logout",
    "DEFAULT_INFO": "karrio.server.core.views.schema.swagger_info",
    "DEFAULT_AUTO_SCHEMA_CLASS": "karrio.server.core.views.schema.SwaggerAutoSchema",
    "SECURITY_DEFINITIONS": {
        "Token": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": """
            `Authorization: Token key_xxxxxxxx`
            """,
        },
        "JWT": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": """
            `Authorization: Bearer xxx.xxx.xxx`
            """,
        },
        "Oauth2": {
            "type": "oauth2",
            "authorizationUrl": "/oauth/authorize/",
            "tokenUrl": "/oauth/token/",
            "flow": "authorizationCode",
            "description": """
            `Authorization: Bearer xxxxxxxx`
            """,
            "scopes": OAUTH2_PROVIDER["SCOPES"],
        },
    },
}
REDOC_SETTINGS = {
    "LAZY_RENDERING": False,
    "HIDE_HOSTNAME": True,
    "REQUIRED_PROPS_FIRST": True,
    "SPEC_URL": ("schema-json", dict(format=".json")),
}

# Logging configuration
LOG_LEVEL = "DEBUG" if DEBUG else config("LOG_LEVEL", default="INFO")
DJANGO_LOG_LEVEL = "INFO" if DEBUG else config("DJANGO_LOG_LEVEL", default="WARNING")
LOG_FILE_DIR = config("LOG_DIR", default=WORK_DIR)
LOG_FILE_NAME = os.path.join(LOG_FILE_DIR, "debug.log")
DRF_TRACKING_ADMIN_LOG_READONLY = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {filename} {lineno} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "verbose",
            "filename": LOG_FILE_NAME,
            "when": "D",  # this specifies the interval
            "interval": 1,  # defaults to 1, only necessary for other values
            "backupCount": 20,  # how many backup file to keep, 10 days
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": DJANGO_LOG_LEVEL,
            "propagate": False,
        },
        "karrio": {
            "handlers": ["file", "console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}
