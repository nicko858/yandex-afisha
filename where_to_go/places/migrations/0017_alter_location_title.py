# Generated by Django 4.0.6 on 2022-07-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0016_alter_location_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
    ]
