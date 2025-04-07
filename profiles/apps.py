"""
Configuration de l'application Django pour 'profiles'.

Ce fichier contient la configuration de l'application 'profiles'. Il définit
le nom de l'application et peut être utilisé pour ajouter des configurations
spécifiques à l'application si nécessaire, dans le futur.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Classe de configuration pour l'application 'profiles'.

    Cette classe définit l'application 'profiles' dans Django et son nom.
    Elle est utilisée pour l'enregistrement de l'application dans le projet et
    peut être étendue si des configurations supplémentaires sont nécessaires.
    """
    name = 'profiles'
