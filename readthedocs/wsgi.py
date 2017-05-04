"""WSGI application helper"""
from __future__ import absolute_import, division, print_function

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
