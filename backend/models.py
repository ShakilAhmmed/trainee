from django.db import models


# from .signals import create_slug
# Create your models here.
class TimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True


class Venue(TimeStamp):
	venue_name = models.CharField(max_length = 100, unique = True)
	venue_mobile = models.CharField(max_length = 20, unique = True)
	venue_email = models.EmailField(max_length = 50, unique = True)
	venue_total_room = models.IntegerField()
	venue_total_capacity = models.IntegerField()
	venue_address = models.TextField()
	venue_status = models.IntegerField(default = 1)


class Course(TimeStamp):
	course_code = models.CharField(unique = True, max_length = 100)
	course_name = models.CharField(unique = True, max_length = 100)
	course_slug = models.SlugField(max_length = 250, null = True, blank = True)
	course_duration = models.IntegerField()
	course_fee = models.IntegerField()
	course_content = models.TextField()
	course_status = models.IntegerField(default = 1)


class Trainer(TimeStamp):
	trainer_name = models.CharField(max_length = 100)
	date_of_birth = models.DateField()
	national_id = models.IntegerField(unique = True)
	birth_reg_no = models.IntegerField(unique = True, null = True, blank = True)
	gender = models.BooleanField(default = 1)
	religion = models.IntegerField()
	mobile_number = models.CharField(max_length = 100)
	email = models.EmailField(unique = True)
	exp_years = models.IntegerField(default = 0)
	nationality = models.CharField(max_length = 100)
	level_of_education = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = "trainer/")
	is_foreign_trainer = models.BooleanField(default = 0)
	is_guest_trainer = models.BooleanField(default = 0)
	area_of_expertise = models.TextField()
	list_of_expertise = models.TextField()
	is_bteb_registered = models.BooleanField(default = 0)
	bteb_register_number = models.IntegerField(null = True, blank = True)


class CourseMap(TimeStamp):
	trainer = models.ForeignKey(Trainer, on_delete = models.CASCADE)
	venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
	course = models.ForeignKey(Course, on_delete = models.CASCADE)

# # Signals Call
# @receiver(pre_save, sender = Course)
# def create_slug(sender, instance, *args, **kwargs):
# 	instance.course_slug = slugify(instance.course_name)
