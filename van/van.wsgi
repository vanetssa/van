import os
import sys
sys.path.append('/website/van')
os.environ['DJANGO_SETTINGS_MODULE'] = 'van.settings'
import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()
