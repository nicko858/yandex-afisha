from django.contrib import admin
from .models import Location, Image
from django.utils.html import format_html


class ImageAdminInline(admin.TabularInline):
    model = Image
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    readonly_fields = ['get_preview', ]
    fields = ['img_url', 'get_preview', 'position']
    extra = 0

    def get_preview(self, obj):
        return format_html(
            '<img src="{url}" "width="150" height="150"/>'.format(
                url=obj.img_url.url,
                )
            )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdminInline,
    ]


admin.site.register(Image)
