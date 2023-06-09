# Generated by Django 2.2.24 on 2023-05-20 08:57

from django.db import migrations


def fill_owner_model(apps, schema_editor):
    Flat = apps.get_model('property', 'flat')
    Owner = apps.get_model('property', 'owner')
    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(owner=flat.owner,
                                    owners_phonenumber=flat.owners_phonenumber,
                                    owner_pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owner_model)
    ]
