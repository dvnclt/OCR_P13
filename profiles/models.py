"""
Modèle pour le profil d'un utilisateur.

Ce fichier contient le modèle `Profile` qui permet d'ajouter des informations
supplémentaires à un utilisateur. Le profil est lié au modèle `User` de Django via
une relation `OneToOne`, et il inclut un champ pour stocker la ville favorite de l'utilisateur.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant le profil d'un utilisateur.

    Ce modèle permet de lier des informations supplémentaires à un utilisateur, comme
    la ville favorite. Il utilise une relation OneToOne avec le modèle `User` de Django,
    garantissant qu'un utilisateur a un seul profil et qu'un profil appartient à un seul
    utilisateur.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne du profil.

        Cette méthode permet de retourner le nom d'utilisateur associé au profil,
        facilitant ainsi l'affichage du profil dans les interfaces administratives ou
        autres représentations textuelles.

        Retour :
            str : Le nom d'utilisateur du profil.
        """
        return self.user.username
