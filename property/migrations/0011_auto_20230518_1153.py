# Generated by Django 2.2.24 on 2023-05-18 08:53

from django.db import migrations
import phonenumbers


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        flat.owner_pure_phone = phonenumbers.format_number(
            phone_number, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230518_1129'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone)
    ]