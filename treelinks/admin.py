from django.contrib import admin

# Register your models here.
from treelinks.admin_class.nodes import Node, NodeAdmin
from treelinks.admin_class.links import Link, LinkAdmin

admin.site.register(Node, NodeAdmin)
admin.site.register(Link, LinkAdmin)

