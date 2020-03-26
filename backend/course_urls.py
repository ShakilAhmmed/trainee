from django.urls import path
from . import course_views

urlpatterns = [
    path('', course_views.course, name="course"),
    path('<int:pk>/delete', course_views.course_delete, name="course_delete"),
    path('<int:pk>/status', course_views.course_status_change, name="course_status_change"),
    path('<int:pk>/edit', course_views.course_edit, name="course_edit")
]
