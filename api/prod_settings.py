import dj_database_url



From api.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()


MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SECRET_KEY = 'n=chr9gt)io#pz!kphevtks5=7lfwenfyf8b^6h*qw1nyg%rpn'

ALLOWED_HOSTS = ['rh-application.herokuapp.com','localhost', '127.0.0.1']