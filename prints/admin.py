from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Print
# Register your models here.

class PrintAdmin(admin.ModelAdmin):

    readonly_fields = ["photo"]
    list_display = ['title', 'price']
    def photo(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width / 6,
            height=obj.image.height / 6,
            )
    )

admin.site.register(Print, PrintAdmin)
