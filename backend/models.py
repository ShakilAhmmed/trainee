from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
# from .signals import create_slug
# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Venue(TimeStamp):
    venue_name = models.CharField(max_length=100, unique=True)
    venue_mobile = models.CharField(max_length=20, unique=True)
    venue_email = models.EmailField(max_length=50, unique=True)
    venue_total_room = models.IntegerField()
    venue_total_capacity = models.IntegerField()
    venue_address = models.TextField()
    venue_status = models.IntegerField(default=1)

class Course(TimeStamp):
    course_code = models.CharField( unique=True , max_length=100)
    course_name = models.CharField( unique=True , max_length=100 )
    course_slug = models.SlugField(max_length = 250, null = True, blank = True)
    course_duration = models.IntegerField()
    course_fee = models.IntegerField()
    course_content = models.TextField()
    course_status = models.IntegerField(default=1)

# Signals Call
@receiver(pre_save,sender=Course)
def create_slug(sender, instance, *args, **kwargs):
    instance.course_slug = slugify(instance.course_name)
