from pathlib import Path
import dj_database_url
import os
import environ


env = environ.Env(
    DEBUG=(bool, True),
    DATABASE_URL=(str, ""),
    SECRET_KEY=(str, "secret"),
    ENVIRONMENT=(str, "DEVELOPMENT"),
    ALLOWED_HOSTS=(str, "127.0.0.1"),
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#load envirom settings
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(";")

DEBUG = env("DEBUG")
ENVIRONMENT = env("ENVIRONMENT")

VERSION = "0.0.1"

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "treelinks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "treelinks", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

DATABASES = {
    "default": dj_database_url.parse(env("DATABASE_URL"), conn_max_age=600)
}

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

#limit 50mb
DATA_UPLOAD_MAX_MEMORY_SIZE = 200 * 1024 * 1024

LANGUAGE_CODE = "es"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = "assets"
STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "locale_files")
MEDIA_URL = "/media/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
