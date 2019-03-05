# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'


"""
WSGI config for ml_with_django project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior
# ml_with_django directory.
#app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')

#sys.path.append(os.path.join(app_path, 'ml_with_django'))


sys.path.append('/home/ml_with_django/workspace/ml_with_django')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/ml_with_django/workspace/stock_analysis/lib/python3.4/site-packages')

path = '/home/ml_with_django/workspace/stock_analysis'
if path not in sys.path:
    sys.path.append(path)
    
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.development"

# if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
#     from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()
# if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
#     application = Sentry(application)
# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
