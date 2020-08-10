DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

SECRET_KEY = 1

INSTALLED_APPS = [
    'django_counter_cache_field',
    'tests',
]

DEBUG = False

SITE_ID = 1
