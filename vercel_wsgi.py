# vercel_wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DD_Tours.settings')

# Get the WSGI application
application = get_wsgi_application()

# Vercel expects the WSGI callable to be named 'app'
app = application