from django.db import models

# Create your models here.


class Location(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()
    img_url = models.ForeignKey('Image',
                                verbose_name='Картинка места',
                                null=True,
                                blank=True,
                                related_name='img',
                                on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    img_url = models.ImageField(
        upload_to='places_images',
        blank=True,
        verbose_name='Путь к картинке'
        )

    def __str__(self):
        return self.title
