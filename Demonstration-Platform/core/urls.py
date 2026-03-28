from django.urls import path
from .views import home_view, landing_page, dashboard_view, sliders_view

urlpatterns = [

    path("landing/", landing_page, name="landing_page"),
    path("", home_view, name="home"),
    path("home/", home_view, name="home_explicit"),
    path('dashboard/', dashboard_view, name='dashboard'),  
    
    # interactive experiences
    path('exp/sliders', sliders_view, name='sliders')
    
]
