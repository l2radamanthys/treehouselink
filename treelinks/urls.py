from django.urls import path
from django.conf.urls import include
from treelinks.views.home import HomePageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
