from django.contrib import admin
from .models import Location, Image


class ImageAdminInline(admin.TabularInline):
    model = Image
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    fields = ['img_url', 'position']
    extra = 0


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdminInline,
    ]


admin.site.register(Image)
