"""
Configuration WSGI pour l'application Django.

Ce fichier permet de configurer l'application WSGI, nécessaire pour déployer
l'application Django sur un serveur de production (par exemple, avec Gunicorn).
Il définit l'application WSGI en utilisant la méthode `get_wsgi_application`.
"""
import os

from django.core.wsgi import get_wsgi_application

# Définition de la variable d'environnement DJANGO_SETTINGS_MODULE pour
# spécifier les paramètres
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

# L'application WSGI pour le déploiement
application = get_wsgi_application()
