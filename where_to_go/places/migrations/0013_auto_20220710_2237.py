# Generated by Django 3.2.14 on 2022-07-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_auto_20220710_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AlterField(
            model_name='image',
            name='img_url',
            field=models.ImageField(blank=True, upload_to='places_images', verbose_name='Картинка'),
        ),
    ]
