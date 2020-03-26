from django import forms
from .models import Course
class CourseForm( forms.ModelForm ):

      class Meta:
          model = Course
          fields = "__all__"
          CHOICES = ((1, 'Active'), (0, 'Inactive'))
          widgets = {
            'course_code' : forms.TextInput( attrs={'class':'form-control'} ),
            'course_name' : forms.TextInput( attrs={'class':'form-control'} ),
            'course_duration' : forms.TextInput( attrs={'class':'form-control'} ),
            'course_fee' : forms.TextInput( attrs={'class':'form-control'} ),
            'course_content' : forms.Textarea( attrs={'class':'richtexteditor', 'id':'editor'} ),
            'course_status': forms.Select( choices=CHOICES, attrs={'class': 'form-control'}),
          }
