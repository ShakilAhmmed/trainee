import django_filters
from django_filters.widgets import BooleanWidget

from .models import Venue



class VenueFilterForm(django_filters.FilterSet):
	CHOICES = ((1, 'Active'), (0, 'Inactive'))
	venue_status = django_filters.BooleanFilter(
		widget = BooleanWidget(attrs = {"class": "form-control"}))

	venue_name = django_filters.CharFilter(lookup_expr = 'icontains')
	venue_mobile = django_filters.CharFilter(lookup_expr = 'icontains')

	class Meta:
		model = Venue
		fields = "__all__"
