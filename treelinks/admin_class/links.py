from django.contrib import admin
from treelinks.models.links import Link


class LinkAdmin(admin.ModelAdmin):
    model = Link
    list_display = (
        'id',
        'node',
        'name',
        'uri',
        'active',
    )
    search_fields = ("name", "uri")
    autocomplete_fields = ("node",)
    list_filter = ("node", "active")
