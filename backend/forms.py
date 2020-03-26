from django import forms

from backend.models import Venue


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        CHOICES = ((1, 'Active'), (0, 'Inactive'))
        widgets = {
            'venue_name': forms.TextInput(attrs={'class': 'form-control'}),
            'venue_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'venue_email': forms.TextInput(attrs={'class': 'form-control'}),
            'venue_total_room': forms.TextInput(attrs={'class': 'form-control'}),
            'venue_total_capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'venue_address': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'venue_status': forms.Select(choices=CHOICES, attrs={'class': 'form-control'}),
        }
