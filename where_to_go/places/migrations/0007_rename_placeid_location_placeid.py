# Generated by Django 3.2.14 on 2022-07-09 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_location_placeid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='placeId',
            new_name='placeid',
        ),
    ]
