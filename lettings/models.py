"""
Définit les modèles de l'application Lettings

Ce fichier contient les modèles Address et Letting utilisés pour stocker les
informations
des adresses et des locations dans la base de données
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse postale

    Attributs :
        - number (int) : Numéro de rue (max : 9999)
        - street (str) : Nom de la rue (max : 64 caractères)
        - city (str) : Ville (max : 64 caractères)
        - state (str) : Code d'état (2 caractères)
        - zip_code (int) : Code postal (max : 99999)
        - country_iso_code (str) : Code ISO du pays (3 caractères)
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3,
                                        validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Retourne une représentation textuelle de l'adresse sous forme de chaîne
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Métadonnées du modèle Address

        Définit des options supplémentaires pour le modèle, notamment le nom
        pluriel utilisé dans l'interface d'administration
        """
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Modèle représentant une location

    Attributs :
        - title (str) : Titre de la location (max : 256 caractères)
        - address (Address) : Adresse associée à la location
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne une représentation textuelle de la location
        """
        return self.title
