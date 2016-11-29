import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'blog/staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'blog/static'),
)
SECRET_KEY = os.environ["SECRET_KEY"]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

ROOT_URLCONF = 'blog.urls'

INSTALLED_APPS = ['blog']
