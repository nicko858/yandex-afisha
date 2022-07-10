from django.contrib import admin
from .models import Location, Image


class PlaceImagesInline(admin.TabularInline):
    model = Location.images.through
    raw_id_fields = ('image', 'location',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    exclude = ('images',)
    inlines = [
        PlaceImagesInline,
    ]


admin.site.register(Image)
