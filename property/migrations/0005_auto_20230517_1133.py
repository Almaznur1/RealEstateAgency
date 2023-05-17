# Generated by Django 2.2.24 on 2023-05-17 08:33

from django.db import migrations


def fill_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = True if flat.construction_year >= 2015 else False
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20230516_1002'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_field)
    ]