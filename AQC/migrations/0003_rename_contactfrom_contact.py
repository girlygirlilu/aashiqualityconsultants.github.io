# Generated by Django 4.1.3 on 2022-12-10 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AQC', '0002_contactfrom_timestamp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contactfrom',
            new_name='Contact',
        ),
    ]
