from django.views.generic import TemplateView
from treelinks.models.nodes import Node


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nodes"] = Node.objects.all()
        return context
