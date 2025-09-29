from django.urls import path
from .views import home_view, landing_view

urlpatterns = [
    path("", home_view, name="home"),
    path("home/", home_view, name="home_explicit"),
    path("landing/", landing_view, name="landing"),
]
