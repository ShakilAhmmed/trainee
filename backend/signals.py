from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Course


# Signals Call
@receiver(pre_save, sender = Course)
def create_slug(sender, instance, *args, **kwargs):
	instance.course_slug = slugify(instance.course_name)
