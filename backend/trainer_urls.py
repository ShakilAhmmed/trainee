from django.urls import path
from . import trainer_views

urlpatterns = [
	path('', trainer_views.trainer, name = "trainer"),
	# path('<int:pk>/delete', course_views.course_delete, name="course_delete"),
	# path('<int:pk>/status', course_views.course_status_change, name="course_status_change"),
	# path('<int:pk>/edit', course_views.course_edit, name="course_edit")
]
