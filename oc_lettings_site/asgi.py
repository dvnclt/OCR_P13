"""
Configuration ASGI pour l'application Django.

Ce fichier permet de configurer l'application ASGI, nécessaire pour déployer
l'application Django dans un environnement asynchrone. Il définit
l'application ASGI en utilisant la méthode `get_asgi_application`, ce qui
permet la gestion des connexions asynchrones, comme WebSockets ou HTTP/2.
"""
import os
from django.core.asgi import get_asgi_application

# Définition de la variable d'environnement DJANGO_SETTINGS_MODULE pour
# spécifier les paramètres
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

# L'application ASGI pour la gestion des connexions asynchrones
application = get_asgi_application()
