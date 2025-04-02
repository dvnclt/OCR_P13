"""
Migration Django pour la création des modèles Address et Letting

Cette migration définit la structure de la base de données pour les adresses et les locations
Elle comprend la création des modèles et la définition des champs avec leurs contraintes

Une migration supplémentaire permet de transférer les données des anciens modèles vers les nouveaux
"""
from django.db import migrations


def transfer_data(apps, schema_editor):
    """
    Transfère les données des anciens modèles Address et Letting vers les nouveaux

    Récupère les anciennes données, les copie dans les nouvelles tables et affiche des logs pour
    le suivi du processus
    """
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')

    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    # Vérifie les données des anciennes tables
    print(f"OldAddress count: {OldAddress.objects.count()}")
    print(f"OldLetting count: {OldLetting.objects.count()}")

    for old_address in OldAddress.objects.all():
        print(f"Transferring address: {old_address}")
        new_address = NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )
        print(f"Created new address: {new_address}")

    for old_letting in OldLetting.objects.all():
        print(f"Transferring letting: {old_letting}")
        new_letting = NewLetting.objects.create(
            title=old_letting.title,
            address=NewAddress.objects.get(pk=old_letting.address_id),
        )
        print(f"Created new letting: {new_letting}")


class Migration(migrations.Migration):
    """
    Migration permettant le transfert des données des anciens modèles vers les nouveaux
    """
    dependencies = [
        ('lettings', '0001_initial'),  # Dépend de la migration initiale
    ]

    operations = [
        migrations.RunPython(transfer_data),
    ]
