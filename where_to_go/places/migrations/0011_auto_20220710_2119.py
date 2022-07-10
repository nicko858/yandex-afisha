# Generated by Django 3.2.14 on 2022-07-10 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_remove_image_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.location', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='location',
            name='description_long',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='description_short',
            field=models.TextField(verbose_name='Сокращенное описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='placeid',
            field=models.CharField(blank=True, max_length=200, verbose_name='Идентификатор места'),
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='location',
            name='title_short',
            field=models.CharField(blank=True, max_length=100, verbose_name='Сокращенное название'),
        ),
    ]
