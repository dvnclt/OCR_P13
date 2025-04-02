"""
Configuration de l'application Django pour 'oc_lettings_site'.

Ce fichier contient la configuration de l'application 'oc_lettings_site' dans Django.
Il définit le nom de l'application et peut être utilisé pour ajouter des configurations spécifiques
à l'application, si nécessaire, dans le futur.
"""
from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Classe de configuration pour l'application 'oc_lettings_site'.

    Cette classe définit l'application 'oc_lettings_site' dans Django et son nom.
    Elle est utilisée pour l'enregistrement de l'application dans le projet.
    """
    name = 'oc_lettings_site'
