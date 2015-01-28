
# Django settings for gladminds project.
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
BASE_DIR = os.path.join(PROJECT_DIR, os.pardir)
STATIC_DIR = os.path.join(PROJECT_DIR, "static")
TEMPLATE_DIR = os.path.join(PROJECT_DIR, "templates")
EMAIL_DIR = os.path.join(TEMPLATE_DIR, "email")
DATA_CSV_PATH = os.path.join(BASE_DIR, "src/data")
TIMEZONE = 'Asia/Kolkata'

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'its secret'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'hu-python',
    }
}


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'hu'
)


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, "hu", 'collected')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    STATIC_DIR,
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
   # 'gladminds.core.custom_staticfiles_loader.FileSystemFinder',                   
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bbu7*-yvup0-*laxug+n5tf^lga_bwtrxu%y4ilb#$lv8%zw0m'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
                    # for performance enable cached templates
                    #      ('django.template.loaders.cached.Loader', (
                    #         'django.template.loaders.filesystem.Loader',
                    #         'django.template.loaders.app_directories.Loader',
                    #     )),
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    #  'django.template.loaders.eggs.Loader',
                   )

ROOT_URLCONF = 'hu.urls'

TEMPLATE_DIRS = (
    TEMPLATE_DIR,
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
