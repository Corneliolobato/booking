# Generated by Django 5.0.2 on 2024-05-27 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0007_remove_guest_address_guest_sex"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomoccupied",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roomoccupiedroom",
                to="apps.room",
            ),
        ),
    ]
