"""
ASGI config for JulyProject project.


It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
# Contains all the files for ASGI compatibe servers.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JulyProject.settings')

application = get_asgi_application()
