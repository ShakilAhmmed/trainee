from django.urls import path,include
from . import views

app_name = "backend"
urlpatterns = [
    path('', views.home, name="home"),
    path('venue/', include("backend.venue_urls"))
]
