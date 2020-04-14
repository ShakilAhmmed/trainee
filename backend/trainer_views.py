from django.http import HttpResponse
from django.shortcuts import render
from .trainer_form import TrainerForm
from .models import Trainer, Venue, Course


def trainer(request):
	form = TrainerForm()
	all_trainer = Trainer.objects.all()
	all_venue = Venue.objects.filter(venue_status = 1)
	all_course = Course.objects.filter(course_status = 1)
	context = {
		"form": form,
		"all_trainer": all_trainer,
		"all_venue": all_venue,
		"all_course": all_course
	}
	return render(request, "Backend/Trainer/trainer.html", context)
