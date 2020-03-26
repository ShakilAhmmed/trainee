from django.urls import path
from . import views

urlpatterns = [
    path('', views.venue, name="venue"),
    path('<int:pk>/delete', views.venue_delete, name="venue_delete"),
    path('<int:pk>/status', views.venue_status_change, name="venue_status_change"),
    path('<int:pk>/edit', views.venue_edit, name="venue_edit")
]
