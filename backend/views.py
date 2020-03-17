from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from .models import Venue
from .forms import VenueForm


# Create your views here.


def home(request):
    context = {
        "title": "Home"
    }
    return render(request, 'Backend/dashboard.html', context)


def venue(request):
    form = VenueForm()
    all_venues = Venue.objects.all().order_by('venue_name')
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Venue Created Successfully')
            return HttpResponseRedirect(reverse('backend:venue'))
    context = {
        "title": "Venue",
        "form": form,
        'all_venues': all_venues
    }
    return render(request, 'Backend/Venue/venue.html', context)
