# Generated by Django 3.2.14 on 2022-07-09 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20220709_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='places.location', verbose_name='Картинка места'),
        ),
    ]