"""
Migration pour transférer les données du modèle 'Profile' de 'oc_lettings_site'
vers 'profiles'.

Cette migration permet de transférer les données existantes du modèle 'Profile'
de l'ancienne application 'oc_lettings_site' vers la nouvelle application
'profiles'. Elle assure que les données de l'utilisateur, y compris la ville
favorite, sont correctement copiées dans le nouveau modèle.
"""
from django.db import migrations


def transfer_data(apps, schema_editor):
    """
    Transfert des données de l'ancien modèle 'Profile' vers le nouveau modèle
    'Profile'.

    Cette fonction parcourt tous les enregistrements de l'ancien modèle
    'Profile' et crée une copie des enregistrements dans le nouveau modèle
    'Profile' de l'application 'profiles'. Elle s'assure que les utilisateurs
    et leurs villes favorites sont correctement transférés.

    Paramètres :
        apps (Apps): L'instance qui permet d'accéder aux modèles avant qu'ils
        ne soient appliqués schema_editor (SchemaEditor): L'éditeur de schéma
        utilisé pour gérer la migration

    Retour :
        None
    """
    # Obtenez les anciens modèles
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')

    # Obtenez les nouveaux modèles
    NewProfile = apps.get_model('profiles', 'Profile')

    # Transférez les données des anciennes tables vers les nouvelles
    for old_profile in OldProfile.objects.all():
        new_profile = NewProfile.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )
        print(f"Created new profile: {new_profile}")


class Migration(migrations.Migration):
    """
    Migration pour transférer les données du modèle 'Profile' de l'ancienne
    application vers la
    nouvelle.
    """
    dependencies = [
        ('profiles', '0001_initial'),  # Dépend de la migration initiale
        ('oc_lettings_site', '0001_initial'),  # Dépend de l'ancienne app
    ]

    operations = [
        migrations.RunPython(transfer_data),
    ]
