from django.db import migrations


def transfer_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')

    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    # Vérifiez les données des anciennes tables
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

def reverse_transfer_data(apps, schema_editor):
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    # Supprimez les données des nouvelles tables
    NewLetting.objects.all().delete()
    NewAddress.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),  # Dépend de la migration initiale
    ]

    operations = [
        migrations.RunPython(transfer_data, reverse_transfer_data),
    ]