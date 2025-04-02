"""
Enregistrement des modèles dans l'interface d'administration Django.

Ce fichier permet d'enregistrer les modèles 'Letting', 'Address' et 'Profile' dans
l'interface d'administration Django. Cela permet de gérer ces modèles via l'interface
administrative sans avoir à manipuler directement la base de données.
"""
from django.contrib import admin

from lettings.models import Letting, Address
from profiles.models import Profile

# Enregistrement des modèles pour les rendre accessibles dans l'administration
admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
