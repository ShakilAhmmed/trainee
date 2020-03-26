from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .course_form import CourseForm
from django.contrib import messages
from django.urls import reverse
from .models import Course

def course(request):
    all_courses = Course.objects.all()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Course Added Successfully")
            return HttpResponseRedirect(reverse("backend:course"))
    else:
        form = CourseForm()
    context = {
        "form": form,
        "title" : "Courses",
        'all_courses' : all_courses
    }
    return render(request, 'Backend/Course/course.html', context)

def course_delete( request , pk ):
    course_data = get_object_or_404(Course , pk=pk)
    course_data.delete()
    messages.warning( request , "Course Deleted Successfully")
    return HttpResponseRedirect(reverse("backend:course"))

def course_status_change(request, pk):
    course_data = Course.objects.get(pk=pk)
    if course_data.course_status == 1:
        course_data.course_status = 0
        messages.success(request, "Status Changed Into Inactive")
    else:
        course_data.course_status = 1
        messages.warning(request, "Status Changed Into Active")
    course_data.save()
    return HttpResponseRedirect(reverse("backend:course"))

def course_edit( request, pk ):
    course_data = Course.objects.get( pk = pk)
    if request.method == "POST":
        form = CourseForm( request.POST , instance=course_data)
        if form.is_valid():
            form.save()
            messages.success( request , "Course Updated Successfully")
            return HttpResponseRedirect( reverse("backend:course_edit",kwargs={'pk':pk}) )
    else:
        form = CourseForm( instance=course_data )
    context = {
        "form" : form
    }
    return render( request , 'Backend/Course/course_edit.html' , context)
