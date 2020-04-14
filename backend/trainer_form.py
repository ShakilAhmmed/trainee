from django import forms

from .models import Trainer


class TrainerForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = "__all__"
        GENDER_CHOICES = ((1, 'Male'), (2, 'Female'))
        RELIGION_CHOICES = ((1, 'Islam'), (2, 'Hindu'),
                            (3, 'Budha'), (4, 'Khristian'))
        EDUCATION_CHOICES = (('SSC','SSC'),('DIPLOMA','DIPLOMA'),('HSC','HSC'),('BSC','BSC'),('MSC','MSC'))
        widgets = {
            "trainer_name": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-control"}),
            "national_id": forms.NumberInput(attrs={"class": "form-control"}),
            "birth_reg_no": forms.TextInput(attrs={"class": "form-control"}),
            "birth_reg_no": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(choices=GENDER_CHOICES, attrs={"class": "form-control"}),
            "religion": forms.Select(choices=RELIGION_CHOICES, attrs={"class": "form-control"}),
            "mobile_number": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "exp_years": forms.NumberInput(attrs={"class": "form-control"}),
            "nationality": forms.TextInput(attrs={"class": "form-control"}),
            "level_of_education": forms.Select(choices=EDUCATION_CHOICES,attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "is_foreign_trainer": forms.CheckboxInput(),
            "is_guest_trainer": forms.CheckboxInput(),
            "area_of_expertise": forms.Textarea(attrs={"class": "form-control","rows":"2"}),
            "list_of_expertise": forms.Textarea(attrs={"class": "form-control","rows":"2"}),
            "is_bteb_registered": forms.CheckboxInput(),
            "bteb_register_number": forms.NumberInput(attrs={"class": "form-control"}),
        }
