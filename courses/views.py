from django.shortcuts import render
from .models import Course
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)


# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'courses/course_list.html'

class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course_detail'
    template_name = 'courses/course_detail.html'