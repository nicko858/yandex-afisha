# Generated by Django 4.0.6 on 2022-07-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0020_alter_image_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_url',
            field=models.ImageField(blank=True, upload_to='places_images', verbose_name='Картинка'),
        ),
    ]