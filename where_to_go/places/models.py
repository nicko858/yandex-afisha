from django.db import models

# Create your models here.


class Location(models.Model):
    title = models.CharField(max_length=200)
    title_short = models.CharField(max_length=100, blank=True)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()
    placeid = models.CharField(
        max_length=200,
        blank=True,
        )

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    img_url = models.ImageField(
        upload_to='places_images',
        blank=True,
        verbose_name='Путь к картинке'
        )
    location = models.ForeignKey(
        'Location',
        verbose_name='Место',
        null=True,
        blank=True,
        related_name='images',
        on_delete=models.SET_NULL,
        )

    def __str__(self):
        return self.title
