import random

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .filter_form import VenueFilterForm
from .models import Venue
from .forms import VenueForm
from django.core.paginator import Paginator


# Create your views here.


def home(request):
	context = {
		"title": "Home"
	}
	return render(request, 'Backend/dashboard.html', context)


def venue(request):
	# for i in range(100):
	# 	venue_model = Venue()
	# 	venue_model.venue_name = f"Test{i}"
	# 	venue_model.venue_mobile = f"01817637{i}"
	# 	venue_model.venue_email = f"s{i}@gmail.com"
	# 	venue_model.venue_total_room = "120"
	# 	venue_model.venue_total_capacity = "120"
	# 	venue_model.venue_address = "Kaz"
	# 	venue_model.venue_status = random.choice([1, 2])
	# 	venue_model.save()
	form = VenueForm()
	all_venues = Venue.objects.all().order_by('venue_name')
	venue_filer_form = VenueFilterForm(request.GET, queryset = all_venues)
	all_venues = venue_filer_form.qs
	paginator = Paginator(all_venues, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	if request.method == "POST":
		form = VenueForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'New Venue Created Successfully')
			return HttpResponseRedirect(reverse('backend:venue'))
	context = {
		"title": "Venue",
		"form": form,
		'all_venues': page_obj,
		"venue_filer_form": venue_filer_form
	}
	return render(request, 'Backend/Venue/venue.html', context)


def venue_edit(request, pk):
	venue_data = Venue.objects.get(pk = pk)
	if request.method == "POST":
		form = VenueForm(request.POST, instance = venue_data)
		if form.is_valid():
			form.save()
			messages.success(request, "Venue Updated Successfully")
			return HttpResponseRedirect(reverse("backend:venue_edit", kwargs = {'pk': pk}))
	else:
		form = VenueForm(instance = venue_data)
	context = {
		"form": form
	}
	return render(request, 'Backend/Venue/venue_edit.html', context)


def venue_status_change(request, pk):
	venue_data = Venue.objects.get(pk = pk)
	if venue_data.venue_status == 1:
		venue_data.venue_status = 0
		messages.success(request, "Status Changed Into Inactive")
	else:
		venue_data.venue_status = 1
		messages.warning(request, "Status Changed Into Active")
	venue_data.save()
	return HttpResponseRedirect(reverse("backend:venue"))


def venue_delete(request, pk):
	venue_data = get_object_or_404(Venue, pk = pk)
	venue_data.delete()
	messages.error(request, 'Venue Deleted Successfully')
	return HttpResponseRedirect(reverse('backend:venue'))
