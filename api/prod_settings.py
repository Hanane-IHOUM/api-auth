import dj_database_url


from api.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




ALLOWED_HOSTS = ['rh-application.herokuapp.com','localhost', '127.0.0.1']