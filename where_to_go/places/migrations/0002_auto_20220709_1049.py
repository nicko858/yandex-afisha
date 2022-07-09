# Generated by Django 3.2.14 on 2022-07-09 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img_url', models.ImageField(blank=True, upload_to='places_images', verbose_name='Путь к картинке')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='img_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='img', to='places.image', verbose_name='Картинка места'),
        ),
    ]
