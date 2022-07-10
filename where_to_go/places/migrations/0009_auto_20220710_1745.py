# Generated by Django 3.2.14 on 2022-07-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_location_title_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='images', to='places.Image', verbose_name='Картинки'),
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ManyToManyField(blank=True, related_name='locations', to='places.Location', verbose_name='Место'),
        ),
    ]
