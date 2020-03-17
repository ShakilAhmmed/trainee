from django.db import models


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
    venue_status = models.BooleanField(default=1)
