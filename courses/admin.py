from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    inlines = []

# Register your models here.
admin.site.register(Course,CourseAdmin)