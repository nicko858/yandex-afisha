from django.db import models
from tinymce import models as tinymce_models

# Create your models here.


class Location(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        unique=True,
        )
    title_short = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Сокращенное название',
        )
    description_short = models.TextField(verbose_name='Сокращенное описание')
    description_long = tinymce_models.HTMLField(verbose_name='Описание')
    lng = models.FloatField(verbose_name='Широта')
    lat = models.FloatField(verbose_name='Долгота')
    placeid = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Идентификатор места',
        )

    def __str__(self):
        return self.title


class Image(models.Model):
    img_url = models.ImageField(
        upload_to='places_images',
        blank=True,
        verbose_name='Картинка',
        unique=True,
        )
    location = models.ForeignKey(
        Location,
        related_name='images',
        null=True,
        verbose_name='Место',
        on_delete=models.SET_NULL,
        )
    position = models.PositiveIntegerField(
        verbose_name='Позиция',
        default=0,
        db_index=True,
        )

    def __str__(self):
        return '{} {}'.format(self.id, self.location)
