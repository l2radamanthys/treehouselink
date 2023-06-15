from django.contrib import admin
from treelinks.models.nodes import Node


class NodeAdmin(admin.ModelAdmin):
    model = Node
    list_display = (
        'id',
        'user',
        'name',
        'active',
    )

