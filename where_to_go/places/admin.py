from django.contrib import admin
from .models import Location, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableTabularInline


class ImageAdminInline(SortableTabularInline, admin.TabularInline):
    model = Image
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии'
    readonly_fields = ['get_preview', ]
    list_display = ['position', 'img_url', 'get_preview', ]
    extra = 0
    ordering = ['position', ]

    def get_preview(self, obj):
        return format_html(
            '<img src="{url}" "width="150" height="150"/>'.format(
                url=obj.img_url.url,
                )
            )


@admin.register(Location)
class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageAdminInline,
    ]


admin.site.register(Image)
