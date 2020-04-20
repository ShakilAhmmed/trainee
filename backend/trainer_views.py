from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from .trainer_form import TrainerForm
from .models import Trainer, Venue, Course, CourseMap
from django.contrib import messages


def trainer(request):
	form = TrainerForm()
	all_trainer = Trainer.objects.all()
	all_venue = Venue.objects.filter(venue_status = 1)
	all_course = Course.objects.filter(course_status = 1)
	if request.method == "POST":
		venue = request.POST.getlist("venue[]")
		course = request.POST.getlist("course[]")
		form = TrainerForm(request.POST, request.FILES)
		if form.is_valid():
			with transaction.atomic():
				main_form = form.save()
				course_map_all_data = []
				for counter in range(len(venue)):
					course_map = CourseMap()
					course_map.trainer = main_form
					course_map.course = get_object_or_404(Course, pk = course[counter])
					course_map.venue = get_object_or_404(Venue, pk = venue[counter])
					course_map_all_data.append(course_map)
				CourseMap.objects.bulk_create(course_map_all_data)
			messages.success(request, 'Trainer Added Successfully')
			return HttpResponseRedirect(reverse("backend:trainer"))

	context = {
		"form": form,
		"all_trainer": all_trainer,
		"all_venue": all_venue,
		"all_course": all_course
	}
	return render(request, "Backend/Trainer/trainer.html", context)
