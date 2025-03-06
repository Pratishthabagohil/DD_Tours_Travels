"""
WSGI config for DD_Tours project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DD_Tours.settings')

# Get the application
application = get_wsgi_application()

# Add WhiteNoise for static file handling
application = WhiteNoise(application, root='staticfiles')
application.add_files('staticfiles', prefix='static/')
application.add_files('media', prefix='media/')