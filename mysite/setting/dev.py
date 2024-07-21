from mysite.settings import *
from decouple import config


ALLOWED_HOSTS = [
    '*'
]

# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django_extensions',
    'django_summernote',
    'captcha',
    'robots',
    "debug_toolbar",
    "taggit",
    'sweetify',
    'website',
    'blog',
    'accounts',
    'crispy_forms',
    'compressor',
    'rjsmin',
    'rcssmin',
]



MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]



#site settings
SITE_ID = config('SITE_ID', cast=int, default=2)

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DEV_ENGINE',default='django.db.backends.sqlite3'),
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]



COMPRESS_ENABLED = config("COMPRESS_ENABLED", cast=bool, default=False)
COMPRESS_OFFLINE = config("COMPRESS_OFFLINE", cast=bool, default=False)

EMAIL_BACKEND = config('EMAIL_BACKEND_DEV')

X_FRAME_OPSTIONS = 'SAMEORIGIN'

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False