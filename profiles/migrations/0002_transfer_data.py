from django.db import migrations


def transfer_data(apps, schema_editor):
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


def reverse_transfer_data(apps, schema_editor):
    # Supprimez les données des nouvelles tables
    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),  # Dépend de la migration initiale
        ('oc_lettings_site', '0001_initial'),  # Dépend de l'ancienne application
    ]

    operations = [
        migrations.RunPython(transfer_data, reverse_transfer_data),
    ]