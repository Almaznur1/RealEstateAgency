# Generated by Django 2.2.24 on 2023-05-17 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='who_complained',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]