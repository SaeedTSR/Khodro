# Generated by Django 4.2.2 on 2023-08-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("khodro", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="khodro",
            name="owner_phone",
            field=models.CharField(max_length=11),
        ),
    ]
