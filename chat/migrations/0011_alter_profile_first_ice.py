# Generated by Django 3.2 on 2022-01-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_profile_first_ice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_ice',
            field=models.BooleanField(default=True),
        ),
    ]
