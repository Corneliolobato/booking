# Generated by Django 5.0.2 on 2024-09-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0002_alter_amenitiess_deskrisaun"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservated",
            name="sex",
            field=models.CharField(max_length=10),
        ),
    ]
