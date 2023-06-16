from django.contrib import admin
from treelinks.models.nodes import Node
from treelinks.models.links import Link


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


class NodeAdmin(admin.ModelAdmin):
    model = Node
    list_display = (
        'id',
        'user',
        'name',
        'active',
    )
    search_fields = ("name",)
    autocomplete_fields = ("user",)
    list_filter = ("user", "active")
    inlines = [
        LinkInline,
    ]