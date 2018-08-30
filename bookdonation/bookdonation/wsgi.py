"""
WSGI config for bookdonation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookdonation.settings")

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
# from whitenoise import WhiteNoise

# from bookdonation import MyWSGIApp

# application = MyWSGIApp()
# application = WhiteNoise(application, root='/path/to/static/files')
# application.add_files('/path/to/more/static/files', prefix='more-files/')