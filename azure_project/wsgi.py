import os
from django.core.wsgi import get_wsgi_application

#settings_module = 'azure_project.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'azure_project.settings'
if os.environ['WEBSITE_HOSTNAME']=='allurepro-staging.azurewebsites.net':
    settings_module = 'azure_project.staging'
elif os.environ['WEBSITE_HOSTNAME']=='allurepro.azurewebsites.net':
    settings_module = 'azure_project.deployment'
else:
    settings_module = 'azure_project.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()

