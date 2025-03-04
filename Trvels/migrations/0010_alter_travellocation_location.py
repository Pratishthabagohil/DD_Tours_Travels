# Generated by Django 5.1.6 on 2025-03-01 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trvels', '0009_travellocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travellocation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trsvels_locations', to='Trvels.location'),
        ),
    ]
