from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # When using class based views, we need to use as_view() when using the views class name.
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]