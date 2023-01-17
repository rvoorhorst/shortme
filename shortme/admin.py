from django.contrib import admin

from shortme.models import URLData


class URLDataAdmin(admin.ModelAdmin):
    list_display = ["__str__", "hash", "times_used", "created_at"]


admin.site.register(URLData, URLDataAdmin)
