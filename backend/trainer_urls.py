from django.urls import path
from . import trainer_views

urlpatterns = [
	path('', trainer_views.trainer, name = "trainer"),
	path('<int:pk>/delete', trainer_views.trainer_delete, name="trainer_delete"),
	path('<int:pk>/edit', trainer_views.trainer_edit, name="trainer_edit")
]
